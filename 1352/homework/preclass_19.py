import csv
    
winners=[]

try:
    with open('homework/oscar_age_female.csv') as file:
        for line in file:
            winners.append(line.strip().split(","))
except FileNotFoundError:
    print("Data file with Oscar winners not found")
    exit()

count_of_wins = {}
for winner in winners:
    if winner[3] in count_of_wins:
        count_of_wins[winner[3]] += 1
    else:
        count_of_wins[winner[3]] = 1
        
count = 0
for actor_name in count_of_wins:
    if count_of_wins[actor_name] > 1:
        count += 1

for actor_name in count_of_wins:
    if count_of_wins[actor_name] > 2:
        print(actor_name, count_of_wins[actor_name])


        
print(count)