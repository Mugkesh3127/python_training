def coin_change(coins, amount):
    # Initialize DP array
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    # Build DP table
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount], dp


# -----------------------------
# Test
# -----------------------------
coins = [1, 5, 10, 25]
amount = 37

minimum_coins, dp = coin_change(coins, amount)

print("Minimum Coins Needed:", minimum_coins)
print(dp)