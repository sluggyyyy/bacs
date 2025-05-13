import random
import time

# O(n)
def sequential_negative(l, x):
    neg_x = -x
    for num in l:
        if num == neg_x:
            return True
        
    return False

# O(log(n))
def binary_negative(l, x):
    start = 0
    end = len(l) - 1
    neg_x = -x
    
    while start <= end:
        mid = (start + end) // 2
        
        if l[mid] == neg_x:
            return True
        if neg_x < l[mid]:
            end = mid - 1
        else:
            start = mid + 1
            
    return False
    

# O(n)
def mystery_search(l):
    i = 0
    j = len(l) - 1
    
    while i < j:
        current_sum = l[i] + l[j]

        if current_sum == 0:
            return True
        elif current_sum < 0:
            i += 1
        else:
            j -= 1

    return False

def create_worst_list(n):
    # No negatives = no sum of 0, no negative value for binary and sequential
    return [i for i in range(1, n*10, 10)]

def main():
    # Initiralize a list for the results
    results = []
    # Initialize a list of the algorithm function names
    algos = [sequential_negative, binary_negative, mystery_search]
    # Initialize a list for the sizes
    sizes = [5000, 10000, 20000, 40000, 80000]
    # Loop over sizes list
    for size in sizes:
        # Loop over algorithms list
        for algo in algos:
            # Create worst case list
            wlist = create_worst_list(size)
            # Sort worst case list
            wlist.sort()
            
            # Set "random" value for x
            x = -999999
            
            # Record start time
            start_time = time.time()
            
            # If the algorithm name is mystery search
            if algo.__name__ == "mystery_search":
                # Call it with the list
                algo(wlist)
            # If the name is one of the ones that takes in an x parameter
            else:
                # Call it with x
                algo(wlist, x)
            
            # Record end time
            end_time = time.time()
            
            elapsed = end_time - start_time
            # Append the results as a tuple
            results.append((size, algo.__name__, elapsed))
        
    print("n\tAlgorithm\tTime")
    print()
    # Initialize current size used for indenting before n increases
    current_size = None
    # Loop over results
    for result in results:
        # If the current size is not none and the size stored in the tuple does not equal current_size
        if current_size is not None and result[0] != current_size:
            # Print a new line
            print()
        
        # Print the size, algorithm name, and time
        print(f"{result[0]}\t{result[1]}\t\t{result[2]}")
        # Set current_size to that of the current result
        current_size = result[0]

if __name__ == '__main__':
    main()