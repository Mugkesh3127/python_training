def length_of_lis(nums):
    n = len(nums)

    # Every element is an LIS of length 1
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

        print(f"After processing {nums[i]:>3}: {dp}")

    return max(dp), dp


# -----------------------
# Test
# -----------------------
nums = [10, 9, 2, 5, 3, 7, 101, 18]

length, dp = length_of_lis(nums)

print("\nFinal DP:", dp)
print("Length of LIS:", length)