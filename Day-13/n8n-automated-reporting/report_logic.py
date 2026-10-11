# report_logic.py - Day 13-er main function gulo
#
# Flow:   age-i pathano hoyeche? -> data anao (query) -> report banao -> pathao -> "pathano hoyeche" likhe rakho
#         kono step-e bhul hole -> ALERT likho (chupchap fail korbe na)
import os


# ---------- 1. Data ana ----------
def get_summary(conn, period):
    rows = conn.execute(
        "SELECT category, type, SUM(ABS(amount)), COUNT(*) "
        "FROM transactions WHERE strftime('%Y-%m', date) = ? "
        "GROUP BY category, type ORDER BY type DESC, SUM(ABS(amount)) DESC",
        (period,),
    ).fetchall()
    return rows


# ---------- 2. Report banano ----------
def build_report_text(period, rows):
    lines = []
    lines.append("Monthly Report - " + period)
    lines.append("=" * 30)

    # Edge case: ei mashe kono transaction nai
    if len(rows) == 0:
        lines.append("No transactions this period.")
        return "\n".join(lines)

    total_income = 0
    total_expense = 0
    for row in rows:
        category = row[0]
        tx_type = row[1]
        total = row[2]
        count = row[3]
        lines.append(tx_type + " | " + category + " | " + str(round(total, 2)) + " (" + str(count) + " tx)")
        if tx_type == "income":
            total_income = total_income + total
        else:
            total_expense = total_expense + total

    lines.append("-" * 30)
    lines.append("Total income : " + str(round(total_income, 2)))
    lines.append("Total expense: " + str(round(total_expense, 2)))
    lines.append("Net          : " + str(round(total_income - total_expense, 2)))
    return "\n".join(lines)


# ---------- 3. Idempotency: age-i pathano hoyeche? ----------
def already_sent(conn, period):
    row = conn.execute("SELECT 1 FROM report_log WHERE period = ?", (period,)).fetchone()
    return row is not None


def mark_sent(conn, period):
    conn.execute("INSERT INTO report_log (period, sent_at) VALUES (?, datetime('now'))", (period,))
    conn.commit()


# ---------- 4. Pathano (ekhane file-e save; n8n-e email/Telegram hobe) ----------
def deliver_to_file(period, text, out_folder):
    os.makedirs(out_folder, exist_ok=True)       # folder na thakle banay
    f = open(out_folder + "/report_" + period + ".txt", "w", encoding="utf-8")
    f.write(text + "\n")
    f.close()


# ---------- 5. Alert: bhul hole chupchap thakbo na ----------
def write_alert(period, message, out_folder):
    os.makedirs(out_folder, exist_ok=True)
    f = open(out_folder + "/ALERTS.log", "a", encoding="utf-8")    # "a" = shesh-e jog koro
    f.write("period=" + period + " ERROR: " + message + "\n")
    f.close()
    print("ALERT:", message)


# ---------- Shob ekshathe ----------
def run_report(conn, period, out_folder="outputs"):
    """Return: 'sent' | 'skipped' | 'error'"""
    try:
        if already_sent(conn, period):
            return "skipped"                       # duplicate report jabe na

        rows = get_summary(conn, period)
        text = build_report_text(period, rows)
        deliver_to_file(period, text, out_folder)
        mark_sent(conn, period)                    # pathanor POR mark kori; pathate bhul hole mark hobe na -> retry kora jabe
        return "sent"
    except Exception as error:
        write_alert(period, str(error), out_folder)
        return "error"
