#python challenge solution 1- PyBank

import os
import csv


# Define the path to the CSV file & text file
budget_csv = os.path.join("Resources", "budget_data.csv")
analysis_txt = os.path.join("Analysis", "budget_analysis.txt")

# Initialize finacial variables
total_months = 0
net_profit_losses = 0
previous_profit_loss = 0
profit_changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Read the CSV file & convert it to a list of dictionaries
with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    header = next(csv_reader)

    # Iterate over each row & track the totals
    for row in csv_reader:
   
        total_months += 1
        net_profit_losses += int(row[1])

        # Calculate change in profit/losses
        current_profit_loss = int(row[1])
        if previous_profit_loss != 0:
            profit_change = current_profit_loss - previous_profit_loss
            profit_changes.append(profit_change)

            # Calculate the greatest increase and greatest decrease
            if profit_change > greatest_increase[1]:
                greatest_increase = [row[0], profit_change]
            if profit_change < greatest_decrease[1]:
                greatest_decrease = [row[0], profit_change]

        # Calculate previous profit loss 
        previous_profit_loss = current_profit_loss

# Calculate the average change
average_monthly = sum(profit_changes) / len(profit_changes)

# Generate output
Output = (f"Financial Analysis\n"
          f"-----------------------------------\n"
          f"Total Months: {total_months}\n"
          f"Total: ${net_profit_losses}\n"
          f"Average Change: ${average_monthly:.2f}\n"
          f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
          f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")


# Print the analysis results
print(Output)


# Export the output as text file
with open(analysis_txt, "w") as text_file:
    text_file.write(Output)
