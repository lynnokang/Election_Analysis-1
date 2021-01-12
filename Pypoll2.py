import csv

# The data we need to retrieve
#The total number of vote cast
#A complete list of candidates who received votes
# The total number of votes each candidates won
#The winner of the election based on popular vote
# Import the datetime class from the datetime module.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)
import csv
import os
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis -1.txt")
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers =next(file_reader)
    




