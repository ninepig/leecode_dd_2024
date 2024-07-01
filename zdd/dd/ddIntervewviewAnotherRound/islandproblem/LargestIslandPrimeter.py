'''
https://www.1point3acres.com/bbs/thread-1045497-1-1.html
这道题没给具体的。
应该是一个follow up 提及到周长问题
上班提可能是 subisland 按照他们出题的尿性
对于primeter 我们看他邻居有几个越界或者不是岛 这个dfs 是关键
'''


class solution:
    def islandPrimeter(self, grid:list[list[int]]):
        rows = len(grid)
        cols = len(grid[0])
        ans = 0
        def dfs(row,col): # using dfs to get primeter
            if not(0<=row< rows and 0 <= col < cols): ## out of bound , return 1
                return 1
            if grid[row][col] == 0 : # neighbout is water
                return 1
            if grid[row][col] == 2: # already visited
                return 0
            grid[row][col] = 2 # set that island to visted
            # if that is 1(island) , we keep dfs process
            return dfs(row + 1 ,col) + dfs(row -1 ,col) + dfs(row,col+1) +dfs(row,col -1 )

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    size = dfs(i,j)
                    ans = max(size,ans)

        return ans