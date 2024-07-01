'''
dp[i][j] reach to this column , min value

'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        dp[0][0] = grid[0][0]
        for i in range(1,rows):
            dp[i][0] = grid[i][0]

        for j in range(1,cols):
            dp[0][j] = grid[j][0]

        for i in range(1,rows):
            for j in range(1,cols):
                ## state transfer， 这道题就是典型的 dp size = input size， 这里就不需要 -1 处理 ,因为size 一样
                dp[i][j] = min(dp[i - 1][j] , dp[i][j - 1]) + grid[i][j]

        return dp[rows - 1][cols - 1]