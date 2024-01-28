class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #state
        #dp[i][j] 表示要经过多少次操作才能把 结尾为i 变为结尾为j的字符串
        size_one = len(word1)
        size_two = len(word2)
        # initial ,初始值 可以这么设 因为是确定的值，没有任何比较
        dp =[[0 for _ in range(size_one + 1)] for _ in range(size_two + 1)]
        for i in range(1,size_one + 1):
            dp[i][0] = i
        for j in range(1,size_two + 1):
            dp[0][j] = j

        # state transfer
        for i in range(1, size_one + 1):
            for j in range(1, size_two + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i-1][j-1] # 如果相同，则不需要编辑，维持数量不变
                else:
                    # insert , edit , remove, least of them + 1
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + 1

        return dp[size_one][size_two]