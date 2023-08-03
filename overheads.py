from pathlib import Path
import csv
# create a file path to csv file.
fp = Path.cwd()/"csv_reports"/"Overheads.csv"
# read the csv file
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    # creating an empty list to store certain calculations later
    overhead_records = []
    # setting the variable total_expense_value to 0 to act as a counter 
    total_expense_value = 0
    # for loop and storing each row as temporary variable called row
    for row in reader: 
        # setting expense_type to the first index item in the temporary variable row 
        expense_type = row[0]
        # converting the second index item in the temporary variable row into a float and then storing it under the variable called expense amount
        expense_amount = float(row[1].replace(",", ""))
        total_expense_value += expense_amount
        overhead_records.append([expense_type, expense_amount])

def overheads_function():
    overhead_percentages=[]
    for expense, value in overhead_records: 
        percentage = (value/total_expense_value)*100
        overhead_percentages.append([expense, percentage])
    
    expensemost, expensevaluemost = overhead_percentages[0]
    
    for expense, value in overhead_percentages[0:]:
        if value > expensevaluemost:
            expensemost, expensevaluemost = expense, value

    fp_cwd = Path.cwd()/'summary_report.txt'
    fp_cwd.touch()
    
    with fp_cwd.open(mode='w', encoding='UTF-8') as file:
        file.write(f'[HIGHEST OVERHEAD] {expensemost}: {round(expensevaluemost,2)}%\n')