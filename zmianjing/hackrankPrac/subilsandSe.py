import copy


class Solution:
    def countSubIsland(self, grid1, grid2):
        if not grid1 or not grid2:
            raise Exception("WRong input")
        ## other santity check ... size ..
        '''
        1 we remove island in grid2 not in grid1 first 
        2 we count island in grid2 now
        '''
        rows = len(grid2)
        cols = len(grid2[1])

        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(row, col):
            if grid2[row][col] == 0:
                return
            grid2[row][col] = 0  ## remove island

            for d in dirs:
                new_row = row + d[0]
                new_col = col + d[1]
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    dfs(new_row, new_col)

        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1 and grid1[i][j] == 0:
                    dfs(i, j)  ## remove island in grid2

        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1:
                    count += 1
                    dfs(i, j)  ## remove island in grid2

        return count

    def countSubIslandSize(self, grid1, grid2):
        rows = len(grid2)
        cols = len(grid2[1])

        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(row, col):
            if grid2[row][col] == 0:
                return
            grid2[row][col] = 0  ## remove island

            for d in dirs:
                new_row = row + d[0]
                new_col = col + d[1]
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    dfs(new_row, new_col)

        def size(row, col, grid):
            if grid[row][col] == 0:
                return 0
            grid[row][col] = 0  # set zero

            cur = 1
            for d in dirs:
                new_row = row + d[0]
                new_col = col + d[1]
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    cur += size(new_row, new_col, grid)

            return cur

        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1 and grid1[i][j] == 0:
                    dfs(i, j)  ## remove island in grid2

        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1:
                    tempGrid = copy.deepcopy(grid1)
                    parentSize = size(i, j, tempGrid)
                    currentSize = size(i, j, grid2)
                    if currentSize / parentSize * 100 >= 40.0:
                        count += 1

        return count

    def countSubIslandsSizeParentSizeHashmap(self, grid, grid1):

      rows = len(grid)
      cols = len(grid[0])
      dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

      ## remove island to 0 once we visited
      def dfs(row, col):
          if grid2[row][col] == 0:
              return
          grid2[row][col] = 0
          for dx, dy in dirs:
              new_row = dx + row
              new_col = dy + col
              if 0 <= new_row < rows and 0 <= new_col < cols:
                  dfs(new_row, new_col)

      def dfsParent(row, col,idx):
          if grid[row][col] != 1: # should not be 0, should be not equal to 1, since we will set grid to other idx
              return 0
          grid[row][col] = idx
          cur = 1
          for dx, dy in dirs:
              new_row = dx + row
              new_col = dy + col
              if 0 <= new_row < rows and 0 <= new_col < cols:
                  cur += dfsParent(new_row, new_col,idx)

          return cur
      def dfsGetSize(row,col,grid):
           if grid[row][col] == 0 :
               return 0
           grid[row][col] = 0
           cur = 1
           for dx,dy in dirs:
               new_row = dx + row
               new_col = dy + col
               if 0<= new_row < rows and 0 <= new_col < cols:
                   cur += dfsGetSize(new_row,new_col,grid)

           return cur


      island_idx = 2
      idx_size_dict = dict()
      ## step 1
      for i in range(rows):
          for j in range(cols):
              if grid2[i][j] == 1 and grid[i][j] == 0:
                  dfs(i, j)
              if grid[i][j] == 1:
                  size = dfsParent(i,j,island_idx)
                  idx_size_dict[island_idx] = size
                  island_idx += 1

      ## step2
      count = 0
      for i in range(rows):
          for j in range(cols):
              if grid2[i][j] == 1:
                  # grid_parent_temp = copy.deepcopy(grid)
                  size_parent = idx_size_dict[grid[i][j]] ## we set grid with islandidx, we get size by it idx
                  size_current = dfsGetSize(i,j,grid2)
                  # FollowUp: Count Sub Islands that are 40% a subset of the other grid
                  ## if we use this way, parent could already be moved, so we should do a
                  if size_current / size_parent * 100 >= 40.0:
                      count += 1
      return count


grid1 = [[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]]
grid2 = [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]
test = Solution()
print(test.countSubIsland(grid1, grid2))
print(test.countSubIslandSize(grid1, grid2))