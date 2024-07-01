class solution:
    '''
    sub island which in grid 1
    1 removed the island which in grid2 but not in grid 1
    2 found the island in grid2 now
    '''

    def subIslandCount(self, grid: list[list[int]], grid2: list[list[int]]) -> int:
        if not grid or not grid2:
            return -1

        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col>= cols:
                return
            if grid2[row][col] == 0 :
                return
            grid2[row][col] = 0  ## dismiss target island
            dfs(row + 1 ,col)
            dfs(row - 1 ,col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        # remove island not subisland in 1 first
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0 and grid2[i][j] == 1 : # island in grid2 but not in grid1
                    dfs(i,j)

        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1:
                    dfs(i,j)
                    count += 1

        return count