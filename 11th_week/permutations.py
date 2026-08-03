def permutations(nums):
    result = []

    def backtrack(path, used):
        # Base case: one complete permutation
        if len(path) == len(nums):
            result.append(path[:])
            return

        # Try every unused element
        for i in range(len(nums)):
            if used[i]:
                continue

            # Choose
            path.append(nums[i])
            used[i] = True

            # Explore
            backtrack(path, used)

            # Backtrack
            path.pop()
            used[i] = False

    backtrack([], [False] * len(nums))
    return result


# -----------------------------
# Test
# -----------------------------
nums = [1, 2, 3]

ans = permutations(nums)

print("All Permutations:")
for perm in ans:
    print(perm)