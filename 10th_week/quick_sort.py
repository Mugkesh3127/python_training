# -----------------------------
# Lomuto Partition
# -----------------------------
def partition(arr, low, high):
    pivot = arr[high]          # Last element as pivot
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


# -----------------------------
# QuickSort
# -----------------------------
def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)

        # Sort left part
        quicksort(arr, low, pivot_index - 1)

        # Sort right part
        quicksort(arr, pivot_index + 1, high)


# -----------------------------
# Test
# -----------------------------
arr = [38, 27, 43, 3, 9, 82, 10]

print("Original Array:", arr)

quicksort(arr, 0, len(arr) - 1)

print("Sorted Array:", arr)