# https://www.reddit.com/r/leetcode/comments/19b2h09/really_hard_problem_in_amazon_oa/
## https://www.fastprep.io/problems/amazon-minimum-total-errors
'''

Databases doesn't support very large numbers, so numbers are stored as a string of binary characters, '0' and '1'. Accidentally, a ! was entered at some positions and it is unknown whether they should be '0' or '1'.

The string of incorrect data is made up of the characters '0', '1' and ! where '!' is the character that got entered incorrectly. '!' can be replaced with either '0' or '1'. Due to some internal faults, some errors are generated every time '0' and '1' occur together as '01' or '10' in any subsequence of the string. It is observed that the number of errors a subsequence '01' generates is x, while a subsequence '10' generates y errors.

Determine the minimum total errors generated? Since the answer can be very large, return it modulo 109+7.

'''
def minTotalErrors(errorString, x, y):
    # python magic syntax
    if not errorString:
        return 0

    n = len(errorString)

    # Initialize dp array
    dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    # Fill dp table
    for i in range(1, n + 1):
        for j in range(i + 1):
            if errorString[i - 1] in ('0', '!'):
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + j * y)
            if errorString[i - 1] in ('1', '!'):
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + x * (i - j))

    return int(min(dp[n]))


print(minTotalErrors("01!0", 2, 3))
print(minTotalErrors("101!1", 2, 3))
print(minTotalErrors("!!!!!!!", 23, 28))
