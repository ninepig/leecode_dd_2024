class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows = len(grid1)
        cols = len(grid1[0])
        res = 0
        dirctions = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(row,col):
            is_sub = True
            # 只有grid2 是1的时候才会进行比较， 这个dfs的核心真的挺难想的 非常牛逼
            if 0 <= row < rows and 0<= col < cols and grid2[row][col] == 1:
                if grid1[i][j] != 1:
                    is_sub = False
                    for dirct in dirctions:
                        new_row = row + dirct[0]
                        new_col = col + dirct[1]
                        is_sub &= dfs(new_row,new_col)

            return is_sub


        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1: # start from grid2
                    res += dfs(i,j)

        return res