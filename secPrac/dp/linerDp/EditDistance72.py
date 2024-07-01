class Solution:
    '''太经典了 需要倒背如流 '''
    def minDistance(self, word1: str, word2: str) -> int:
        size1 = len(word1)
        size2 = len(word2)
        dp = [[ 0 for _ in range(size1 + 1)] for _ in range(size2 + 1)]
        for i in range(1,size1 + 1):
            dp[i][0] = i

        for j in range(1,size2 + 1):
            dp[0][j] = j

        for i in range(1,size1 + 1):
            for j in range(1,size2 + 1):
                if word1[i - 1] == word2[j - 1]: # state transfer , if pos is same, so dp[i][j] = dp[i - 1][j - 1]
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i-1][j - 1], dp[i-1][j],dp[i][j-1]) + 1

        return dp[size1][size2]

