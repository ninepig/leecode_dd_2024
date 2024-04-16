import collections


class solution:
    def getLongestSameValuePath(self, grid):
        ## sanity check and others conditions
        if not grid:
            raise Exception("wrong input")

        '''
        Using dfs + memo to travel search all grid .
        we updated in each dfs searching level
        '''
        rows = len(grid)
        cols = len(grid[0])
        max_value = 0
        ## memo record longest path in that point
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(row, col):
            if visited[row][col]:
                return 0
            visited[row][col] = True
            cur = 1
            for d in dirs:
                new_row = row + d[0]
                new_col = col + d[1]
                if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == grid[row][col]:
                    cur = max(dfs(new_row, new_col) + 1, cur)

            visited[row][col] = False  ## we need back track
            return cur

        res = 0
        for i in range(rows):
            for j in range(cols):
                ## starting from any value
                res = max(res, dfs(i, j))

        return res


nums = [[7, 5, 6, 6, 6, 6],
        [7, 7, 4, 6, 6, 6],
        [7, 7, 1, 2, 3, 6],
        [7, 1, 7, 7, 3, 2],
        [7, 7, 7, 7, 7, 1],
        [1, 1, 1, 1, 1, 1]]
sol = solution()
print(sol.getLongestSameValuePath(nums))
