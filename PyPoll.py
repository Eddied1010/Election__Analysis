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

# Open the election results and read the file.
with open(file_to_load) as election_data:

# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    header = next(file_reader)
    print(header)

# Print each row in the CSV file.
#   for row in file_reader:
 #       print(row)


# Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")

outfile.write("Arapahoe")
outfile.write("Denver")
outfile.write("Jefferson")

outfile.write("\nUSA\nCAN\nMEX\nEUR")

# Close the file
outfile.close()
# Assign a variable for the file to load and the path.







#file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
#with open(file_to_load) as election_data:
    
# Print the file object.
#    print(election_data)


#path to excel csv file
# Assign a variable for the file to load and the path.
#file_to_load = 'Resources/election_results.csv'


#election_results = 'Resouces/election_results.csv'
#election_data = open(file_to_load, 'r' , encoding='UTF-8')
#election_data.close()

# Open the election results and read the file
#with open(file_to_load) as election_data:
    # To do: perform analysis.
 #   print(election_data)





