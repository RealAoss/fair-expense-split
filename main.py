import argparse
import re

def money(cents):
    return f"{cents // 100}.{cents % 100:02}"

parser = argparse.ArgumentParser(description="Settle equal shares in one currency")
parser.add_argument("payments", nargs="+", metavar="NAME=AMOUNT")
args = parser.parse_args()
paid = {}
for entry in args.payments:
    name, separator, amount = entry.rpartition("=")
    name = name.strip()
    if not name or name in paid or not re.fullmatch(r"[0-9]+(?:\.[0-9]{1,2})?", amount):
        parser.error(f"Expected a unique NAME and nonnegative amount: {entry}")
    whole, _, fraction = amount.partition(".")
    paid[name] = int(whole) * 100 + int(fraction.ljust(2, "0"))
share, extra = divmod(sum(paid.values()), len(paid))
creditors, debtors = [], []
for index, (name, payment) in enumerate(paid.items()):
    due = share + int(index < extra)
    print(f"{name}: share {money(due)}")
    balance = payment - due
    if balance > 0:
        creditors.append([name, balance])
    elif balance < 0:
        debtors.append([name, -balance])
index = 0
for debtor, remaining in debtors:
    while remaining:
        creditor, credit = creditors[index]
        transfer = min(credit, remaining)
        print(f"{debtor} -> {creditor}: {money(transfer)}")
        remaining -= transfer
        creditors[index][1] -= transfer
        if not creditors[index][1]:
            index += 1
