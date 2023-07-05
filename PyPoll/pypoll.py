#python challenge solution 2- PyPoll

import os
import csv


# Define the path to the CSV file & text file
election_csv = os.path.join("Resources", "election_data.csv")
analysis_txt = os.path.join("Analysis", "election_analysis.txt")

# Initialize election variables
total_votes = 0
candidates = {}
winner = ""

# Read the CSV file & convert it to a list of dictionaries
with open(election_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    header = next(csv_reader)


  # Iterate over each row & track the total votes
    for row in csv_reader:
   
        total_votes += 1
        
        # Retrieve the candiate's name 
        candidate_name = row[2]

        # Calculate the candidate's vote count using if else function
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

# Determine the winner and winning vote count 
winning_votes = 0
for candidate_name, votes in candidates.items():
    if votes > winning_votes:
        winning_votes = votes
        winner_candidate = candidate_name

# Retrieve the percenatge of votes 
vote_percentages = {}
for candidate_name, votes in candidates.items():
    percentage = (votes/total_votes) *100
    vote_percentages[candidate_name] = percentage


# output results 
output = (
    "Election Results\n"
    "-----------------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-----------------------------------\n"
    )

for candidate_name, votes in candidates.items():
    percentage = vote_percentages[candidate_name]
    output += f"{candidate_name}:{percentage:.3f}% ({votes})\n"
    
    
    output += (
        "------------------------------\n"
        f"Winner = {winner_candidate}\n"
        "-------------------------------\n"
        )
    

# Print the analysis results 
print (output)


# Export the output as text file
with open(analysis_txt, "w") as text_file:
    text_file.write(output)

