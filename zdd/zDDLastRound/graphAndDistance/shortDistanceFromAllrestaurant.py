
'''
从每个building出发 对每个点更新距离 以及可以达到的酒店数量
bfs 来做 不需要构图
'''
import collections
import math

## good!
## 这个题就是 dashmart的后半部分。
class solution:
    def shortestDistance(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = collections.deque()
        ## count , dist to record each point 's island/ distance
        count = [[0 for _ in range(cols)] for _ in range(rows)]
        dist = [[0 for _ in range(cols)] for _ in range(rows)]
        total = 0 # record for how many restuant in map

        ## only 0 can be road and our target
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    total += 1
                    queue.clear() ## we start from each restaunt
                    visited = set()
                    queue.append((i,j,0))
                    visited.add((i,j))
                    while queue:
                        cur = queue.popleft()
                        cur_x, cur_y ,cur_dis = cur[0],cur[1], cur[2]
                        for dir in dirs:
                            new_x = cur_x + dir[0]
                            new_y = cur_y + dir[1]
                            if 0<= new_x < rows and 0 <= new_y < cols and (new_x,new_y) not in visited and grid[new_x][new_y] == 0:
                                visited.add((new_x,new_y))
                                count[new_x][new_y] += 1
                                dist[new_x][new_y] += cur_dis + 1
                                queue.append((new_x,new_y,cur_dis + 1))

        ## after all visited
        ## we check each's distance, count
        min_distance = math.inf
        # res = [] ## if we need answer, use res array ,
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0 and count[i][j] == total: ## point can reach all restuant
                    if dist[i][j] < min_distance:
                        min_distance = dist[i][j]
                    #     res.clear()
                    # res.append((i,j))

        return min_distance

sol = solution()
test = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
print(sol.shortestDistance(test))