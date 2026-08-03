def subsets(nums):
    result = []

    def backtrack(index, current):
        # If all elements are considered
        if index == len(nums):
            result.append(current[:])
            return

        # Choice 1: Exclude current element
        backtrack(index + 1, current)

        # Choice 2: Include current element
        current.append(nums[index])
        backtrack(index + 1, current)

        # Backtrack
        current.pop()

    backtrack(0, [])
    return result


# -----------------------------
# Test
# -----------------------------
nums = [1, 2, 3]

ans = subsets(nums)

print("All Subsets:")
for subset in ans:
    print(subset)