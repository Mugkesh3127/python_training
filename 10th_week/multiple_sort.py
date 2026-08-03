def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Stop if already sorted
        if not swapped:
            break

    return arr


# Test
arr = [38, 27, 43, 3, 9, 82, 10]
print("Bubble Sort:", bubble_sort(arr.copy()))



# Merge Sort
def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):

    result = []
    i = j = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Test
arr = [38, 27, 43, 3, 9, 82, 10]
print("Merge Sort:", merge_sort(arr))


# Quick Sort (Lomuto Partition)
def partition(arr, low, high):

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):

        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quick_sort(arr, low, high):

    if low < high:

        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


# Test
arr = [38, 27, 43, 3, 9, 82, 10]

quick_sort(arr, 0, len(arr) - 1)

print("Quick Sort:", arr)



# Python Built-in
arr = [38, 27, 43, 3, 9, 82, 10]

sorted_arr = sorted(arr)

print("Original:", arr)
print("Sorted():", sorted_arr)