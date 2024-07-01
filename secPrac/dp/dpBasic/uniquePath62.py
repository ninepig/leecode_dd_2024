class Solution:
    '''这道题不需要m+1 n+1 因为我们是到达右下角 不是m，n
    dp corner case的经典错误'''
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = 1
        for j in range(n + 1):
            dp[0][j] = 1

        for i in range(1,m + 1):
            for j in range(1,n + 1):
                dp[i][j]  = dp[i - 1][j] + dp[i][j - 1]

        return dp[m][n]
        '''
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]  = dp[i - 1][j] + dp[i][j - 1]

        return dp[m-1][n-1]