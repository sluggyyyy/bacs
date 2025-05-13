import numpy as np

def merge_arrays(arr1: np.ndarray, arr2: np.ndarray) -> np.ndarray:
    i, j = 0, 0
    merged_list = []

    # Merge the two arrays using a two-pointer approach
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged_list.append(arr1[i])
            i += 1
        else:
            merged_list.append(arr2[j])
            j += 1

    # Append remaining elements from arr1, if any
    while i < len(arr1):
        merged_list.append(arr1[i])
        i += 1

    # Append remaining elements from arr2, if any
    while j < len(arr2):
        merged_list.append(arr2[j])
        j += 1

    # Convert the merged list into a NumPy array and return
    return np.array(merged_list)