# Exercise 06 -- ER Diagram (Practice Lab)

Full ER diagram `diagrams/er_diagram.png` ar `diagrams/er_diagram.md` (Mermaid)
e ache -- eta shudhu prottekta relationship হাতে explain kore rakhার jonno,
jate video/LinkedIn post-e explain korার somoy dekhe bolte paro.

| Table | Primary Key | Foreign Key(s) | Relationship |
|---|---|---|---|
| `accounts` | `id` | -- | -- |
| `categories` | `id` | -- | -- |
| `transactions` | `id` | `account_id` -> accounts.id, `category_id` -> categories.id | accounts (1) -> (many) transactions; categories (1) -> (many) transactions |
| `loans` | `id` | `account_id` -> accounts.id | accounts (1) -> (many) loans |
| `investments` | `id` | `account_id` -> accounts.id | accounts (1) -> (many) investments |

**Sob koyta relationship-i one-to-many.** Many-to-many kono core entity-r
moddhe nai -- shudhu `practice/ex04_relationships.sql`-e ekta optional
demo ache (`investment_categories` junction table), jodi kono din ekta
investment-ke multiple category-te fela lage.
