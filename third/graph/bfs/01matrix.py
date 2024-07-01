'''
https://leetcode.com/problems/01-matrix/description/

这个题找每个格子到达目标的距离。
一般这种题 都可以考虑从目标点出发。 往回走 这样每次反向遍历得时候就可以不断记录答案
类似 dd的经典饭店题之类的
如果把step放在 queue之中， 就不需要在bfs之中考虑循环
'''
import collections
from typing import List


class Solution:
    ## 这道题自己写错了，
    ## 因为这道题 你找了1 ，你还要继续走下去
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or len(mat) == 0 : return [] ## sanity check
        rows = len(mat)
        cols = len(mat[0])
        res = [[0 for _ in range(cols)] for _ in range(rows)]
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        deque = collections.deque() ## starting from each 0 point , using deque
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    deque.append((i,j,0))
                    visited[i][j] = True
        dirs = [(0,1),(0,-1),(-1,0),(1,0)]
        ## we cal shortest for all, so that is mult souce problem, so we put all 0 into queue first
        while deque:
            row,col,step = deque.popleft()
            for dir in dirs:
                new_row = row + dir[0]
                new_col = col + dir[1]
                if 0<= new_row < rows and 0 <= new_col < cols and not visited[new_row][new_col]:
                    if mat[new_row][new_col] == 1 : ## we found start point
                        visited[new_row][new_col] = True
                        res[new_row][new_col] = step + 1
                        ## 我们需要继续走下去 ，而不是停止，因为就算找到了1，
                        # 因为1 不是blocker 你还需要考虑继续走下去的情况， 再入栈就行了
                        deque.append((new_row, new_col, step + 1))
                    else:
                        visited[new_row][new_col] = True
                        deque.append((new_row,new_col,step + 1))

        return res

    def updateMatrix2(self, matrix: List[List[int]]) -> List[List[int]]:
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