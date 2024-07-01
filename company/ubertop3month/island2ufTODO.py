from itertools import pairwise
from typing import List


## 这个题是每一个操作以后 能有多少小岛
## 利用uf 来做。 uf 有memo 来记录有多少连通分量。

class UnionFind:
    def __init__(self, n: int):
        self.p = list(range(n))
        self.size = [1] * n

    def find(self, x: int):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a: int, b: int) -> bool:
        pa, pb = self.find(a - 1), self.find(b - 1)
        if pa == pb:
            return False
        if self.size[pa] > self.size[pb]:
            self.p[pb] = pa
            self.size[pa] += self.size[pb]
        else:
            self.p[pa] = pb
            self.size[pb] += self.size[pa]
        return True


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf = UnionFind(m * n)
        grid = [[0] * n for _ in range(m)]
        ans = []
        dirs = (-1, 0, 1, 0, -1)
        cnt = 0
        for i, j in positions:
            if grid[i][j]:
                ans.append(cnt)
                continue
            grid[i][j] = 1
            cnt += 1
            for a, b in pairwise(dirs):
                x, y = i + a, j + b
                if (0 <= x < m and 0 <= y < n and grid[x][y] and uf.union(i * n + j, x * n + y)):
                    cnt -= 1
            ans.append(cnt)
        return ans


class uf:
    def __init__(self,size):
        self.size = [1 for _ in range(size)]
        self.pa = [i for i in range(size)]

    def find(self,n):
        if self.pa[n] != n:
            self.pa[n] = self.find(self.pa[n])

        return self.pa[n]

    def union(self,a,b):
        parent_a = self.find(a)
        parent_b = self.find(b)
        if parent_a == parent_b:
            return False
        if self.size[parent_a] >= self.size[parent_b]:
            self.pa[parent_b] = parent_a
            self.size[parent_a] += self.size[parent_b]
        else:
            self.pa[parent_a] = parent_b
            self.size[parent_b] += self.size[parent_a]

        return  True

class Solution2:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        '''
        in inital --> 0s grid
        in each pos, we flip that to 1
        in pos loop
        if grid is already 1, we add to result
        if grid is not 1 , we try to flip
        count + 1, but we need check if that union to 4 dirs to form island
        对于这个题 uf的作用就是连接起来
        '''
        union_find = uf(m*n)
        cnt = 0
        dirs = [-1,0,1,0,-1]
        res = []
        grid = [[0 for _ in range(n)] for _ in range(m)]

        for row,col in positions:
            if grid[row][col] : ## already be an island
                res.append(cnt)
                continue
            grid[row][col] = 1
            cnt += 1
            for x,y in pairwise(dirs):
                new_row , new_col = row + x , col + y
                uf_fisrt = row*m + col -1
                uf_second = new_row*m + new_col - 1
                if 0<= new_row < m and 0 <= new_col < n and grid[new_row][new_col] and union_find.union(uf_fisrt,uf_second):
                    cnt -= 1
            res.append(cnt)

        return res





















