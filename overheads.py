from pathlib import Path
import csv
fp = Path.cwd()/"csv_reports"/"Overheads.csv"
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    overhead_records = []
    total_expense_value = 0
    for row in reader: 
        expense_type = row[0]
        expense_amount = float(row[1].replace(",", ""))
        total_expense_value += expense_amount
        overhead_records.append([expense_type, expense_amount])

overhead_percentages=[]
for expense, value in overhead_records: 
    percentage = (value/total_expense_value)*100
    overhead_percentages.append([expense, percentage])

expensemost, valuemost = overhead_percentages[0]

for expense, value in overhead_percentages[0:]:
    if value > valuemost:
        expensemost, valuemost = expense, value

fp_cwd = Path.cwd()/'summary_report.txt'
fp_cwd.touch()

with fp_cwd.open(mode='w', encoding='UTF-8') as file:
    file.write(f'[HIGHEST OVERHEAD] {expensemost}: {round(valuemost,2)}%')


