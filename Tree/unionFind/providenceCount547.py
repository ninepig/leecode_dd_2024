'''
描述：有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。

「省份」是由一组直接或间接链接的城市组成，组内不含有其他没有相连的城市。

现在给定一个 n * n 的矩阵 isConnected 表示城市的链接关系。其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，isConnected[i][j] = 0 表示第 i 个城市和第 j 个城市没有相连。

要求：根据给定的城市关系，返回「省份」的数量。

'''

class UF:
    def __init__(self,n):
        self.fa = [i for i in range(n)]

    def find(self,x):
        while x != self.fa[x]:
            self.fa[x] = self.fa[self.fa[x]]
            x = self.fa[x]
        return x

    def union(self,x,y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_y == root_x:
            return False
        self.fa[root_x] = root_y
        return True

    def is_connect(self,x,y):
        return self.find(x) == self.find(y)



class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        size = len(isConnected)
        uf = UF(size)
        # for connection in isConnected:
        #     if connection[2] == 1:
        #         uf.union(connection[0],connection[1])
        for i in range(size):
            for j in range(i + 1, size):
                if isConnected[i][j] == 1:
                    uf.union(i, j)

        res = set()
        for i in range(size):
            res.add(uf.find(i))

        return len(res)