'''
不知道题目什么样  最大变长

边长的的定义就是 看你这个格子有几个越界或者有几个周围是0 （0）代表水
'''

class solution:
    def largestPrimeter(self,grid:list[list[int]]):
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        ## we use orignal grid as visited memo table
        ## if cross bound , return 1 ,if is water, return 1 for bound
        def dfs(row,col):
            if not ( 0 <= row < rows and 0<=col < cols):
                return 1 ## cross bound
            if grid[row][col] == 0:
                # get water
                return 1
            if grid[row][col] == 2:
                ## visited before
                return 0
            ## if this is an unvisted island (1)
            grid[row][col] = 2 ## set as vistied
            size = 0
            size += dfs(row + 1 , col) + dfs(row - 1 ,col) + dfs(row,col +1 )+ dfs(row, col -1 )
            return size

        for i in range(rows):
            for j in range(cols):
                if grid[rows][cols] == 1 : # start from any island
                    res = max(res,dfs(i,j))
                    ## if we only have 1 island break here

        return res
