# Exercise 01 - Idempotent ki, ar non-idempotent ki?
#
# Idempotent = ekoi kaj 1 bar kori ba 5 bar kori, FINAL RESULT ekoi.

# ---- Non-idempotent: "balance-e 500 jog koro" ----
balance = 1000
for attempt in range(5):        # network retry-te 5 bar chole gelo
    balance = balance + 500
print("'500 jog koro' 5 bar  ->", balance, " (BHUL: 3500 hoye gelo)")

# ---- Idempotent: "balance 1500 koro" ----
balance = 1000
for attempt in range(5):
    balance = 1500
print("'balance 1500 koro' 5 bar ->", balance, " (THIK: shobshomoy 1500)")

print("\nShikha: 'jog koro' non-idempotent, 'eta set koro' idempotent.")
print("POST /transactions (notun transaction banao) by default non-idempotent.")
print("Tai request_id diye seta-ke 'effectively idempotent' banate hoy (Day 11/12).")