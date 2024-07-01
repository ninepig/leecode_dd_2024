'''

题目的场景套了一个送快递的外衣，但是本质是
给两个相同size的2D array，只含有0和1，所有相邻（4-ways）的1组成一块地方称之为area。举个例子
a= [[1,1,1,0,0,0],
 [0,0,1,1,1,1],
[0,0,0,0,0,0],

 [1,0,1,0,0,0],
 [0,1,0,1,1,0]]
b= [[1,1,1,0,0,0],
 [0,0,1,1,1,1],
 [0,1,0,0,0,0],
 [1,0,1,1,0,0],
 [0,1,0,1,1,0]]
b里面有5个unique的area，对于b的这5个area，如果一个area在a中对应的所有位置[i, j]的值也都是1的话，我们称之为valid。否则就是invalid。
求b一共有多少个valid的area。对于这个例子，答案是3
 https://leetcode.com/discuss/interview-question/4855144/DoorDash-or-Senior-Software-Engineer-or-Feb-2024
 https://www.1point3acres.com/bbs/thread-1042019-1-1.html
 这道题应该是subisland的变种题

1 follow up
  get 40% size of island
'''
import copy
from typing import List


class Solution:
    def countSubIslands(self, grid: List[List[int]], grid2: List[List[int]]) -> int:
        '''
        1 remove island in grid2 but not in grid1--> so that is not subisland
        2 count left island in grid2
        '''
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]

        ## remove island to 0 once we visited
        def dfs(row,col):
            if grid2[row][col] == 0 :
                return
            grid2[row][col] = 0
            for dx,dy in dirs:
                new_row = dx + row
                new_col = dy + col
                if 0<= new_row < rows and 0 <= new_col < cols:
                    dfs(new_row,new_col)

        ## step 1
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1 and grid[i][j] == 0 :
                    dfs(i,j)

        ## step2
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1:
                    dfs(i,j)
                    # FollowUp: Count Sub Islands that are 40% a subset of the other grid
                    count += 1

        return count

    # FollowUp: Count Sub Islands that are 40% a subset of the other grid
    def countSubIslandsSize(self, grid: List[List[int]], grid2: List[List[int]]) -> int:
        '''
        1 remove island in grid2 but not in grid1--> so that is not subisland
        2 count left island in grid2
        followup
        1用deepcopy 来复制grid 用来避免 多次计算parent grid 被干扰

        '''
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

        ## step 1
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1 and grid[i][j] == 0:
                    dfs(i, j)
                    # grid_parent_temp = copy.deepcopy(grid)
        ## step2
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1:
                    ## using a deep copy to get a new grid so it won't affect next round
                    grid_parent_temp = copy.deepcopy(grid)
                    # print(grid)
                    # print(grid2)
                    size_parent = dfsGetSize(i,j,grid_parent_temp)
                    # print("parent" + str(size_parent))
                    size_current = dfsGetSize(i,j,grid2)
                    # print("current" + str(size_current))
                    # FollowUp: Count Sub Islands that are 40% a subset of the other grid
                    ## if we use this way, parent could already be moved, so we should do a
                    if size_current / size_parent * 100 >= 40.0:
                        count += 1

        return count

    def countSubIslandsSizeParentSize(self, grid, grid1):
      '''
      1 remove island in grid2 but not in grid1--> so that is not subisland
      2 count left island in grid2
      followup
      2 换一个方法--》 给parent里小岛一个编号，然后维护一个编号--》size的dict。 这样每次用grid[i][j]得到的就是小岛的编号
      '''
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



grid1 =[[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]

grid3 =[[1,1,1,0,0],
        [0,1,1,1,1],
        [0,0,0,0,0],
        [1,0,0,0,0],
        [1,1,0,1,1]]
grid4 = [[1,1,1,0,0],
         [0,0,1,1,1],
         [0,1,0,0,0],
         [1,0,1,1,0],
         [0,1,0,1,0]]

test = Solution()
# print(test.countSubIslands(grid1,grid2))
print(test.countSubIslandsSize(grid3,grid4))
print(test.countSubIslandsSizeParentSize(grid3,grid4))