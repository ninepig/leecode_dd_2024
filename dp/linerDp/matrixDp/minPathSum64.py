class Solution:
    '''matrix dp'''
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        # state , dp[i][j] means arrive i , j min path sum
        rows = len(grid)
        cols = len(grid)
        dp = [[ 0 for _ in range(rows)] for _ in range(cols)]

        # inital state -> first row , first col eqauls arrvie theirs' grid value
        for i in range(rows):
            dp[0][i] = dp[0][i] + grid[0][i]
        for i in range(cols):
            dp[i][0] = dp[i][0] + grid[i][0]

        # transfer --> current grid = min(up, left） + grid
        for i in range(1,rows):
            for j in range(1,cols):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]

        return dp[rows - 1][cols -1 ]