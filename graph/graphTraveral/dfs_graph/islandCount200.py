'''
描述：给定一个由字符 '1'（陆地）和字符 '0'（水）组成的的二维网格
。
要求：计算网格中岛屿的数量。
'''
from LinkedList import List


class Solution:
    def dfs(self, grid, i, j, m, n):
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == '0':
            return
        # dfs的任务就是把联通的置0
        grid[i][j] = '0'
        self.dfs(grid,i + 1 , j , m , n)
        self.dfs(grid,i - 1 , j , m , n)
        self.dfs(grid,i , j + 1 , m , n)
        self.dfs(grid,i, j - 1 , m , n)

    '''对于任何1 来说 dfs把它可以链接的岛找出来, 然后置为0,+1, 最终统计多少有多少岛'''
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[m][n] == '1':
                    self.dfs(grid,i,j,m,n)
                    count += 1

        return count