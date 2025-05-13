from random import random
from time import time


def max(some_list: list)->int:
    max = some_list[0][0]
    for row in some_list:
        for value in row:
            if value>max:
                max = value
    return max

def normalize(some_list: list)->list:
    max_value = max(some_list)
    scaled = [[value/max_value for value in row] for row in some_list]
    return scaled

def main():
    n = 200
    nested_list = [[j*n + i + 1 for i in range(n)] for j in range(n)]

    # Time the following function call, with a variety of values for n:
    start_time = time()
    scaled = normalize(nested_list)
    end_time = time()
    
    elapsed_time = end_time - start_time
    print(elapsed_time)


# Run the program:
if __name__ == '__main__':
    main()