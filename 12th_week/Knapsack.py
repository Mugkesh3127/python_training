def knapsack(weights, values, capacity):
    n = len(weights)

    # DP table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):

            # Item doesn't fit
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]

            else:
                # Max of excluding or including the item
                dp[i][w] = max(
                    dp[i - 1][w],
                    values[i - 1] + dp[i - 1][w - weights[i - 1]]
                )

    return dp[n][capacity], dp


# ------------------------
# Test
# ------------------------
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

max_value, dp = knapsack(weights, values, capacity)

print("Maximum Value:", max_value)

print("\nDP Table:")
for row in dp:
    print(row)