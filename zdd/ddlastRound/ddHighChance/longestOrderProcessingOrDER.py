'''
题目是求2D数组里可以根据时间线拿的最多个订单数，利口伞贰玖
dfs + memo
o(m*n)
'''
import collections


class solution:
    def getLongestValidOrder(self,grid:list[list[int]]):
        if not grid and len(grid) == 0:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        largest = 0
        memo = [[0 for _ in range(cols)] for _ in range(rows)]
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        def dfs(row,col):
            if memo[row][col] != 0 :
                ## have been visited
                ## not need back track , since we have memo to store that
                return memo[row][col]
            # memo[row][col] = 1 ## every searching, we have 1 means 1 order
            cur = 1
            for dir in dirs:
                new_row = row + dir[0]
                new_col = col + dir[1]
                if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] > grid[row][col]:
                    cur = max(cur,dfs(new_row,new_col) + 1 ) ## if they have a larger, so increasing 1
            memo[row][col] = cur

            return memo[row][col]

        for i in range(rows):
            for j in range(cols):
                if memo[i][j] == 0: ## not visted yet
                    largest = max(largest,dfs(i,j))

        return largest


## bfs todo test that
    class Solution:
        longest_path = 1
        def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
            self.ROWS, self.COLS = len(matrix), len(matrix[0])
            if self.ROWS == 0 and self.COLS == 0:
                return 0
            visited = [[0 for i in range(self.COLS)] for j in range(self.ROWS)]
            for i in range(self.ROWS):
                for j in range(self.COLS):
                    if visited[i][j] == 0:
                        self.BFS(matrix, i, j, visited)

            return self.longest_path

        def isSafe(self, i, j, visited, path_len):
            return self.ROWS > i >= 0 and self.COLS > j >= 0 and path_len > visited[i][j]

        def BFS(self, matrix, i, j, visited):
            queue = collections.deque()
            queue.append((i, j))
            path_len = 1

            while queue:
                path_len += 1
                n = len(queue)
                for _ in range(n):
                    x, y = queue.popleft()
                    for k in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        neighbor_x = x + k[0]
                        neighbor_y = y + k[1]
                        if self.isSafe(neighbor_x, neighbor_y, visited, path_len) and matrix[neighbor_x][neighbor_y] > \
                                matrix[x][y]:
                            visited[neighbor_x][neighbor_y] = path_len
                            queue.append((neighbor_x, neighbor_y))
                            self.longest_path = max(self.longest_path, path_len)

