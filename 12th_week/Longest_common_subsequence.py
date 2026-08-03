def longest_common_subsequence(text1, text2):
    m = len(text1)
    n = len(text2)

    # DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct LCS
    i = m
    j = n
    lcs = []

    while i > 0 and j > 0:

        if text1[i - 1] == text2[j - 1]:
            lcs.append(text1[i - 1])
            i -= 1
            j -= 1

        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lcs.reverse()

    return dp[m][n], "".join(lcs), dp


# -------------------------
# Test
# -------------------------
text1 = "abcde"
text2 = "ace"

length, subsequence, table = longest_common_subsequence(text1, text2)

print("LCS Length:", length)
print("LCS:", subsequence)

print("\nDP Table:")
for row in table:
    print(row)