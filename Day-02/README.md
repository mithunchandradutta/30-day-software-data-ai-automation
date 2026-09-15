# Python Transaction Processor

A simple command-line transaction processor that reads income/expense records from a JSON file and prints a summary — total income, total expense, balance, and category-wise breakdown.

## Project Structure

```
python-transaction-processor/
│
├── main.py             # Entry point
├── transactions.py     # Validation + calculation logic
├── utils.py            # File loading + summary printing
├── data/
│   └── transactions.json
├── README.md
└── .gitignore
```

## Setup

1. Open this folder in VS Code (`File > Open Folder`).
2. Make sure the Python extension is installed (search "Python" in the VS Code Extensions tab and install the official one from Microsoft).
3. Check that Python 3 is installed:
   ```
   python3 --version
   ```
4. Open a terminal (`` Ctrl + ` `` / `` Cmd + ` ``) and navigate to the project folder:
   ```
   cd python-transaction-processor
   ```
5. Run the program:
   ```
   python3 main.py
   ```

## Data Format

Transactions live in `data/transactions.json`. Each entry looks like:

```json
{
    "type": "income",
    "amount": 5000,
    "category": "Salary"
}
```

- `type` — must be `"income"` or `"expense"`
- `amount` — a non-negative number
- `category` — a non-empty string

Invalid entries (missing fields, wrong type, negative amount, etc.) are automatically detected and skipped, and the summary reports how many were skipped.

## Example Output

```
========================
TRANSACTION SUMMARY
========================

Total Income: 5000
Total Expense: 800
Balance: 4200

Category Summary:

Food: 500
Transport: 300

Total Transactions: 3
```

## Extending the Project

- To add transactions, edit `data/transactions.json`.
- To add a new calculation, write a function in `transactions.py` and call it from `main.py`.

## License

Free to use and modify.