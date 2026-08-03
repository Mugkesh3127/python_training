# Naive Recursion
def fib_recursive(n):
    if n <= 1:
        return n

    return fib_recursive(n - 1) + fib_recursive(n - 2)


# Test
n = 10
print("Recursive:", fib_recursive(n))



# Memoization using @lru_cache
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_memo(n):
    if n <= 1:
        return n

    return fib_memo(n - 1) + fib_memo(n - 2)


# Test
n = 10
print("Memoization:", fib_memo(n))


# Bottom-Up Tabulation (Dynamic Programming)
def fib_tabulation(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# Test
n = 10
print("Tabulation:", fib_tabulation(n))


# Space Optimization
def fib_optimized(n):
    if n <= 1:
        return n

    prev2 = 0
    prev1 = 1

    for _ in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1


# Test
n = 10
print("Optimized:", fib_optimized(n))