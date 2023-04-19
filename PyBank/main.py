import os
import csv


#Open and read budget data file
#budgetdata_csv = os.path.join( "Resources", "budget_data.csv")
budgetdata_csv = os.path.join("C://Users/gpanc/OneDrive/Documents/python-challenge/PyBank/Resources/budget_data.csv")

#Works cited: https://codecaliper.me/counting-the-number-of-rows-in-a-csv-file-with-python

with open(budgetdata_csv,"r") as csv_reader:
    line = next(csv_reader)
    csv_reader = csv.reader(csv_reader)
    row_count = 0
    total_pnl = 0
    line = next(csv_reader)
    previous_pnl = int(line[1])
    all_pnl_differences = []
    greatest_pnl_inc = 0
    greatest_inc_date = 0
    greatest_pnl_dec = 0
    greatest_dec_date = 0
    

    for row in csv_reader:
        row_count += 1
        total_pnl += int(row[1])
        date = str(row[0])
        pnl = int(row[1])  
        pnl_difference = pnl - previous_pnl
        if greatest_pnl_inc < pnl_difference:
            greatest_pnl_inc = pnl_difference 
            greatest_inc_date = date
        elif greatest_pnl_dec > pnl_difference:
            greatest_pnl_dec = pnl_difference
            greatest_dec_date = date
        all_pnl_differences.append(pnl_difference)
        previous_pnl = pnl

    

print()
print("Financial Analysis")
print()
print("---------------------------------------")
print()
print("Total Months: ", row_count)  
print()
print("Total: " "${:,.2f}".format(total_pnl)) 
print()
print("Average Change: ", "${:,.2f}".format(round(sum(all_pnl_differences)/len(all_pnl_differences),2)))
print()
print("Greatest Increase in Profits: ", greatest_inc_date, "${:,.2f}".format(greatest_pnl_inc))
print()
print("Greatest Decrease in Profits: ", greatest_dec_date, "${:,.2f}".format(greatest_pnl_dec))
print()


txt_file = open("results_file.txt", "w")
txt_file.write("Financial Analysis\n")
txt_file.write("---------------------------------------\n")
txt_file.write("Total Months: "+ str(row_count)+"\n")  
total_pnl = "Total: " "${:,.2f}".format(total_pnl) + "\n"
txt_file.write(total_pnl) 
avg_change = "Average Change: "+ "${:,.2f}".format(round(sum(all_pnl_differences)/len(all_pnl_differences),2))
greatest_inc = "Greatest Increase in Profits: "+ greatest_inc_date+ " ${:,.2f}".format(greatest_pnl_inc)
greatest_dec = "Greatest Decrease in Profits: "+ greatest_dec_date+ " ${:,.2f}".format(greatest_pnl_dec)
txt_file.write(avg_change+ "\n")
txt_file.write(greatest_inc+ "\n")
txt_file.write(greatest_dec+ "\n")
txt_file.close()
    


    

