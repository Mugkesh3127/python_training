def find_median_sorted_arrays(nums1, nums2):
    # Ensure nums1 is the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m = len(nums1)
    n = len(nums2)

    left = 0
    right = m

    while left <= right:
        partitionX = (left + right) // 2
        partitionY = (m + n + 1) // 2 - partitionX

        # Handle boundaries
        maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        minRightX = float('inf') if partitionX == m else nums1[partitionX]

        maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        minRightY = float('inf') if partitionY == n else nums2[partitionY]

        # Correct partition found
        if maxLeftX <= minRightY and maxLeftY <= minRightX:

            # Even total number of elements
            if (m + n) % 2 == 0:
                return (
                    max(maxLeftX, maxLeftY) +
                    min(minRightX, minRightY)
                ) / 2

            # Odd total number of elements
            else:
                return max(maxLeftX, maxLeftY)

        # Move left
        elif maxLeftX > minRightY:
            right = partitionX - 1

        # Move right
        else:
            left = partitionX + 1


# -----------------------------
# Test
# -----------------------------
nums1 = [1, 3]
nums2 = [2]

print(find_median_sorted_arrays(nums1, nums2))

nums1 = [1, 2]
nums2 = [3, 4]

print(find_median_sorted_arrays(nums1, nums2))