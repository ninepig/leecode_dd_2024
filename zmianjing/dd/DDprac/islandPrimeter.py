class solution:
    '''
    1 岛的周长 相当于 他旁边海的大小
    2 对于程序 岛--》1 ---》 它的四周如果是边界/海 则周长+1
    3 dfs 搜索过程之中
    '''
    def islandPrimeter(self, grid:list[list[int]]):
        rows = len(grid)
        cols = len(grid[0])
        ans = 0
        def dfs(row,col):
            if not(0 <= row < rows and 0 <= col < cols):
                return 1
            if grid[row][col] == 0:
                return 1
            if grid[row][col] == 2:
                return 0
            grid[row][col] = 2 ## set visited map

            return dfs(row + 1, col) + dfs(row - 1 , col) + dfs(row, col + 1) + dfs(row, col - 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1: ## starting from any island
                    boarder = dfs(i,j)
                    ans = max(ans,boarder)

        return ans 