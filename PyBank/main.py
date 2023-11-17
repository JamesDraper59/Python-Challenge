#analyze bank budget data 

#import csv module
import csv

#create storage locations for data with lists and variables
profit = []

monthly_difference = []

date = []

total_months = 0

starting_profit = 0

total_profit = 0

profit_change = 0


#set working directory using a raw string
budget_data = r'C:\Users\James\Python-Challenge\PyBank\Resources\budget_data.csv'

#open and read through csv file
with open(budget_data, 'r') as csvfile:
    
    reader = csv.reader(csvfile, delimiter=',')
    
    header = next(reader)

    #begin looping through budget data with a loop for every row in the file
    for row in reader:
        
        #count and total the number of months in the budget data 
        total_months = total_months + 1

        #calculate current profit total 
        total_profit = total_profit + int(row[1])

        #find the change in profit between the months
        final_profit = int(row[1])
        
        monthly_profit = final_profit - starting_profit

        #append data to lists
        date.append(row[0])
        
        profit.append(row[1])
        
        monthly_difference.append(monthly_profit)

        #reset the starting profit for the next month and calculate the total change of profit 
        starting_profit = final_profit
        
        profit_change = profit_change + monthly_profit

        #obtain the max, min, and mean of the monthly differences
        max_increase = max(monthly_difference)
        
        min_increase = min(monthly_difference)
        
        mean_increase = sum(monthly_difference) / len(monthly_difference)
        
        #cut off at the 2nd decimal place for neatness
        
        mean_increase = round(mean_increase, 2)

        #Store dates for greatest increase and decrease 
        greatest_inc_date = date[monthly_difference.index(max_increase)]
        
        greatest_dec_date = date[monthly_difference.index(min_increase)]

        #print statistical analysis to terminal 

        print("Financial Analysis" + "\n")
        
        print("----------------------------" + "\n")
        
        print("Total Months: " + str(total_months) + "\n")
        
        print("Total :" + str(total_profit) + "\n")

        print("Average Change: " + str(mean_increase) + "\n")
        
        print("Greatest Increase in Profits: " + str(greatest_inc_date) + " ($" + str(max_increase) + ")" + "\n")
        
        print("Greatest Decrease in Profits: " + str(greatest_dec_date) + " ($" + str(min_increase)+ ")" + "\n")
        
        print("----------------------------")

        
       
        #write analysis out to a new txt file created by script
        with open('Budget_Analysis.txt', 'w') as text:
        
            text.write("----------------------------" + "\n")
        
            text.write("  Financial Analysis"+ "\n")
        
            text.write("----------------------------" + "\n")
        
            text.write("Total Months: " + str(total_months) + "\n")
        
            text.write("Total Profits: " + "$" + str(total_profit) +"\n")
        
            text.write("Average Change: " + '$' + str(int(mean_increase)) + "\n")
        
            text.write("Greatest Increase in Profits: " + str(greatest_inc_date) + " ($" + str(max_increase) + ")\n")
        
            text.write("Greatest Decrease in Profits: " + str(greatest_dec_date) + " ($" + str(min_increase) + ")\n")
        
            text.write("----------------------------" + "\n")











    


    
