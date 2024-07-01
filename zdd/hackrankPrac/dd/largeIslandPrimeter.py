class Solution:
    def largestIslandPrimeter(self, grid):
        ## santiy check
        if not grid or len(grid) == 0:
            raise Exception("wrong input")
        '''
        we use grid it self as memo table
        2 means visited
        1 means island
        0 means water
        for primeter 
            if we get 
            1 cross grid
            2 water  
            primeter +1
        '''
        max_value = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):
            if not (0 <= row < rows and 0 <= col < cols):
                ## cross grid
                return 1
            if grid[row][col] == 2:
                return 0  ## vistied
            if grid[row][col] == 0:
                return 1  # water
            grid[row][col] = 2  # set island to vistied

            return dfs(row - 1, col) + dfs(row + 1, col) + dfs(row, col - 1) + dfs(row, col + 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:  ## starting from one island
                    max_value = max(max_value, dfs(i, j))

        return max_value


grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
sol = Solution()
print(sol.largestIslandPrimeter(grid))