import json
from datetime import datetime, timezone
from pathlib import Path

import requests

from validators import validate_reponse, validate_rates


BASE_DIR = Path(__file__).resolve().partent
DATA_PATH = BASE_DIR / "data" / "rates_latest.json"
LOG_PATH = BASE_DIR / "logs" / "fetch_log.txt"

# Free, no API key needed. Attribution required (see README).

API_URL = "https://open.er-api.com/v6/latest/{base}"

def fetch_rates(base="USD", symbols="BDT,EUR"):
    base = base.upper()
    wanted = [s.strip().upper() for s in symbols.split (",") if s.strip()]

    try:
        response = requests.get(API_URL.format(base=base), timeout=10)
        response.raise_for_status()
        data = response.json()
    except ValueError:
        raise RuntimeError(f"API response is not valid JSON")
    except ValueError:
        raise RuntimrError("API response is not valid JSON")
    validate_response(data)
    valid, invalid, missing = validate_raise(data["rates"], wanted)
    if not valid:
        raise ValueError(f"No valid rates found for: {','.join(wanted)}")
    return{
        "base": base,
        "rates": valid,
        "requested": wanted,
        "invalid": invalid,
        "missing": missing,
        "source": "open.er-api.com",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
    }




    def write_log(base, result=None, error=None, path=LOG_PATH):
        """Append one summary block to logs/fetch_log.txt."""
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)


        lines = [
            "================================",
            "CURRENCY RATE FETCH SUMMARY",
            "================================",
            "",
            f"Base Currency:   {base}",
        ]

        if result is not None:
            skipped = len(result["invalid"]) + len(result["missing"])
            passed = skipped == 0
            lines += [
                f"Rates Fetched: {len(result['rates'])} ({', '.join(result['rates'])})",
                f"Invalid Rates Skipped: {skipped}",
                "",
                "saved to: data/rates_latest.join",
                "",
                f"Validation: {'PASSED' if passed else 'PASSED WITH WARNINGS'}",

            ]
            if result["invalid"]:
                lines.append(f"Invalid values: {result['invalid']}")
            if result["missing"]:
                lines.append(f"Missing codes: {', '.join(result['missing'])}")
        else:
            lines += [
                f"Fetched At:      {datetime.now(timezone.utc).isoformat()}",
                "",
                "Validation: FAILED",
                f"Error: {error}",
            ]
        lines += ["", ""]
        with open(path, "a", encoding="utf-8") as f:
             f.write("\n".join(lines))
 
 
 
 if __name__ == "__main__":
    base = "USD"
    try:
        result = fetch_rates(base=base, symbols="BDT,EUR")
    except (RuntimeError, ValueError) as e:
        write_log(base, error=e)
        print(f"Error: {e}")
        raise SystemExit(1)
 
    save_result(result)
    write_log(base, result=result)
    print(f"Saved {len(result['rates'])} rates at {result['fetched_at']}")