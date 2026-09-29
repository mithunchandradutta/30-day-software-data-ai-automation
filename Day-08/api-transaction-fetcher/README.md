# API Transaction Fetcher (Day 8)

A small Python tool that fetches currency exchange rates (USD → BDT, EUR) from a public API, **validates** them, saves them to a JSON file, and keeps a **log** of every run.

**Why I built it:** My [Finance Tracker](../) handles multi-currency transactions. Instead of typing exchange rates by hand, I want to pull them from an API. This is the first step: API call → validation → save → log.

---

## Folder structure

```
api-transaction-fetcher/
├── fetch_rates.py        # main script: API call, save, log
├── validators.py         # rate and response validation
├── data/
│   └── rates_latest.json # latest fetched rates (created on run)
├── logs/
│   └── fetch_log.txt     # summary of every run (created on run)
├── README.md
└── .gitignore
```

---

## Setup

```bash
pip install requests
```

## Run

```bash
python fetch_rates.py
```

Output:
```
Saved 2 rates at 2026-09-27T10:15:00+00:00
```

The files are created in the correct places (`data/`, `logs/`) no matter which folder you run the script from.

---

## How it works

```
API call → check response → validate rates → save JSON → write log
```

1. `fetch_rates()` sends a GET request to the API (`timeout=10`)
2. `validate_response()` checks that the response is a `success` and contains `rates`
3. `validate_rates()` splits the requested currencies into:
   - **valid**: the rate is a positive number
   - **invalid**: present, but the value is bad (negative, string, `null`)
   - **missing**: not in the response at all
4. `save_result()` writes the valid rates to `data/rates_latest.json`
5. `write_log()` appends a summary to `logs/fetch_log.txt`

---

## Validation rules

| Rule | If it fails |
|---|---|
| Response is a JSON object with `result == "success"` | `ValueError` |
| `rates` is not empty | `ValueError` |
| Rate is a number, `> 0`, not NaN/Infinity, not `True/False` | skipped as invalid |
| Requested currency exists in the response | skipped as missing |
| No valid rate at all | `ValueError`, nothing is saved |

---

## Sample output

**`data/rates_latest.json`**
```json
{
  "base": "USD",
  "rates": {
    "BDT": 122.5,
    "EUR": 0.85
  },
  "requested": ["BDT", "EUR"],
  "invalid": {},
  "missing": [],
  "source": "open.er-api.com",
  "fetched_at": "2026-09-27T10:15:00+00:00"
}
```
(The numbers above are examples. A real run returns the current rates.)

**`logs/fetch_log.txt`**
```
================================
CURRENCY RATE FETCH SUMMARY
================================

Base Currency:   USD
Rates Fetched:   2 (BDT, EUR)
Invalid Rates Skipped: 0
Fetched At:      2026-09-27T10:15:00+00:00

Saved to: data/rates_latest.json

Validation: PASSED
```

On failure:
```
Validation: FAILED
Error: API request failed: ...
```

---

## Error handling

| Problem | What happens |
|---|---|
| No internet / timeout | `RuntimeError`, log shows `FAILED`, exit code 1 |
| 4xx / 5xx response | Caught by `raise_for_status()`, fails the same way |
| Response is not valid JSON | `RuntimeError` |
| API itself reports a failure | `ValueError` |

If a run fails, the previous `rates_latest.json` stays untouched.

---

## Important notes about the API

- Endpoint used: `https://open.er-api.com/v6/latest/USD` (ExchangeRate-API Open Access endpoint)
- **No API key required**
- Data updates only **once per day**, so calling it repeatedly gives no benefit
- Too many requests can return `429`; the limit lifts after about 20 minutes. Calling once a day or once an hour is safe
- **Attribution is required:** if rates are shown on a public page, link to [ExchangeRate-API](https://www.exchangerate-api.com)

---

## What I learned on Day 8

- Calling an API with `requests.get()`, including `params` and `timeout`
- Error handling with `raise_for_status()` and `try/except`
- Validating API responses instead of trusting them blindly
- Splitting code into small files (`fetch_rates.py` + `validators.py`)
- Keeping a log so I can see later what happened and when

## Next steps (ideas)

- [ ] Use these rates in the Finance Tracker's `Exchange Rate` column
- [ ] Cache the rates (no new API call within 24 hours)
- [ ] Add retry logic and `429` handling
- [ ] Write unit tests for `validators.py`

## Security

- This project contains no secret keys
- If I use a paid API in the future, the key goes in `.env`, not in code. `.env` is already in `.gitignore`