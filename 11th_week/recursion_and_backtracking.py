# Recursion
def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1

    # Recursive call
    return n * factorial(n - 1)


# Test
n = 5
print("Factorial:", factorial(n))


# Backtracking
def subsets(nums):
    result = []

    def backtrack(index, current):

        if index == len(nums):
            result.append(current[:])
            return

        # Include current element
        current.append(nums[index])
        backtrack(index + 1, current)

        # Undo choice (Backtrack)
        current.pop()

        # Exclude current element
        backtrack(index + 1, current)

    backtrack(0, [])

    return result


# Test
nums = [1, 2, 3]

print(subsets(nums))