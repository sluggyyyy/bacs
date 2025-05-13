import random
random.seed(112023)
h = int(random.random()*15)
w = int(random.random()*20)
random_numbers = [[int(random.random()*1000) for col in range(w)] for row in range(h)]

column_sums = [sum(random_numbers[row][col] for row in range(h)) for col in range(w)]
print(column_sums)