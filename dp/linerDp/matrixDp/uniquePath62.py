class Solution:
    '''
    矩阵线性dp
    1 split phase
    2 define state
    3 state transfer
    4 inital state
    5 final state

    '''
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(m):
            dp[i][0] = 1 # in the boarder, we only have 1 way to there
        for i in range(n):
            dp[0][i] = 1

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]

        # board的结尾
        return dp[m-1][n-1]

