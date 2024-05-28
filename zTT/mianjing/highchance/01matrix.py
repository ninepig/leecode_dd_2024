'''
从0出发 到各个点
'''
import collections
from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        M, N = len(matrix), len(matrix[0])
        queue = collections.deque()
        visited = [[0] * N for _ in range(M)]
        res = [[0] * N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    queue.append((i, j))
                    visited[i][j] = 1
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        step = 0
        while queue:
            size = len(queue)
            for i in range(size):
                x, y = queue.popleft()
                if matrix[x][y] == 1:
                    res[x][y] = step
                for dx, dy in dirs:
                    newx, newy = x + dx, y + dy
                    if newx < 0 or newx >= M or newy < 0 or newy >= N or visited[newx][newy] == 1:
                        continue
                    queue.append((newx, newy))
                    visited[newx][newy] = 1
            step += 1
        return res

# 作者：负雪明烛
# 链接：https://leetcode.cn/problems/01-matrix/solutions/203364/tao-lu-da-jie-mi-gao-dong-ti-mu-kao-cha-shi-yao-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。