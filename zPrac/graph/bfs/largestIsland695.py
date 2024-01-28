import collections
'''
自己写一下
'''
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(grid), len(grid[0])
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    temp_ans = 1
                    q = collections.deque([(i, j)])
                    while q:
                        i, j = q.popleft()
                        for direct in directs:
                            new_i = i + direct[0]
                            new_j = j + direct[1]
                            if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols or grid[new_i][new_j] == 0:
                                continue
                            grid[new_i][new_j] = 0
                            q.append((new_i, new_j))
                            temp_ans += 1

                    ans = max(ans, temp_ans)
        return ans

    def maxAreaOfIslandPrac(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        ans = 0
        queue = collections.deque([])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    ## missing this step
                    grid[i][j] = 0
                    queue.append((i,j))
                    size = 1
                    while queue:
                        cur_i,cur_j = queue.popleft()
                        for dir in dirs:
                            new_i = cur_i + dir[0]
                            new_j = cur_j + dir[1]
                            if new_i < 0 or new_i >= rows or new_j <0 or new_j >= cols or grid[new_i][new_j] == 0:
                                continue
                            grid[new_i][new_j] = 0
                            queue.append((new_i,new_j))
                            size += 1
                    ans = max(size,ans)
        return ans