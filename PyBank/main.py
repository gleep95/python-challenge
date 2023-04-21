import os
import csv


#Open and read budget data file
budgetdata_csv = os.path.join("Resources", "budget_data.csv")

#Works cited: https://codecaliper.me/counting-the-number-of-rows-in-a-csv-file-with-python
#Open budget data, skip header and set variables/counters/empty listlists
with open(budgetdata_csv,"r") as csv_reader:
    line = next(csv_reader)
    csv_reader = csv.reader(csv_reader)
    row_count = 1
    total_pnl = 0
    line = next(csv_reader)
    line1 = int(line[1])
    previous_pnl = int(line[1])
    all_pnl_differences = []
    greatest_pnl_inc = 0
    greatest_inc_date = 0
    greatest_pnl_dec = 0
    greatest_dec_date = 0
    
    #Loop over every row in data file and count the total months, and sum of profit/loss column, as well as average change
    #Works Cited: https://codecaliper.me/counting-the-number-of-rows-in-a-csv-file-with-python
    #Works Cited: https://stackoverflow.com/questions/13517080/sum-a-csv-column-in-python
    for row in csv_reader:
        row_count += 1
        total_pnl += int(row[1])
        date = str(row[0])
        pnl = int(row[1])  
        pnl_difference = pnl - previous_pnl
        #Get the greatest increase in profits and date
        if greatest_pnl_inc < pnl_difference:
            greatest_pnl_inc = pnl_difference 
            greatest_inc_date = date
        #Get the greatest decrease in profits and date
        elif greatest_pnl_dec > pnl_difference:
            greatest_pnl_dec = pnl_difference
            greatest_dec_date = date
        all_pnl_differences.append(pnl_difference)
        previous_pnl = pnl

    
#Print out the results of months, sum of P/L column, total average change, greatest inc in profits with date, greatest dec in profits with date
#Works Cited: https://www.adamsmith.haus/python/answers/how-to-format-currency-in-python
print()
print("Financial Analysis")
print()
print("---------------------------------------")
print()
print("Total Months: ", row_count)  
print()
print("Total: " "${:,.2f}".format(total_pnl + line1)) 
print()
print("Average Change: ", "${:,.2f}".format(round(sum(all_pnl_differences)/len(all_pnl_differences),2)))
print()
print("Greatest Increase in Profits: ", greatest_inc_date, "${:,.2f}".format(greatest_pnl_inc))
print()
print("Greatest Decrease in Profits: ", greatest_dec_date, "${:,.2f}".format(greatest_pnl_dec))
print()

#Write out the results of months, sum of P/L column, total average change, greatest inc in profits with date, greatest dec in profits with date to results text file
#Works Cited: https://www.adamsmith.haus/python/answers/how-to-format-currency-in-python
txt_file = open("analysis/results_file.txt", "w")
txt_file.write("Financial Analysis\n")
txt_file.write("---------------------------------------\n")
txt_file.write("Total Months: "+ str(row_count)+"\n")  
total_pnl = "Total: " "${:,.2f}".format(total_pnl+line1) + "\n"
txt_file.write(total_pnl) 
avg_change = "Average Change: "+ "${:,.2f}".format(round(sum(all_pnl_differences)/len(all_pnl_differences),2))
greatest_inc = "Greatest Increase in Profits: "+ greatest_inc_date+ " ${:,.2f}".format(greatest_pnl_inc)
greatest_dec = "Greatest Decrease in Profits: "+ greatest_dec_date+ " ${:,.2f}".format(greatest_pnl_dec)
txt_file.write(avg_change+ "\n")
txt_file.write(greatest_inc+ "\n")
txt_file.write(greatest_dec+ "\n")
txt_file.close()
    


    

