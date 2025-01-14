#This is for PyBank
#Import modules
import csv

#Join dataset file (assumes file is in Resources subfolder)
budget_data = ("budget_data.csv")

#Create variables to process results
months = 0
net_income = 0
last_month = 0
first_month = True
monthly_change = 0
total_change = 0
greatest_increase = 0
greatest_decrease = 0

#Access dataset
with open(budget_data, newline="") as budget_data_file:
    budget_data_reader = csv.reader(budget_data_file, delimiter=",")
    #Skip header row
    header = next(budget_data_file)

    #Read through each remaining row
    for row in budget_data_reader:

        #Update months
        months += 1 

        #Update net_income 
        net_income += int(row[1])

        #Update monthly_change if not the first month (nothing to compare it to)
        if first_month is False:
            monthly_change = int(row[1]) - last_month
            
        #Update last_month 
        last_month = int(row[1])

        #Tracking for avg_change
        total_change += monthly_change

        #After first pass through, no longer the first month
        first_month = False

        #Check greatest values
        if monthly_change > greatest_increase:
            greatest_increase = monthly_change
            greatest_increase_date = (row[0])

        if monthly_change < greatest_decrease:
            greatest_decrease = monthly_change
            greatest_decrease_date = (row[0])

#Calculate average change adjusting for first month when there was no comparison to make
avg_change = total_change/(months-1)
  
#Print the results to the terminal
print ("\nFinancial Analysis")
print ("----------------------------")
print (f"Total Months: {months}")
print (f"Total: ${net_income}")
print ("Average Change: $" + str(round(avg_change,2)))
print (f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print (f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

#Export a text file with the results
f = open("PyBank_analysis.text", "w+")
f.write("Financial Analysis\n") 
f.write ("----------------------------\n")
f.write ("Total Months: " + str(months) + "\n")
f.write ("Total: $" + str(net_income)+ "\n")
f.write ("Average Change: $" + str(round(avg_change,2))+ "\n")
f.write ("Greatest Increase in Profits: " + greatest_increase_date + " ($" + str(greatest_increase) + ")\n")
f.write ("Greatest Decrease in Profits: " + greatest_decrease_date + " ($" + str(greatest_decrease) + ")\n")

