# Median of Medians implementation in Python

def partition(arr, low, high, pivot):
    pivot_index = arr.index(pivot)
    arr[low], arr[pivot_index] = arr[pivot_index], arr[low]  # Move pivot to start
    i = low + 1
    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[low], arr[i - 1] = arr[i - 1], arr[low]  # Move pivot to its correct position
    return i - 1

def select_pivot(arr):
    # Divide arr into groups of 5, sort each group, and find the median of each group
    sublists = [sorted(arr[i:i + 5]) for i in range(0, len(arr), 5)]
    medians = [sublist[len(sublist) // 2] for sublist in sublists]
    
    # Recursively find the median of the medians
    if len(medians) <= 5:
        return sorted(medians)[len(medians) // 2]
    else:
        return median_of_medians(medians)

def median_of_medians(arr, k):
    if len(arr) == 1:
        return arr[0]

    # Step 1: Find a good pivot
    pivot = select_pivot(arr)

    # Step 2: Partition the array around the pivot
    pivot_index = partition(arr, 0, len(arr) - 1, pivot)

    # Step 3: Determine which side to recurse on
    if k == pivot_index:
        return arr[pivot_index]
    elif k < pivot_index:
        return median_of_medians(arr[:pivot_index], k)
    else:
        return median_of_medians(arr[pivot_index + 1:], k - pivot_index - 1)

# Helper function to find the k-th smallest element
def find_kth_smallest(arr, k):
    return median_of_medians(arr, k)

# Example usage
arr = [12, 3, 5, 7, 4, 19, 26, 14, 2, 11, 8]
k = 4  # Find the 5th smallest element (0-indexed)
find_kth_smallest(arr, k)
