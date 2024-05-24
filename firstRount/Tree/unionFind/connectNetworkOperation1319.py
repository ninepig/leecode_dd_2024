'''
n 台计算机通过网线连接成一个网络，计算机的编号从 0 到 n - 1。线缆用 comnnections 表示，其中 connections[i] = [a, b] 表示连接了计算机 a 和 b。

给定这个计算机网络的初始布线 connections，可以拔除任意两台直接相连的计算机之间的网线，并用这根网线连接任意一对未直接连接的计算机。
现在要求：计算并返回使所有计算机都连通所需的最少操作次数。如果不可能，则返回 -1。
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
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        remove_count = 0
        need_count = n - 1
        uf = UF(n)
        # for connection in connections:
        #     if uf.is_connect(connection[0],connection[1]):
        #         remove_count += 1
        #     else:
        #         need_count -= 1
        #         uf.union(connection[0],connection[1])
        for connection in connections:
            if uf.union(connection[0], connection[1]):
                need_count -= 1
            else:
                remove_count += 1

        if remove_count < need_count:
            return -1

        return need_count
