"""Validation helpers for the currency rate fetcher.

Rule: never trust API data blindly. Check it before saving it.
"""

import math


def is_valid_rate(rate):
    """A rate is valid if it is a real number greater than 0."""
    if isinstance(rate, bool):  # True/False are ints in Python, reject them
        return False
    if not isinstance(rate, (int, float)):
        return False
    if math.isnan(rate) or math.isinf(rate):
        return False
    return rate > 0


def validate_response(data):
    """Check the overall shape of the API response.

    Raises ValueError if the response is not usable.
    """
    if not isinstance(data, dict):
        raise ValueError("API response is not a JSON object")

    if data.get("result") != "success":
        error_type = data.get("error-type", "unknown error")
        raise ValueError(f"API returned failure: {error_type}")

    rates = data.get("rates")
    if not isinstance(rates, dict) or not rates:
        raise ValueError("No rates found in API response")


def validate_rates(rates, symbols):
    """Split the requested currencies into valid, invalid and missing.

    rates   : dict from the API, e.g. {"BDT": 122.5, "EUR": 0.85, ...}
    symbols : list of currency codes we asked for, e.g. ["BDT", "EUR"]

    Returns (valid, invalid, missing):
        valid   -> {"BDT": 122.5}          rate is a positive number
        invalid -> {"EUR": -1}             present but bad value
        missing -> ["GBP"]                 not in the response at all
    """
    valid = {}
    invalid = {}
    missing = []

    for code in symbols:
        if code not in rates:
            missing.append(code)
        elif is_valid_rate(rates[code]):
            valid[code] = rates[code]
        else:
            invalid[code] = rates[code]

    return valid, invalid, missing