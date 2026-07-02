# Bank CLI

A simple command-line bank simulator built in Python. Lets you check your balance, deposit money, and withdraw money through a menu-driven interface.

## Features

- **Show Balance** — displays your current balance
- **Deposit** — add funds to your balance
- **Withdraw** — remove funds from your balance (with basic validation)
- **Exit** — quit the program

## How to Run

```bash
python bank.py
```

You'll be shown a menu and prompted to enter a choice from 1–4:

```
Welcome to the bank
1. Show balance
2. Deposit
3. Withdraw
4. Exit
Enter your choice (1-4):
```

## Example Usage

```
Enter your choice (1-4): 2
Enter the amount to deposit: 500
Deposit is:  500

Enter your choice (1-4): 1
Balance is:  500

Enter your choice (1-4): 3
Enter the amount to withdraw: 200
Withdraw is:  300

Enter your choice (1-4): 4
Thank you and have a nice day!
```

## Project Structure

| Function | Description |
|---|---|
| `main()` | Runs the menu loop and routes user input to the right function |
| `show_balance(balance)` | Prints the current balance |
| `deposit(n)` | Adds `n` to the global balance |
| `withdraw(n)` | Subtracts an entered amount from the global balance, with checks for insufficient funds and negative amounts |

## Known Limitations

- Balance is stored in a global variable rather than being passed/returned cleanly between functions
- No input validation for non-numeric entries (will crash on invalid input)
- `withdraw()` takes a parameter `n` but immediately overwrites it with a new `input()` call inside the function

## Possible Next Steps

- Replace the global `balance` variable with a class-based `Account` object
- Add `try/except` blocks around numeric input to handle invalid entries gracefully
- Add unit tests (e.g. with `pytest`) for `deposit`, `withdraw`, and edge cases like negative amounts or overdrafts
- Persist balance to a file so it's saved between runs
