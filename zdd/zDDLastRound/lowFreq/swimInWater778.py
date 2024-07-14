import heapq
from typing import List

'''
柒柒巴 问题背景改了一下 不是游泳 而是dasher要从top left (0, 0) 到 bottom right (n - 1, n - 1)
利用最小pq， 不断把栈顶最小可以达到所需要的value 弹出，然后看他四周的位置。再入栈 最终更新最大值
需要最大的时间 到达某个点至少需要多少时间。 这样用pq来做
'''

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        res = 0
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]
        visited = set()
        visited.add((0,0))

        while heap:
            height, x, y = heapq.heappop(heap)
            res = max(res, height)
            if x == n - 1 and y == n - 1:
                return res

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < n and 0 <= new_y < n and (new_x, new_y) not in visited:
                    visited.add((new_x, new_y))
                    heapq.heappush(heap, (grid[new_x][new_y], new_x, new_y))

        return -1

