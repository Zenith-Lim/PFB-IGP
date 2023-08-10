from pathlib import Path
import csv

#create a file path to the file needed.
fp = Path.cwd()/"csv_reports/Profits_and_Loss.csv"

#read the file
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) #skip header

    #create an empty list to store profit and loss records
    profitandloss=[]

    #append profit and loss data into the profitandloss list 
    for row in reader:
        #get the day, sale, trading profit, operating expense and net profit for each record
        #and append the profitandloss list
        #int() and float() for calculations, int() for day as it's whole number
        profitandloss.append([int(row[0]), float(row[1]), float(row[2]), float(row[3]), float(row[4])])

#create function to find out profit and loss trend (deficit, surplus or both), calculate and write the breakdowns for all 3 situations
def profitloss_function():
    """
    1. Objective:
    - To decipher whether there's a net profit surplus, deficit or both for all business days given
    - To get highest net profit surplus, lowest net profit deficit or all profit deficits for the respective situations
    - To write final statements into a summary text file

    2. Parameters:
    - No parameters needed
    """
    #create empty list to store calculated differences of net profits
    alldiff=[]
    #setting the variable previousnetprofit to 0 to store previous day net profits
    previousnetprofit=0
    #for loop to iterate over alldiff
    for value in profitandloss:
        #setting the individual days in the profitandloss list to temporary variable day
        day=value[0]
        #setting the individual net profits in the profitandloss list to temporary variable netprofit
        netprofit=value[4]
        #calculate the difference between current day net profit and previous day's
        diff=netprofit-previousnetprofit
        #append the day and calculated difference into previously created alldiff list
        alldiff.append((day, diff))
        #set previousnetprofit to current net profit for calculation for next day
        previousnetprofit=netprofit
    
    #first assume that the first day and net profit difference is the highest
    daymost, valuemost = alldiff[0]
    
    #for loop to iterate over alldiff, [0:] to iterate over first to last items in the list
    for day, value in alldiff[0:]:
        #if the net profit difference of the certain day in the alldiff list is higher than the first day...
        if value > valuemost:
            #...change the "daymost" and "valuemost" variables to store the new highest net profit difference and day associated
            daymost, valuemost = day, value
    
    #first assume that the first day and net profit difference is the lowest
    dayleast, valueleast = alldiff[0]
    #for loop to iterate over alldiff, [0:] to iterate over first to last items in the list
    for day, value in alldiff[0:]:
        #if the net profit difference of the certain day in the alldiff list is lower than the first day...
        if value < valueleast:
            #...change the "dayleast" and "valueleast" variables to store the new lowest net profit difference and day associated
            dayleast, valueleast = day, value
    #abs() to remove "-" from the final lowest difference for final written statement
    valueleast=abs(valueleast)
    
    #setting the variable positivevalues to 0 to act as a counter
    positivevalues=0
    #setting the variable negativevalues to 0 to act as a counter
    negativevalues=0
    
    #for loop to iterate over the alldiff list
    for day, value in alldiff:
        #if the value is positive...
        if value >= 0:
            #...add 1 into the positivevalues counter
            positivevalues += 1
        #otherwise (if the value is negative)...
        else:
            #...add 1 into the negativevalues counter
            negativevalues += 1
    
    #create a file path pointing to 'summary_report.txt' file in the current working directory, stored as temporary variable 'fp_cwd'
    fp_cwd = Path.cwd()/'summary_report.txt'
    #with statement with mode='a' to append the calculated info into the summary_report.txt file with UTF-8 character encoding
    #The return value of fp_cwd.open() assigned to the variable name 'file'
    with fp_cwd.open(mode='a', encoding='UTF-8') as file:
        #if all values in alldiff are positive
        if positivevalues == len(alldiff):
            #.write() to write the following lines into the summary_report.txt file
            #f-string for highest net profit surplus in the summary_report.txt file
            file.write("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY\n")
            file.write(f"[HIGHEST NET PROFIT SURPLUS] DAY: {daymost}, AMOUNT: {int(valuemost)}\n")
        #however, if all values in cohdiffs are negative
        elif negativevalues == len(alldiff):
            #.write() to write the following lines into the summary_report.txt file
            #f-string for highest net profit deficit in the summary_report.txt file
            file.write("[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN PREVIOUS DAY\n")
            file.write(f"[HIGHEST NET PROFIT DEFICIT] DAY: {dayleast}, AMOUNT: {int(valueleast)}\n")
        #otherwise (if the values in alldiff are mixed)
        else:
            #for loop to iterate over alldiff
            for value in alldiff:
                #setting the individual days in the alldiff list to temporary variable day
                day = value[0]
                #setting the individual net profit differences in the alldiff list to temporary variable diff
                diff = value[1]
                #if the net profit difference is negative
                if diff < 0:
                    #abs to remove "-" for final statement
                    diff = abs(diff)
                    #int to remove decimals
                    diff = int(diff)
                    #.write() to write the f-string for all profit deficits in the summary_report.txt file
                    file.write(f"[PROFIT DEFICIT] DAY: {day}, AMOUNT: USD{diff}\n")
    #close the file after writing
    file.close()