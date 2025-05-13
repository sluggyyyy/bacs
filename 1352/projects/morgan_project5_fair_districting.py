"""
    Description of program: Program that calculates wasted votes and efficiency gaps for elections in specific years/states
    Filename: morgan_project5_fair_districting.py
    Author: Zachary Morgan  
    Date: 02/26/25
    Course: Project 5 - Fair districting, Gerrymandering, Wasted Votes and Efficiency Gap 
    Assignment: Project 3 SandGame - Part 2 
    Collaborators: N/A
    Internet Source: geeksforgeeks
"""
class Election:
    def __init__(self, district, votes1, votes2):
        self.district = district
        self.votes1 = votes1
        self.votes2 = votes2
    
    def __str__ (self):
        return f"Election(district='{self.district}', votes1={self.votes1}, votes2={self.votes2})"

"""
Class that stores election data, for use inside of the [year][state] keys
"""
        
def parse_data(path):
    election_data = {}
    
    with open(path, "r") as file:
        for line in file:
            data = line.strip().split(",")
            
            # For each line, read data into variables
            year = data[0]
            state = data[1]
            # Set everything after the first two entries to district data
            district_data = data[2:]
            
            # If the year is not already in the dictionary,
            if year not in election_data:
                # Set key at year to an empty dictionary
                election_data[year] = {}   
            # If the state is not already in the dictionary,
            if state not in election_data[year]:
                # Set key at [year][state] to an empty list for holding Election objects
                election_data[year][state] = []
            
            # Loop over the length of district_data in steps of 3
            for i in range(0, len(district_data), 3):
                # Set values inside of district_data to variables
                district = district_data[i]
                votes1 = int(district_data[i+1])
                votes2 = int(district_data[i+2])
                
                # Use variables from loop to create Election objects
                election = Election(district, votes1, votes2)
                # Append objects to the list at [year][state]
                election_data[year][state].append(election)
    
    return election_data
"""
Function that parses election data text file and reads it into a dictionary
Parameters: file path
Returns: dictionary of election data
"""
def report_efficiency_gap(districts: list[Election]):
    # Initialize variables to be used later in function
    dem_waste = 0
    rep_waste = 0
    total_votes = 0
    
    # Loop over districts list
    for district in districts:
        # Calculate total votes
        total_votes += district.votes1 + district.votes2
        
        # If dem votes are more than rep votes
        if district.votes1 > district.votes2:
            # Calculate wasted votes
            winning_threshold = (district.votes1 + district.votes2) / 2 + 1
            dem_waste += district.votes1 - winning_threshold
            rep_waste += district.votes2
        else:
            # If rep votes > dem votes, repeat but for republican votes
            winning_threshold = (district.votes1 + district.votes2) / 2 + 1       
            rep_waste += district.votes2 - winning_threshold
            dem_waste += district.votes1
        
        # Calculate efficiency gap
        efficiency_gap = ((rep_waste - dem_waste) / total_votes) * 100
        
        # Check favoring
        if efficiency_gap > 0:
            favored_party = "Democrats"
        else: 
            favored_party = "Republican"
    
    # Print feedback for user
    print(f'Wasted Democratic votes: {dem_waste:.1f}')
    print(f'Wasted Republican votes: {rep_waste:.1f}')
    print(f'Efficiency gap: {efficiency_gap:.1f}%, in favor of {favored_party}')
            
    return efficiency_gap
"""
Function that takes a list of objects and manipulates data inside of them
to calculate efficiency gap and wasted votes
Parameters: list of Election objects
Returns: efficiency gap value
"""
election_results = parse_data("projects/1976-2020votes.txt")

print('This program evaluates districting fairness for US House elections from 1976-2020.')
# Start feedback loop
while True:
    while True:
        # Take input from user and check if it is a digit, if it is, convert to int
        year = input('What election year would you like to evaluate? ')
        if year.isdigit():
            year = int(year)
            # Check if the year entered is in the dictionary
            if str(year) in election_results:
                # Check if year is even
                if year % 2 == 0:
                    break
                else:
                    print(f'Sorry, valid election years are even years from 1976-2020.')
            else:
                print(f'{year} is not a valid election year.')
        else:
            print(f'{year} is not a numerical value!')
        
    while True:
        # Take in state from user input
        state = input('What state would you like to evaluate? ')
        state = state.upper()
        # Check if state is in election_results[year]
        if state.upper() in election_results[str(year)]:
            # If there is more than one district
            if len(election_results[str(year)][state]) > 1:
                # Print how many districts are in [year][state]
                print(f'{len(election_results[str(year)][state])} districts.')
                # Call report_efficiency_gap to give user final feedback
                report_efficiency_gap(election_results[str(year)][state])
                break
            else:
                print('Efficiency gap cannot be computed for states with only one district.')
        else:
            print(f'{state} is not a valid state.')

    while True:
        # Take input from user to determine whether or not to continue the program
        cont = input('Would you like to continue? ')
        if cont.upper() == 'YES':
            break
        elif cont.upper() == 'NO':
            break
        else:
            print("Invalid response. Please enter a 'yes' or a 'no'!")
    
    # Kill program if input == no
    if cont == 'no':
        break