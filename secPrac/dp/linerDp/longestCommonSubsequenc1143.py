'''
dp[i][j] means string1 string2 end with i , j position, longest common subsequnce length
dp[0][0] = 0
dp size = string length + 1  since dp[0] does not make sense , we need return dp[size][size2]
state transfer :
if string[i] = string2[j]
dp[i][j] = dp[i-1][j-1] + 1
else
dp[i][j] = max( dp[i-1][j],dp[i][j-1]


'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        size1 = len(text1)
        size2 = len(text2)
        dp = [[0 for _ in range(size2 + 1)] for _ in range(size1 + 1)]
        for i in range(1,size1 + 1):
            for j in range(1,size2 + 1):
                if text2[j - 1] == text1[i - 1]: # 对于 i j 在string之中 就是 i-1 j-1 要不然就不match了！！！切记切记 todo 统计上
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])

        return dp[size1][size2]