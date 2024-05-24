class Solution:
    ## 这个bfs + 多维度 非常好玩
    '''
    电面 国人 题目分两步 以尔🍷潵 第一步简单的BFS 从（0，0）出发知道走到 row -1， col-1的位置的最少步骤 0代表可以走 1代表不可以通过, 如果走不到最终位置 返回-1
    电商组
    https://www.1point3acres.com/bbs/thread-1064194-1-1.html

    1293的变形题，先是没有elimination，然后follow up加入k eliminations。求加米看帖！
    
    '''
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 0

        k = min(k, m + n - 3)
        visited = set([(0, 0, k)])
        q = collections.deque([(0, 0, k)])

        step = 0
        while len(q) > 0:
            step += 1
            cnt = len(q)
            for _ in range(cnt):
                x, y, rest = q.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[nx][ny] == 0 and (nx, ny, rest) not in visited:
                            if nx == m - 1 and ny == n - 1:
                                return step
                            q.append((nx, ny, rest))
                            visited.add((nx, ny, rest))
                        elif grid[nx][ny] == 1 and rest > 0 and (nx, ny, rest - 1) not in visited:
                            q.append((nx, ny, rest - 1))
                            visited.add((nx, ny, rest - 1))
        return -1


# 作者：力扣官方题解
# 链接：https: // leetcode.cn / problems / shortest - path - in -a - grid -
# with-obstacles - elimination / solutions /
#     来源：力扣（LeetCode）
#     著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。