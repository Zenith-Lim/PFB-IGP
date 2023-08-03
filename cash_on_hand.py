from pathlib import Path
import csv

fp = Path.cwd() / "csv_reports" / "Cash_on_Hand.csv"

COHrecords = []

with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        COHrecords.append((row[0], float(row[1])))

cohdiffs=[]

previouscoh=0

for value in COHrecords:
    day=value[0]
    coh=value[1]
    diff=coh-previouscoh
    cohdiffs.append((day, diff))
    previouscoh=coh

daymost, valuemost = cohdiffs[0]

for day, value in cohdiffs[0:]:
    if value > valuemost:
        daymost, valuemost = day, value

dayleast, valueleast = cohdiffs[0]
for day, value in cohdiffs[0:]:
    if value < valueleast:
        dayleast, valueleast = day, value
valueleast=abs(valueleast)

positivevalues=0
negativevalues=0

for day, value in cohdiffs:
    if value >= 0:
        positivevalues += 1
    else:
        negativevalues += 1

fp_cwd = Path.cwd()/'summary_report.txt'
fp_cwd.touch()

with fp_cwd.open(mode='w', encoding='UTF-8') as file:
    if positivevalues == len(cohdiffs):
        file.write("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN PREVIOUS DAY\n")
        file.write(f"[HIGHEST CASH SURPLUS] DAY: {daymost}, AMOUNT: {int(valuemost)}\n")
    elif negativevalues == len(cohdiffs):
        file.write("[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN PREVIOUS DAY\n")
        file.write(f"[HIGHEST CASH DEFICIT] DAY: {dayleast}, AMOUNT: {int(valueleast)}\n")
    else:
        file.write("[CASH MIXED] CASH ON DAYS ARE HIGHER OR LOWER THAN PREVIOUS DAY\n")
        file.write(f"[HIGHEST CASH SURPLUS] DAY: {daymost}, AMOUNT: {int(valuemost)}\n")
        file.write(f"[HIGHEST CASH DEFICIT] DAY: {dayleast}, AMOUNT: {int(valueleast)}\n")

    for value in cohdiffs:
        day = value[0]
        diff = value[1]
        if diff < 0:
            diff = abs(diff)
            diff = int(diff)
            file.write(f"[CASH DEFICIT] DAY: {day}, AMOUNT: USD{diff}\n")