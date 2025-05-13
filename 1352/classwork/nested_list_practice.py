import random
random.seed(1272025)
practice_list = [[random.random() for i in range(3)] for j in range(10)]


for row in range(len(practice_list)):
    count = 0
    for cell in range(len(practice_list[row])):
        if practice_list[row][cell] > 0.1:
            count += 1
    print(count)