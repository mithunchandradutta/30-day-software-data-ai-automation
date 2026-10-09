# Exercise 02 - Fingerprint diye duplicate dhora (Finance Tracker-er purono fix)
#
# Fingerprint = date + amount + description jure ekta text banano.
# Same fingerprint dekhle bujhi "eta age dekhechi" -> skip.


def build_fingerprint(date, amount, description):
    return date + "|" + str(amount) + "|" + description.strip().lower()


seen_fingerprints = []     # je fingerprint gulo age dekhechi (real tracker-e eta sheet/DB-te thakto)


def add_with_fingerprint(date, amount, description):
    fp = build_fingerprint(date, amount, description)
    if fp in seen_fingerprints:
        return "SKIPPED (duplicate)"
    seen_fingerprints.append(fp)
    return "SAVED"


print("--- Case 1: ashol duplicate (double-click) ---")
print(add_with_fingerprint("2026-09-10", -150, "Lunch"))   # SAVED
print(add_with_fingerprint("2026-09-10", -150, "Lunch"))   # SKIPPED  <- bhalo, kaj korlo

print("\n--- Case 2: duita ALADA coffee, same din, same dam ---")
print(add_with_fingerprint("2026-09-11", -80, "Coffee"))   # SAVED
print(add_with_fingerprint("2026-09-11", -80, "Coffee"))   # SKIPPED  <- BHUL! eta ashole 2nd coffee
print("\nSomossha: fingerprint 'ashol duplicate' ar 'ashole alada duita' alada korte pare na.")
print("Solution: client prottek request-e ekta unique request_id pathabe (Exercise 03).")