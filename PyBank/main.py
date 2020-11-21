import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')
print(csvpath)
csvpath_out = os.path.join('Resources', 'budget_data.txt')
print(csvpath_out)

with open(csvpath, newline= '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    csv_header = next(csvreader, None)
    print(csv_header)

    change = 0
    total_months = 0
    total_profitandLoss= 0
    avg_chg = 0
    increase_profit = 0
    decrease_profit = 0

#total months count loop 
    for row in csvreader:
        total_months += 1
        total_profitandLoss += int(row[1])
        print(total_months)
        
        if int(row[1]) - avg_chg > increase_profit:
            increase_profit = int(row[1]) - avg_chg
            increase_month = row[0]
        elif int(row[1]) - avg_chg < decrease_profit:
            decrease_profit = int(row[1]) - avg_chg
            decrease_month = row[0]
            change += int(row[1])

        avg_chg = int(row[1])

# financial analysis, add a newline after each text 
with open(csvpath_out, 'w', newline= '') as txtfile:

    txtfile.write('Financial Analysis\n')
    txtfile.write('----------------------------\n')
    txtfile.write('Total Months: '+str(total_months)+ '\n')
    txtfile.write('Total: $'+str(total_profitandLoss)+ '\n' )
    txtfile.write('Average Change: '+str(round((change/(total_months-1)),2))+ '\n')
    txtfile.write('Greatest Increase in Profit: '+increase_month+' ($'+str(increase_profit) + ')\n')
    txtfile.write('Greatest Decrease in Profits:'+increase_month+' ($'+str(decrease_month) + ')\n')
    
    
with open(csvpath_out, newline= '') as f:
    for line in f:
        print(line, end = '')

    





