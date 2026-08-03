def counting_sort(arr, k):
    # Create count array
    count = [0] * (k + 1)

    # Count occurrences of each element
    for num in arr:
        count[num] += 1

    # Reconstruct the sorted array
    index = 0
    for i in range(k + 1):
        while count[i] > 0:
            arr[index] = i
            index += 1
            count[i] -= 1

    return arr


# -----------------------------
# Test
# -----------------------------
arr = [4, 2, 2, 8, 3, 3, 1]
k = 8

print("Original Array:", arr)
print("Sorted Array:", counting_sort(arr, k))