from pathlib import Path
import csv

# create a file to csv file
fp = Path.cwd() / "csv_reports" / "Cash_on_Hand.csv"

#create an empty list to store cash on hand record
COHrecords = []
#read the CSV file to append day and cash on hand from the csv
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) #skip header

#append cash on hand record into the COHrecords
    for row in reader:
        COHrecords.append((row[0], float(row[1])))

cohdiffs=[]
#creating an empty list
previouscoh=0

for value in COHrecords:
    day=value[0]
    coh=value[1]
    diff=coh-previouscoh
    cohdiffs.append((day, diff))
    previouscoh=coh

daymostcoh, valuemostcoh = cohdiffs[0]

for day, value in cohdiffs[0:]:
    if value > valuemostcoh:
        daymostcoh, valuemostcoh = day, value

dayleastcoh, valueleastcoh = cohdiffs[0]
for day, value in cohdiffs[0:]:
    if value < valueleastcoh:
        dayleastcoh, valueleastcoh = day, value
valueleastcoh=abs(valueleastcoh)

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
        file.write(f"[HIGHEST CASH SURPLUS] DAY: {daymostcoh}, AMOUNT: {int(valuemostcoh)}\n")
    elif negativevalues == len(cohdiffs):
        file.write("[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN PREVIOUS DAY\n")
        file.write(f"[HIGHEST CASH DEFICIT] DAY: {dayleastcoh}, AMOUNT: {int(valueleastcoh)}\n")
    else:
        for value in cohdiffs:
            day = value[0]
            diff = value[1]
            if diff < 0:
                diff = abs(diff)
                diff = int(diff)
                file.write(f"[CASH DEFICIT] DAY: {day}, AMOUNT: USD{diff}\n")