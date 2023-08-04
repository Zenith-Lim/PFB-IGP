from pathlib import Path
import csv

# create a file path to the file needed.
fp = Path.cwd()/"csv_reports"/"Overheads.csv"
# read the file
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    # creating an empty list to store values later
    overhead_records = []
    # setting the variable total_expense_value to 0 to act as a counter 
    total_expense_value = 0
    # for loop and storing each row as temporary variable called row
    for row in reader: 
        # setting expense_type to the first index item in the temporary variable row 
        expense_type = row[0]
        # converting the second index item in the temporary variable row into a float and then storing it under the variable called expense amount
        # use .replace to remove the "," to be able to convert to float
        expense_amount = float(row[1].replace(",", ""))
        # accumulate expense amounts
        total_expense_value += expense_amount
        # append the expense type and expense amount into previously created overhead_records list
        overhead_records.append([expense_type, expense_amount])

# create function to calculate and write highest overhead
def overheads_function():
    # create empty list to store calculated percentages for overheads
    overhead_percentages=[]
    # for loop to iterate over the overhead_records list
    for expense, value in overhead_records:
        # calculate percentage for individual expenses
        percentage = (value/total_expense_value)*100
        # append calculated percentages with the expense type
        overhead_percentages.append([expense, percentage])
    
    # first assume that the first expense type and percentage is the highest
    expensemost, expensevaluemost = overhead_percentages[0]
    
    # for loop to iterate over overhead_percentages, [0:] to iterate over first to last items in the list
    for expense, value in overhead_percentages[0:]:
        # if the percentage of the certain expense in the overhead_percentages list is higher than the first expense type...
        if value > expensevaluemost:
            # ...change the "expensemost" and "expensevaluemost" variables to store the new highest percentage and expense type associated
            expensemost, expensevaluemost = expense, value

    #create a file path pointing to 'summary_report.txt' file the current working directory, stored as temporary variable 'fp_cwd'
    fp_cwd = Path.cwd()/'summary_report.txt'
    #.touch() creates the new 'summary_report.txt' file in the current working directory file path.
    fp_cwd.touch()
    #with statement with mode='w' to write the calculated info into the summary_report.txt file with UTF-8 character encoding
    #The return value of fp_cwd.open() assigned to the variable name 'file'
    with fp_cwd.open(mode='w', encoding='UTF-8') as file:
        #.write() to write the f-string for highest overhead in the summary_report.txt file
        file.write(f'[HIGHEST OVERHEAD] {expensemost}: {round(expensevaluemost,2)}%\n')