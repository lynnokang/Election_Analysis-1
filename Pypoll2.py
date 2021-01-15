import csv
dir(csv)

import os
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
print("the time right now is", now)
file_to_load ="Resources/election_results.csv"
election_data = open(file_to_load, "r")
election_data.close()
with open(file_to_load) as election_data:
    print(election_data)
import csv
import os
file_to_load = os.path.join("Resources", "election_results.csv")
with open(file_to_load) as election_data:
    print(election_data)
file_to_save = os.path.join("Analysis", "election_analysis.txt")
open(file_to_save, "w")

file_to_save =os.path.join("analysis", "election_analysis.txt")
outfile = open(file_to_save, "w")
outfile.write("Hello World")

outfile.close()
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_save, "w") as txt_file:
    txt_file.write("Arapahoe")
    txt_file.write("Denver")
    txt_file.write("Jefferson")
election_data = open(file_to_load, 'r')
election_data.close()
with open(file_to_load) as election_data:
    print(election_data)
import csv
import os
file_to_load =os.path.join("Resources", "election_results.csv")
with open(file_to_load) as election_data:
    print(election_data)

file_to_save = os.path.join("analysis", "election_analysis.txt")
open(file_to_save, "w")
file_to_save = os.path.join("analysis", "election_analysis.txt")
outfile = open(file_to_save, "w")
outfile.write("Hello World")
outfile.close()

file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_save, "w") as txt_file:
    txt_file.write("Arapahoe, ")
    txt_file.write("Denver, ")
    txt_file.write("Jefferson")

file_to_save =os.path.join("analysis", "election_analysis.txt")
with open(file_to_save, "w") as txt_file:
    txt_file.write("Arapahoe\nDenver\nJefferson")
    


























    




