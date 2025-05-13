values = [41, 28, 11, 82, 40, 75, 21, 0,  90, 52, 96, 70, 83, 98, 1, 43, 4, 85, 79, 87]

for value in values:
    print(f'{((13*value + 5) % 23) % 20} : {value}')

