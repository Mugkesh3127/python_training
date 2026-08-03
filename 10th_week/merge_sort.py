# -----------------------------
# Merge Sort
# -----------------------------
def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    # Find middle
    mid = len(arr) // 2

    # Divide
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge
    return merge(left, right)


def merge(left, right):

    result = []
    i = j = 0

    # Compare elements from both halves
    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# -----------------------------
# Test
# -----------------------------
arr = [38, 27, 43, 3, 9, 82, 10]

print("Original Array :", arr)

sorted_arr = merge_sort(arr)

print("Sorted Array   :", sorted_arr)