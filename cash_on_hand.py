from pathlib import Path
import csv

fp = Path.cwd() / "csv_reports" / "Cash_on_Hand.csv"

COHrecords = []

with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row

    for row in reader:
        COHrecords.append((row[0], float(row[1])))

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


print("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
print(f"[HIGHEST CASH SURPLUS] DAY: {highest_incre_day},AMOUNT: USD{highest_incre_cash}")

lower_cash_days = []

for items in range(1, len(COHrecords)):
    date, cash = COHrecords[items]
    prev_date, prev_cash = COHrecords[items - 1]

    difference = cash - prev_cash

    if difference < 0:
        lower_cash_days.append((date, cash, difference))
    

for date, cash, difference in lower_cash_days:
    print(f"[CASH DEFICIT] DAY: {date}, AMOUNT: USD{difference*-1}")
    
    
