from pathlib import Path
import csv

#create a file path to the file needed.
fp = Path.cwd() / "csv_reports" / "Cash_on_Hand.csv"

#create an empty list to store cash on hand records
COHrecords = []
#read the file
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) #skip header

    #append cash on hand record into the COHrecords
    for row in reader:
        #get the day and cash on hand for each record and append the COHrecords list
        #float() for calculations
        COHrecords.append((row[0], float(row[1])))

#create function to find out cash on hand trend (deficit, surplus or both), calculate and write the breakdowns for all 3 situations
def coh_function():
    """
    1. Objective:
    - To decipher whether there's a cash surplus, deficit or both for all business days given
    - To get highest cash surplus, lowest cash deficit or all cash deficits for the respective situations
    - To write final statements into a summary text file

    2. Parameters:
    - No parameters needed
    """
    #create empty list to store calculated differences of cash on hands
    cohdiffs=[]
    #setting the variable previouscoh to 0 to store previous day cash on hands 
    previouscoh=0
    #for loop to iterate over COHrecords
    for value in COHrecords:
        #setting the individual days in the COHrecords list to temporary variable day
        day=value[0]
        #setting the individual cash on hands in the COHrecords list to temporary variable coh
        coh=value[1]
        #calculate the difference between current day cash on hand and previous day's
        diff=coh-previouscoh
        #append the day and calculated difference into previously created cohdiffs list
        cohdiffs.append((day, diff))
        #set previouscoh to current cash on hand for calculation for next day
        previouscoh=coh
    
    #first assume that the first day and cash on hand difference is the highest
    daymostcoh, valuemostcoh = cohdiffs[0]
    #for loop to iterate over cohdiffs, [0:] to iterate over first to last items in the list
    for day, value in cohdiffs[0:]:
        #if the cash on hand difference of the certain day in the cohdiffs list is higher than the first day...
        if value > valuemostcoh:
            #...change the "daymostcoh" and "valuemostcoh" variables to store the new highest cash on hand difference and day associated
            daymostcoh, valuemostcoh = day, value
    
    #first assume that the first day and cash on hand difference is the lowest
    dayleastcoh, valueleastcoh = cohdiffs[0]
    #for loop to iterate over cohdiffs, [0:] to iterate over first to last items in the list
    for day, value in cohdiffs[0:]:
        #if the cash on hand difference of the certain day in the cohdiffs list is lower than the first day...
        if value < valueleastcoh:
            #...change the "dayleastcoh" and "valueleastcoh" variables to store the new lowest cash on hand difference and day associated
            dayleastcoh, valueleastcoh = day, value
    #abs() to remove "-" from the final lowest difference for final written statement
    valueleastcoh=abs(valueleastcoh)
    
    #setting the variable positivevalues to 0 to act as a counter
    positivevalues=0
    #setting the variable negativevalues to 0 to act as a counter
    negativevalues=0
    
    #for loop to iterate over the cohdiffs list
    for day, value in cohdiffs:
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
        #if all values in cohdiffs are positive
        if positivevalues == len(cohdiffs):
            #.write() to write the following lines into the summary_report.txt file
            #f-string for highest cash surplus in the summary_report.txt file
            file.write("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN PREVIOUS DAY\n")
            file.write(f"[HIGHEST CASH SURPLUS] DAY: {daymostcoh}, AMOUNT: {int(valuemostcoh)}\n")
        #however, if all values in cohdiffs are negative
        elif negativevalues == len(cohdiffs):
            #.write() to write the following lines into the summary_report.txt file
            #f-string for highest cash deficit in the summary_report.txt file
            file.write("[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN PREVIOUS DAY\n")
            file.write(f"[HIGHEST CASH DEFICIT] DAY: {dayleastcoh}, AMOUNT: {int(valueleastcoh)}\n")
        #otherwise (if the values in cohdiffs are mixed)
        else:
            #for loop to iterate over cohdiffs
            for value in cohdiffs:
                #setting the individual days in the cohdiffs list to temporary variable daycoh
                daycoh = value[0]
                #setting the individual cash on hand differences in the cohdiffs list to temporary variable diffcoh
                diffcoh = value[1]
                #if the cash on hand difference is negative
                if diffcoh < 0:
                    #abs to remove "-" for final statement
                    diffcoh = abs(diffcoh)
                    #int to remove decimals
                    diffcoh = int(diffcoh)
                    #.write() to write the f-string for all cash deficits in the summary_report.txt file
                    file.write(f"[CASH DEFICIT] DAY: {daycoh}, AMOUNT: USD{diffcoh}\n")