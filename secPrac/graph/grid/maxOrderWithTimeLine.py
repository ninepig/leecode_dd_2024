'''
题目是求2D数组里可以根据时间线拿的最多个订单数，利口329 doordash
dfs + memo
o(m*n)
'''
import math


class solution:
    def getLongestValidOrder(self,grid:list[list[int]]):
        if not grid or len(grid) == 0:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        def dfs(row,col):
            if visited[row][col] != 0:
                return visited[row][col]
            cur = 1 # for each order ,basic is 1
            for dir in dirs:
                new_row = row + dir[0]
                new_col = col + dir[1]
                ## 不需要判断是否 visited。因为在dfs之中有判断。
                if 0 <= new_row < rows and 0<=new_col < cols  and grid[new_row][new_col] > grid[row][col]:
                    cur = max(dfs(new_row,new_col) + 1, cur)
            ## 记录当前四个方向能得到最大的值
            visited[row][col] = cur

            return visited[row][col]

        res = 0
        for i in range(rows):
            for j in range(cols):
                if visited[i][j] == 0:
                    res = max(res,dfs(i,j))

        return res