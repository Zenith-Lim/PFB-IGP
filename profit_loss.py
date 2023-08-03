from pathlib import Path
import csv

fp = Path.cwd()/"csv_reports/profit_and_loss.csv"

with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    profitandloss=[] 

    for row in reader:
        profitandloss.append([int(row[0]), float(row[1]), float(row[2]), float(row[3]), float(row[4])])

alldiff=[]

previousnetprofit=0

for value in profitandloss:
    day=value[0]
    netprofit=value[4]
    diff=netprofit-previousnetprofit
    alldiff.append((day, diff))
    previousnetprofit=netprofit

daymost, valuemost = alldiff[0]

for day, value in alldiff[0:]:
    if value > valuemost:
        daymost, valuemost = day, value

dayleast, valueleast = alldiff[0]
for day, value in alldiff[0:]:
    if value < valueleast:
        dayleast, valueleast = day, value
valueleast=abs(valueleast)

positivevalues=0
negativevalues=0

for day, value in alldiff:
    if value >= 0:
        positivevalues += 1
    else:
        negativevalues += 1

fp_cwd = Path.cwd()/'summary_report.txt'
fp_cwd.touch()

with fp_cwd.open(mode='w', encoding='UTF-8') as file:
    if positivevalues == len(alldiff):
        file.write("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY\n")
        file.write(f"[HIGHEST NET PROFIT SURPLUS] DAY: {daymost}, AMOUNT: {int(valuemost)}\n")
    elif negativevalues == len(alldiff):
        file.write("[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN PREVIOUS DAY\n")
        file.write(f"[HIGHEST NET PROFIT DEFICIT] DAY: {dayleast}, AMOUNT: {int(valueleast)}\n")
    else:
        for value in alldiff:
            day = value[0]
            diff = value[1]
            if diff < 0:
                diff = abs(diff)
                diff = int(diff)
                file.write(f"[PROFIT DEFICIT] DAY: {day}, AMOUNT: USD{diff}\n")