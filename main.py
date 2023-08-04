from overheads import overheads_function
from cash_on_hand import coh_function
from profit_loss import profitloss_function

#create function to invoke all 3 functions (overheads, cash on hand, profit and loss)
def main():
    #to invoke all 3 functions imported from the original files
    overheads_function()
    coh_function()
    profitloss_function()
#invoke the function
main()