# Fair Expense Split

Settle a shared expense with equal shares, using exact integer cents.

## Run

From this folder with Python 3.9 or later:

```sh
python main.py GuestA=90 GuestB=15 GuestC=0
```

Each participant owes 35.00. GuestB transfers 20.00 to GuestA and GuestC transfers 35.00 to GuestA. Enter every participant once in one two-decimal currency. Input order determines who bears a leftover cent.

## Limitations

Shares are equal and all payments must use the same two-decimal currency.

## Development

See [CONTRIBUTING.md](CONTRIBUTING.md) for setup and test commands, and the [changelog](CHANGELOG.md) for project history.

## License

[MIT License](LICENSE). Copyright (c) 2026 fair-expense-split contributors.
