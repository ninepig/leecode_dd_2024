class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    size = self.dfs(grid,i,j,rows,cols)
                    ans = max(size,ans)
        return ans

    def dfs(self, grid, i, j, rows, cols):
        if grid[i][j] == 0:
            return 0
        if i < 0 or i >= rows or j < 0 or j >= cols:
            return 0
        # at least we have 1 , since grid[i][j] = 1
        ans = 1
        ans += self.dfs(grid,i + 1 , j , rows, cols)
        ans += self.dfs(grid, i - 1, j, rows, cols)
        ans += self.dfs(grid, i , j + 1, rows, cols)
        ans += self.dfs(grid, i , j - 1 , rows, cols)
        return ans
