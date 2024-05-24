'''
描述：二维平面中有
 块石头，每块石头都在整数坐标点上，且每个坐标点上最多只能有一块石头。如果一块石头的同行或者同列上有其他石头存在，那么就可以移除这块石头。

要求：返回可以移除的石子的最大数量。

UF 应用题
关键是把 二维映射为1维

最多可以移走的石头数目 = 所有石头个数 - 最少可以留下的石头（并查集的集合个数）
'''

class UnionFind:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.count = n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return

        self.parent[root_x] = root_y
        self.count -= 1

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        size = len(stones)
        n = 10100
        uf =UnionFind(2*n)
        for i in range(size):
            uf.union(stones[i][0],stones[i][1] + 10000)

        stones_set = set()
        for i in range(size):
            stones_set.add(uf.find(stones[i][0]))

        return size -  len(stones_set)