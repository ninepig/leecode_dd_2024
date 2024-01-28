class Solution:
    '''类似包围题, 先把周围一圈的1 以及和她连接的1 设为0,这些就是可以跑出去的 然后数剩下的1'''


    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # directions = [(-1,0),(1,0),(0,1),(0,-1)]

        def dfs(i,j):
            if i < 0 or i >=m or j <0 or j>= n or grid[i][j] == 0:
                return
            grid[i][j] = 0
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        for i in range(m):
            if grid[i][0] == '1':
                dfs(i,0)
            if grid[i][n-1] == '1':
                dfs(i, n - 1)

        for j in range(n):
            if grid[0][j] == '1':
                dfs(0,j)
            if grid[m-1][j] == '1':
                dfs(m-1, j)

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans += 1

        return ans




