'''
1 并查集
--》 遍历grid， 把岛合并在一起， 然后记录下size
--》 第二遍grid --》 如果grid xx = 1 不需要做任何事情， 因为无法改成岛
---》对于 海水， 计算四周岛屿size ， 全部累加， 计算最大
uf 的方法
https://leetcode.cn/problems/making-a-large-island/solutions/1830996/by-ac_oier-1kmp

'''
from collections import defaultdict
from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        prt, qrt = self.find(p), self.find(q)
        if prt == qrt: return False
        if self.rank[prt] > self.rank[qrt]: prt, qrt = qrt, prt
        self.parent[prt] = qrt
        self.rank[qrt] += self.rank[prt]
        return True


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)  # dimension
        uf = UnionFind(n * n)
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    ##只考虑左侧或者上边的
                    for (ii, jj) in (i - 1, j), (i, j - 1):
                        if 0 <= ii < n and 0 <= jj < n and grid[ii][jj]: uf.union(i * n + j, ii * n + jj)

        freq = defaultdict(int)
        for i in range(n * n): freq[uf.find(i)] += 1

        ans = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    ans = max(ans, freq[uf.find(i * n + j)])
                else:
                    cand = 1
                    seen = set()
                    for ii, jj in (i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j):
                        if 0 <= ii < n and 0 <= jj < n:
                            if grid[ii][jj]:
                                key = uf.find(ii * n + jj)
                                if key not in seen:
                                    seen.add(key)
                                    cand += freq[key]
                    ans = max(ans, cand)
        return ans

'''
dfs 版本
1 同样 先计算每个小岛的面积 （dfs） ， 记录
2 对于 海水区域， 计算四周小岛的面积
3 计算最大面积
这个做法太复杂了 要写得简化一点
## 计算四周的面积， 中间利用到最早的那个dict， 得到 idx: size， 看看四周是不是属于1个岛 自己写下 

https://leetcode.cn/problems/making-a-large-island/solutions/790816/827zui-da-ren-gong-dao-python3-shi-yong-wwkd5
'''
class Solution2:
    def largestIsland(self, grid):
        if not grid or len(grid) == 0:
            raise Exception("Wrong input")
        rows = len(grid)
        cols = len(grid[0])
        idx = 2  ## starting idx is 2
        idx_size_dict = dict()
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        ## get size of orignal grid and coloring grid with island idx
        def getSize(row, col, idx):
            if grid[row][col] == 0:
                return 0  ## water
            elif grid[row][col] != 1:  # vistied
                return 0
            grid[row][col] = idx
            size = 1
            for dx, dy in dirs:
                x = row + dx
                y = col + dy
                if 0 <= x < rows and 0 <= y < cols:
                    size += getSize(x, y, idx)

            return size

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    size = getSize(i, j, idx)
                    idx_size_dict[idx] = size
                    idx += 1

        # flip 0 to 1
        max_size = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 0:
                    max_size = max(max_size, idx_size_dict[grid[i][j]])
                elif grid[i][j] == 0:
                    curSize = 1
                    neigh_dict = dict()
                    for dx, dy in dirs:
                        x = i + dx
                        y = j + dy
                        if 0 <= x < rows and 0 <= y < cols:
                            neigh_idx = grid[x][y]
                            neigh_area = 0
                            if neigh_idx in idx_size_dict:
                                neigh_area = idx_size_dict[neigh_idx]

                            if neigh_idx not in neigh_dict:
                                neigh_dict[neigh_idx] = neigh_area

                    curSize += sum(neigh_dict.values())
                    max_size = max(max_size, curSize)

        return max_size


if __name__ == "__main__":
    input = [[1,1],[1,1]]
    sol = Solution2()
    print(sol.largestIslandWenjing(input))