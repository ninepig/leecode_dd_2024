import collections


class Solution2:
    '''
    1 callting each island's size and store idx of island  to orginal island
    2 store idx --> size to a map
    3 we need duplicated orignal grid for another round search
    4 when grid is 1 , we check size , when grid is 0, we cound the surranding island size



    '''
    def largestMakingIsland(self, grid: List[List[int]]) -> int:

        # 1 cal the island size and store info
        temp_grid = grid
        rows = len(grid)
        cols = len(grid[0])
        idx_size_dict = collections.defaultdict(int) ## default idx size will be 0
        idx = 2 ## 1 means island , 0 means sea
        ## use temp_grid to do dfs, use idx number as visited map

        def dfs(row,col,idx):
            if not ( 0 <= row < rows and 0 <= col < cols):
                ## out of bound
                return 0
            if temp_grid[row][col] != 1: # not island
                return 0
            temp_grid[row][col] = idx ## set this island to island idx
            return (1 + dfs(row + 1 ,col) + dfs(row - 1,col)
                    + dfs(row, col + 1) + dfs(row,col - 1))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 :## starting from island
                    cur_size = dfs(i,j,idx)
                    idx_size_dict[idx] = cur_size ## store size in to area dict
                    idx+=1 ## once we finished 1 island, need add idx

        if max(idx_size_dict.values()) == 0:
            return 1 ## no island

        if max(idx_size_dict.values()) == rows * cols :
            return rows*cols ## max island size

        #2 we flip 0 to 1 to make island

        ans = 0
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 : ##no way to flip, get it is idx and size
                    target_size = idx_size_dict[temp_grid[i][j]] ## get island idx --> size
                    ans = max(target_size,ans)
                else: ## flip island, final result equals current plus surrunding
                    cur = 1
                    neighbour_neighbour = dict()
                    ## check surrunding size
                    for dir in dirs:
                        new_row = i + dir[0]
                        new_col = j + dir[1]
                        if 0 <= new_row < rows and 0 <= new_col < cols : ## inside of island
                            if temp_grid[new_row][new_col] in idx_size_dict: ## if we have that size stored
                               cur_idx =temp_grid[new_row][new_col]
                               if cur_idx not in neighbour_neighbour: # if neighbour belong to different idx
                                   neighbour_neighbour[cur_idx] = idx_size_dict[cur_idx] ## store neighbour's size
                    cur += sum(neighbour_neighbour.values())
                    ans = max(ans, cur)

        return ans







