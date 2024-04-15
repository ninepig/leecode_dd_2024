import collections


class solution:
    def getLongestSIncreasingValuePath(self, grid):
        ## sanity check and others conditions
        if not grid:
            raise Exception("wrong input")

        '''
        Using dfs + memo to travel search all grid .
        '''
        rows = len(grid)
        cols = len(grid[0])
        ## memo record longest path in that point
        memo = [[0 for _ in range(cols)] for _ in range(rows)]
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(row, col, memo):
            if memo[row][col] != 0:
                return memo[row][col]
            cur = 1
            for d in dirs:
                new_row = d[0] + row
                new_col = d[1] + col
                ## bug 迷糊了 ，这里是大于  ， increasing order
                if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] > grid[row][col]:
                    cur = max(dfs(new_row, new_col, memo) + 1, cur)

            memo[row][col] = cur
            return cur

        res = 0

        for i in range(rows):
            for j in range(cols):
                if memo[i][j] == 0:
                    res = max(res, dfs(i, j, memo))

        return res

## todo adding here  bfs way
