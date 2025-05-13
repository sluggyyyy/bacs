import numpy as np

# np.random.seed(3042024)
# arr = np.random.randint(0, 1000, 30)
# arr2 = np.array([i for i in range(30)])

# def modified_selection_sort(arr):
#     compares = 0 
#     swap_distance = 0
    
#     for pass_number in range(arr.size - 1):
#         max_index = 0  # Reset max index for each pass
        
#         for i in range(1, arr.size - pass_number):  # Start at index 1
#             compares += 1  # Count every comparison
#             if arr[i] > arr[max_index]:
#                 max_index = i  # Update max_index
        
#         # Swap with the last unsorted element
#         swap_pos = arr.size - pass_number - 1
        
#         if max_index != swap_pos:  # Swap only if needed
#             arr[max_index], arr[swap_pos] = arr[swap_pos], arr[max_index]
#             swap_distance += abs(max_index - swap_pos)  # Track swap distance

#     print(f'Compares: {compares}')
#     print(f'Swap Distance: {swap_distance}')

# print("Before sorting:", arr2)
# modified_selection_sort(arr2)
# print("After sorting:", arr2)

np.random.seed(3042024)
arr = np.random.randint(0, 1000, 30)

def bubble_sort(arr):
    compares = 0
    swap_distance = 0
    n = arr.size  # Length of array
    
    for pass_number in range(n - 1):
        for i in range(n - 1 - pass_number):  # Decreasing range in each pass
            compares += 1  # Every comparison is counted
            if arr[i] > arr[i + 1]:  # If elements are out of order
                arr[i], arr[i + 1] = arr[i + 1], arr[i]  # Swap elements
                swap_distance += 1  # Swaps always have distance of 1

print("Before sorting:", arr)
bubble_sort(arr)
print("After sorting:", arr)