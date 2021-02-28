import os
import csv

#set the variables
months = []
profit_loss_amount = []

#set starting values
month_total = 0
profit_total = 0
profit change = 0
monthly_change = 0

#Path to collect data from resources folder
budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')

#Open the CSV
with open(budget_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

    #print{f"Header: {csv_header}")

    for row in csv_reader:
       date.append(row[0])
        money.append(int(row[1]))
        sum_total += float(row[1])
        #print(row)

total months
month_total = len(months)

increase = profit_loss_amount[0]
decrease = profit_loss_amount[0]

for i in range(len(profit_loss_amount)):
    if profit_loss_amount[i] >= increase:
        increase = profit_loss_amount[i]
        month_increase = months[i]
    elif profit_loss_amount[i] <= decrease:
        decrease = profit_loss_amount[i]
        month_decrease = months[i]
    else:
        pringt("Error")

avg_profit = round(sum_total/months, 2)

with open('output_financial.txt',"w",newline = '') as textfile:
    print("Financial Analysis", file = textfile)
    print("-----------------------------------", file = textfile)
    print(f'Total Months: {months}', file = textfile)
    print(f'Total Revenue: ${sum_total}',file = textfile)
    print(f'Average Profit/Loss Change: ${avg_money}',file = textfile)
    print(f'Greatest Increase Profit/Loss: {increase_month}(${increase})',file = textfile)
    print(f'Greatest Decrease Profit/Loss: {decrease_month}(${decrease})',file = textfile)
    print("-----------------------------------", file = textfile) 

with open('output_financial.txt', newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    for row in csvreader:
        print(row)