import collections

'''自己做的多考虑了visit
不需要 因为我们可以用原数组来处理'''
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        queue = collections.deque([])
        # visited = set() #不需要visited , 因为 用1 来取代了
        length = len(grid)
        width = len(grid[0])
        ans = 0
        for i in range(length):
            for j in range(width):
                if grid[i][j] == 1:
                    queue.append((i,j))
                    grid[i][j] = 0
                    # visited.add((i,j))
                    size = 1
                    while queue:
                        cur = queue.popleft()
                        for direction in directions:
                            new_x = cur[0] + direction[0]
                            new_y = cur[1] + direction[1]
                            # if 0<= new_x < length and 0 <= new_y < width and (new_x,new_y) not in visited and grid[i][j] == 1:
                            if 0 <= new_x < length and 0 <= new_y < width and grid[i][j] == 1:
                                queue.append((new_x,new_y))
                                # visited.add((new_x,new_y))
                                size += 1
                                grid[i][j] = 0
                    ans = max(ans,size)

        return ans

    def maxAreaOfIslandAnswer(self, grid: List[List[int]]) -> int:
        directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(grid), len(grid[0])
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    temp_ans = 1
                    queue = collections.deque([(i, j)])
                    while queue:
                        i, j = queue.popleft()
                        for direct in directs:
                            new_i = i + direct[0]
                            new_j = j + direct[1]
                            if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols or grid[new_i][new_j] == 0:
                                continue
                            grid[new_i][new_j] = 0
                            queue.append((new_i, new_j))
                            temp_ans += 1

                    ans = max(ans, temp_ans)
        return ans