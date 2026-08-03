def first_occurrence(nums, target):
    left = 0
    right = len(nums) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            result = mid          # Store current index
            right = mid - 1       # Continue searching on the left

        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return result


# -----------------------------
# Test
# -----------------------------
nums = [1, 2, 2, 2, 3, 4]
target = 2

index = first_occurrence(nums, target)

print("First occurrence of", target, "is at index:", index)