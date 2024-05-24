
class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.count = n

    def find(self,x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self,x,y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_y == root_x:
            return False
        self.parent[x] = y
        self.count -= 1
        return True

    def is_union(self,x,y):
        return self.find(x) == self.find(y)

'''这道题构建边的方法好像更简单点
因为这个不是一个matrix, 而是空间之中多个点'''
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        arr = []
        n = len(points)
        # 构建边
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                arr.append([i, j, abs(x2 - x1) + abs(y2 - y1)])
        # 排序
        arr.sort(key=lambda x: x[2])
        # 并查集
        parent = list(range(n))

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        # 构建最小生成树
        edge = 0
        cost = 0
        for i, j, d in arr:
            a, b = find(i), find(j)
            if a != b:
                parent[b] = a
                edge += 1
                cost += d
            if edge == n - 1:
                break
        return cost
