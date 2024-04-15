import collections
import math


class Solution:
    def shortestPathFromALLbuilding(self, grid):
        ## santity check
        if not grid or len(grid) == 0:
            raise Exception("wrong input")
        '''
        we need a memo table record each point , how many building can arrivve , 
        another table recoed each point , path from build to arrive
        bfs from each building , record these two value 
        '''
        rows = len(grid)
        cols = len(grid[0])
        ## TODO BUG 用了array 下面的就要用array 而不是tuble
        build_dict = [[0 for _ in range(cols)] for _ in range(rows)]
        distance_dict = [[0 for _ in range(cols)] for _ in range(rows)]
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        building_count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    q = collections.deque()
                    ## 0 mean's distance so far
                    q.append((i, j, 0))
                    visited = set()
                    visited.add((i, j))
                    building_count += 1
                    while q:
                        cur_x, cur_y, dis = q.popleft()
                        for d in dirs:
                            new_x = cur_x + d[0]
                            new_y = cur_y + d[1]
                            if 0 <= new_x < rows and 0 <= new_y < cols and (new_x, new_y) not in visited:
                                if grid[new_x][new_y] == 0:  ## means can pass
                                    visited.add((new_x, new_y))
                                    ## 用array 不是tuble
                                    build_dict[new_x][new_y] += 1
                                    distance_dict[new_x][new_y] += dis + 1
                                    q.append((new_x, new_y, dis + 1))

        min_distance = math.inf

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0 and build_dict[i][j] == building_count:
                    min_distance = min(min_distance, distance_dict[i][j])

        return min_distance


sol = Solution()
test = [[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
print(sol.shortestPathFromALLbuilding(test))
