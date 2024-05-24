'''
Given an m x n 2D grid map of '1’s which represents land and '0’s which represents water returns the number of islands
(surrounded by water and formed by connecting adjacent lands in 2 directions - vertically or horizontally).
'''

class solution:
    def numberOfIsland(self,grid:list[list[int]]):
        if not grid or len(grid) == 0 :
            return 0
        rows = len(grid)
        cols = len(grid[0])
        def dfs(row,col):
            if row<0 or row >= rows or col <  0 or col>= cols:
                return
            if grid[row][col] == 0:
                return
            grid[row][col] = 0
            dfs(row + 1 ,col)
            dfs(row,col+1)
            dfs(row-1,col)
            dfs(row,col-1)

        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dfs(i,j)
                    count += 1

        return count