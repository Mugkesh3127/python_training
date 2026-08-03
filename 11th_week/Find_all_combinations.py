def combination_sum(candidates, target):
    result = []

    def backtrack(start, current, total):
        # Found a valid combination
        if total == target:
            result.append(current[:])
            return

        # Stop if sum exceeds target
        if total > target:
            return

        # Try all candidates starting from 'start'
        for i in range(start, len(candidates)):
            current.append(candidates[i])

            # Reuse the same element (pass i, not i+1)
            backtrack(i, current, total + candidates[i])

            # Backtrack
            current.pop()

    backtrack(0, [], 0)
    return result


# -----------------------------
# Test
# -----------------------------
candidates = [2, 3, 6, 7]
target = 7

answer = combination_sum(candidates, target)

print("Combinations:")
for combo in answer:
    print(combo)