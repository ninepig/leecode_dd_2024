class Solution:
    def dfs(self, grid, i, j, m, n)-> int:
        if i < 0 or j < 0 or i >= m or j >=0 or grid[i][j] == '0':
            return 0
        # dfs的目的是累加 , 同时置0
        ans = 1
        grid[i][j] = '0'
        ans += self.dfs(grid,i+1,j,m,n)
        ans += self.dfs(grid,i-1,j,m,n)
        ans += self.dfs(grid,i,j+1,m,n)
        ans += self.dfs(grid,i,j-1,m,n)
        return ans

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid :
            return 0
        ans = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans = max(ans,self.dfs(grid,i,j,m,n))
        return