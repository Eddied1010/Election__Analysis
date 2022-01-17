# 1. The data we need to retrieve.
# 2. The Total number of votes Casted.
# 3. A complete list of candidates who received votes.
# 4. The percentage of votes each candidates won
# 5. The total number of votes each candidate won
# 6. The winner of the election based on popular vote. 


# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

import csv
dir(csv)
import os

file_to_load = 'Resources/election_results.csv'

election_data = open(file_to_load, 'r', encoding='UTF-8')
election_data.close()

print(election_data)

file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize a total vote counter.election_data
total_votes = 0

candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    header = next(file_reader)
#    print(header)

# Print each row in the CSV file.
    for row in file_reader:
#      print(row)
        total_votes += 1

        candidate_name = row[2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0
               
        candidate_votes[candidate_name] +=1

        
# print(candidate_options)   
print(candidate_votes)
print(total_votes)

#vote_percentage = (votes / total_votes)*100

# Use the open statement to open the file as a text file.


#Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
 #   print(f"{candidate_name}: received {vote_percentage}% of the vote.")

    # Determine winning vote count and candidate
    # 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. If true then set winning_count = votes and winning_percent =
        # vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # 3. Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name

# To do: print out each candidate's name, vote count, and percentage of
# votes to the terminal.
print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)