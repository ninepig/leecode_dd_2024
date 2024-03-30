'''
Given an integer matrix, find the length of the longest path that have same values. The matrix has no boundary limits.
(like, Google Maps - see edit for context)

From each cell, you can either move to two directions: horizontal or vertical. You may NOT move diagonally or move outside of the boundary.

nums = [
[1,1],
[5,5],
[5,5]
]

Return 4 ( Four 5's).

这道题虽然说的是相同的value path，但实际上就是相同数的最大面积

'''
import math


class solution:
    def longestPathWithSameValue(self,grid:list[list[int]]):
        # use dfs to handle this question
        # since we have difference value, so can not levage it self to do memo work
        if not grid or len(grid) == 0:
            return 0
        max_value = -math.inf
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        def dfs(row,col):
            if visited[row][col]:
                return 0

            visited[row][col] = True

            left = 0
            if 0 <= row - 1 < rows and grid[row - 1][col] == grid[row][col]:
                left = dfs(row - 1 , col)

            right = 0
            if 0 <= row + 1 < rows and grid[row + 1][col] == grid[row][col]:
                right = dfs(row + 1 , col)

            up = 0
            if 0 <= col - 1 < cols and grid[row ][col - 1] == grid[row][col]:
                up = dfs(row , col - 1)

            down = 0
            if 0 <= col + 1 < cols and grid[row][col + 1] == grid[row][col]:
                down = dfs(row , col + 1)

            visited[row][col] = False ## need backtrack , so we can move up then move down

            return 1 + max(up,max(down,max(left,right)))

        for i in range(rows):
            for j in range(cols):
                max_value = max(max_value,dfs(i,j))

        return max_value



nums = [[7,5,6,6,6,6],[7,7,4,6,6,6],[7,7,1,2,3,6],[7,1,7,7,3,2],[7,7,7,7,7,1],[1,1,1,1,1,1]]
sol = solution()
print(sol.longestPathWithSameValue(nums))