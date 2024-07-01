class Solution:
    '''
    dfs + visit ,这个是每次dfs就往前走 不需要回溯
    优化:利用原有的岛屿数组作为visit
    '''
    def numIslands(self, grid: List[List[str]]) -> int:
        ## helper list
        # visit = [[False for _ in range(len(grid))] for _ in range(len(grid[0]))]
        # for i in range
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        visit = [[False for _ in range(rows)] for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    self.dfs(visit,grid,i,j,rows,cols)
                    count += 1
        return count

    def dfs(self, visit, grid, row, col, rows, cols):
        if visit[row][col] == True:
            return
        visit[row][col] = True
        if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] =='0':
            return
        self.dfs(visit,grid,row + 1 , col , rows, cols)
        self.dfs(visit,grid,row - 1 , col , rows, cols)
        self.dfs(visit,grid,row  , col + 1 , rows, cols)
        self.dfs(visit,grid,row  , col - 1, rows, cols)



    def numIslandsBetter(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs2(grid, i, j)
                    count += 1
        return count

    def dfs2(self, grid, i, j):
        n = len(grid)
        m = len(grid[0])
        if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == '0':
            return 0
        grid[i][j] = '0'
        self.dfs2(grid, i + 1, j)
        self.dfs2(grid, i, j + 1)
        self.dfs2(grid, i - 1, j)
        self.dfs2(grid, i, j - 1)