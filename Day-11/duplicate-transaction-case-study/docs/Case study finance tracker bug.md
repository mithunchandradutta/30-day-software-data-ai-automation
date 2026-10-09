# Case Study: Finance Tracker-e Duplicate Transaction Risk (sanitized)

> Ekhane kono real amount/account nai. Shob example sample data.

## 1. Ki hoyechilo?
Google Apps Script Finance Tracker-e (`Form.html` -> `Code.gs`) ekta transaction submit korar shomoy
ekoi transaction 2 bar `Code.gs`-e pouchate parto.

## 2. Keno hoto?
- User double-click korlo
- Network slow chhilo, client bhabe fail hoyeche, abar pathalo (retry) - kintu server ager-ta process kore felechhe
- User browser back chepe abar submit korlo

Mul somossha: **server janto na je ei request ta ager-tar-i "same" kina.**

## 3. Prothom fix: fingerprint
`date + amount + description` jure ekta text banano. Same text dekhle skip.
- Bhalo: ashol duplicate dhorto.
- Weakness: duita ASHOLE alada transaction (2 ta coffee, same din, same dam) hole 2nd ta bhul kore skip hoye jeto.

## 4. Proper fix (Day 11)
1. Client prottek request-e ekta `request_id` pathay (retry-te SAME id).
2. Server age `request_id` ta `processed_events` table-e likhe "claim" kore.
3. Table-e `request_id` **PRIMARY KEY**, tai duibar claim kora jay na - database nijei atkay.
4. Claim fail = age-i hoyeche = notun kore process korbo na.

## 5. Layered protection
| Layer | Ki | Guarantee? |
|---|---|---|
| Client | Button disable | Na (shudhu bhalo UX) |
| Code | "age-i hoyeche?" check | Na (race condition-e fail kore) |
| Database | `request_id PRIMARY KEY` | **Ha** |

## 6. Shikha
Asol guarantee shob shomoy database-e thake - UI ba application code-e na.