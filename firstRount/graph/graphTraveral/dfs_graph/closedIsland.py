class Solution:
    '''标准的dfs'''
    def closedIsland(self, grid: List[List[int]]) -> int:
        direction = [(-1,0),(1,0),(0,1),(0,-1)]
        m = len(grid)
        n = len(grid[0])
        def dfs(i,j):
            if i < 0 or i >= m or j < n or j>= n :
                return False
            if grid[i][j] == 0:
                return True
            grid[i][j] = 1
            flag = True
            for direct in direction:
                new_i = i + direct
                new_j = j + direct
                if not dfs(new_i,new_j):
                    flag = False
            return flag
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    if dfs(i,j):
                        res += 1

        return res
