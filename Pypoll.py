print("Hello World")
counties =["Arapahoe","Denver","Jefferson"]
print (counties)
print (counties)
if counties[1] =="Denver":
    print(counties[1])

    counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
  print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")
    if "Arapahoe" in counties and "El Paso" not in counties:
        print (" Only Arapahoe is in the list of counties.")
    else:
        print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

for county in counties:
    print(county)
    counties_dict ={"Arapahoe":422829, "Denver":463353,"Jefferson":432438}
    for county in counties_dict:
        print(county)
    for county in counties_dict.keys():
        print(county)
    for voters in counties_dict.values():
        print(voters)
    for county in counties_dict:
        print(counties_dict[county])

    voting_data = [{"county":"Arapahoe", "registered_voters":422829},
        {"county":"Denver", "registered_voters": 463353},
        {"county":"Jefferson","registered_voters": 432438}]
    for county_dict in voting_data:
            print(county_dict)
    for  county_dict in voting_data:
        for value in county_dict.values():
            print(value)
            print(county_dict["registered_voters"])
        for county_dict in voting_data:
            print(county_dict["county"])

           















   






# The data we need to retrieve
#The total number of vote cast
#A complete list of candidates who received votes
# The total number of votes each candidates won
#The winner of the election based on popular vote