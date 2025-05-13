import random
import numpy as np
import time

arr1 = np.array([i for i in range(4000)])
np.random.shuffle(arr1)

arr2 = np.array([i for i in range(4000)])
for _ in range(10):
    i = random.randint(0,3999)
    j = random.randint(0,3999)
    arr2[i], arr2[j] = arr2[j], arr2[i]

arr3 = np.array([1])
arr4 = np.array([])

arr5 = np.array([i for i in range(4000)])
np.random.shuffle(arr5)

def insert_sort(arr):
    compares = 0
    swaps = 0
    for pass_number in range(1, arr.size):
        current_position = pass_number
        while current_position > 0 and arr[current_position] < arr[current_position - 1]:
            compares += 1
            swaps += 1
            arr[current_position] = arr[current_position - 1]
            arr[current_position - 1] = arr[current_position]
            current_position -= 1

def modified_selection_sort(arr):
    compares = 0 
    swap_distance = 0
    
    for pass_number in range(arr.size - 1):
        max_index = 0  # Reset max index for each pass
        
        for i in range(1, arr.size - pass_number):  # Start at index 1
            compares += 1  # Count every comparison
            if arr[i] > arr[max_index]:
                max_index = i  # Update max_index
        
        # Swap with the last unsorted element
        swap_pos = arr.size - pass_number - 1
        
        if max_index != swap_pos:  # Swap only if needed
            arr[max_index], arr[swap_pos] = arr[swap_pos], arr[max_index]
            swap_distance += abs(max_index - swap_pos)  # Track swap distance

start_time = time.time()
insert_sort(arr5)
stop_time = time.time()

start_time2 = time.time()
modified_selection_sort(arr5)
stop_time2 = time.time()

start_time3 = time.time()
insert_sort(arr2)
stop_time3 = time.time()

start_time4 = time.time()
modified_selection_sort(arr2)
stop_time4 = time.time()

print(f'{stop_time - start_time}')
print(f'{stop_time - start_time2}')
print()
print(f'{stop_time3 - start_time3}')
print(f'{stop_time4 - start_time4}')