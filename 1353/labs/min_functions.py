import random
import time

def min1(input_list: list[int])->int:
    min = input_list[0]  
    for value in input_list:
        if min > value :
            min = value
    return min

def min2(input_list: list[int])->int:
    # performs bubble sort on the input
    n = len(input_list)
    for i in range(n):
        for j in range(1, n-i):
            if input_list[j - 1] > input_list[j]:
            # swap elements
                temp = input_list[j - 1]
                input_list[j - 1] = input_list[j]
                input_list[j] = temp
    return input_list[0]

def main():
    
    num_trials = 10
    print(f'n:\ttime per call:\t\ttotal elapsed time')
    for n in range(1000, 10001, 1000):
        random_list = [random.randint(0, 20) for i in range(n)]
        start_time = time.time()
        for _ in range(num_trials):
            min2(random_list)
        end_time = time.time()
        print(f'{n}\t{(end_time - start_time) / num_trials:.6f}\t{end_time - start_time:.6f}')
    
if __name__ == "__main__":
    main()