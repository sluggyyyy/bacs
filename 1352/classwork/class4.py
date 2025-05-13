from random import random
numbers = [[int(random()*4) for column in range(8)] for row in range(5)]
print(numbers)

# sum of row index 3, content-based loop
total = 0
for num in numbers[3]:
    total += num
print(total)

# sum of index 3 row, index-based
total = 0
for col_index in range(len(numbers[3])):
    total = total + numbers[3][col_index]
print(total)

# sum of every row (sum is calculated for each row separately)
for row in range(len(numbers)):
    total = 0
    for value in range(len(numbers[row])):
        total += numbers[row][value]
    print(f'sum of row index {row}: {total}')
    
# sum of entire list
total = 0   
for row in range(len(numbers)): 
    for value in range(len(numbers[row])):
        total += numbers[row][value]
print(f'{total}')

# sum of every column; assumes a rectangular nested list
for col_index in range(len(numbers[0])):
    total = 0
    for row_index in range(len(numbers)):
        total += numbers[row_index][col_index]
    print(f'total of column {col_index}: {total}')
    