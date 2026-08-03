# Memoization

from functools import lru_cache

def rob_memo(nums):

    @lru_cache(maxsize=None)
    def dp(i):
        if i >= len(nums):
            return 0

        # Option 1: Rob current house
        rob = nums[i] + dp(i + 2)

        # Option 2: Skip current house
        skip = dp(i + 1)

        return max(rob, skip)

    return dp(0)


# Test
houses = [2, 7, 9, 3, 1]
print("Maximum Money (Memoization):", rob_memo(houses))


# Tabulation
def rob_tabulation(nums):
    n = len(nums)

    if n == 0:
        return 0
    if n == 1:
        return nums[0]

    dp = [0] * n

    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

    return dp[-1]


# Test
houses = [2, 7, 9, 3, 1]
print("Maximum Money (Tabulation):", rob_tabulation(houses))