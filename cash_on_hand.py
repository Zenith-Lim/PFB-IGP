from pathlib import Path
import csv

fp = Path.cwd() / "csv_reports" / "Cash_on_Hand.csv"

COHrecords = []

with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row

    for row in reader:
        COHrecords.append((row[0], int(row[1])))

COHDiff = {}
prev_cash = 0

for day, cash in COHrecords:
    if prev_cash != 0:
        COHDiff[day] = cash - prev_cash
    prev_cash = cash

highest_incre_day = 0
highest_incre_cash = 0

for day, difference in COHDiff.items():
    if difference > highest_incre_cash:
        highest_incre_day = day
        highest_incre_cash = difference


print("Day and Amount with the Highest Increment:")
print("Day:", highest_incre_day)
print("Amount:", highest_incre_cash)

lower_cash_days = []

for i in range(1, len(COHrecords)):
    date, cash = COHrecords[i]
    prev_date, prev_cash = COHrecords[i - 1]

    difference = cash - prev_cash

    if difference < 0:
        lower_cash_days.append((date, cash, difference))

print("Days where the Current Day is Lower than the Previous Day:")
for date, cash, difference in lower_cash_days:
    print(f"Date: {date}, Cash on Hand: {cash}, diff: {difference}")

