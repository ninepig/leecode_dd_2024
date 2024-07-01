## 这个题和leetcode 不一样 因为要计算所有岛最大的  leetcode是单个岛 所以需要dfs
## 对于一个1的小岛， 他边上有几个0 就能贡献几个周长
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