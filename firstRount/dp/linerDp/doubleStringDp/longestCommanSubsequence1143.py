class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # state
        size_one = len(text1)
        size_two = len(text2)
        # dp[i][j] means lcs number when our substring end with i, j
        dp = [[0 for _ in range(size_one+1)] for _ in range(size_two+1)]
        # inital done, every one is 0
        for i in range(1,size_one + 1):
            for j in range(1, size_two + 1):
                # state transfer 2 conditions
                if text1[i - 1] == text2 [j - 1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        # final state
        return dp[size_one][size_two]
