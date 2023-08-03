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

print(f"Difference in Cash-on-Hand: {COHDiff}")
print("Day and Amount with the Highest Increment:")
print("Day:", highest_incre_day)
print("Amount:", highest_incre_cash)