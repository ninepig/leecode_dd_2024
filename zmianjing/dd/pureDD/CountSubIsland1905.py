from typing import List


class Solution:
    '''dfs 来做
    对于grid2 上下左右移动，同时需要满足在grid 1之中满足条件 才可以算是+1'''
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # visit1 = [[False for _ in range(grid1)] for _ in range(grid1[0]) ]
        # visit2 = [[False for _ in range(grid2)] for _ in range(grid2[0]) ]no need, we use it self as set
        res = 0
        rows =len(grid1)
        cols = len(grid1[0])

        # 利用一个flag 作为返回的形式, 这个flag 可以根据上下左右的结果发生变化。 小技巧
        def dfs(x, y):
            isSubIsland = True
            if 0 <= x < rows and 0 <= y < cols and grid2[x][y] == 1:
                if grid1[x][y] != 1: return False
                grid2[x][y] = -1
                for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    isSubIsland &= dfs(x + dx, y + dy)
            return isSubIsland

        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1: # starting from any 1
                    if dfs(i,j):
                        res += 1
        return res
    

    # 自己的做法挺接近的了 加油！
    # def dfs(self,row, col,rows, cols,  grid1, grid2):
    #     flag = True
    #     if row < 0 or col >= cols or col < 0 or row >= rows:
    #         return False
    #     if grid2[row][col] == 1 and grid1[row][col] != 1:
    #         return False
    #     if (0 <= row < rows - 1 and 0 <= col < cols - 1
    #             and grid1[row][col] == 1 and grid2[row][col] == 1):
    #         # grid1[row][col] = -1
    #         grid2[row][col] = -1
    #
    #         flag = (self.dfs(row + 1,col,rows,cols,grid1,grid2) and self.dfs(row - 1, col, rows, cols, grid1, grid2)
    #                 and self.dfs(row , col + 1, rows, cols, grid1, grid2) and
    #                 self.dfs(row, col - 1, rows, cols, grid1, grid2))
    #
    #     return flag



