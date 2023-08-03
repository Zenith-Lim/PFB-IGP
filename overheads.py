from pathlib import Path
import csv
fp = Path.cwd()/"csv_reports"/"Overheads.csv"
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    overhead_records = []
    total_expense_value = 0
    for row in reader: 
        expense_type = row[0]
        expense_amount = int(row[1].replace(",", ""))
        total_expense_value += expense_amount 
        overhead_records.append([expense_type, expense_amount])
print(overhead_records)
print(total_expense_value)
#for type in overhead_records: 
    #percentage = (int(type[1]) / int(total_expense_value))
    #percentage = percentage * 100
    #overhead_records.append(percentage)


# value = 0
# for expense in overhead_records: 
    # expense = overhead_records[0]
    # number = overhead_records[1]
    # if number > value:
        # value = number  


