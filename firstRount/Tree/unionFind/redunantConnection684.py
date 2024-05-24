class UF:
    def __init__(self,n):
        self.fa = [i for i in range(n)]

    def find(self,x):
        while x != self.fa[x]:
            self.fa[x] = self.fa[self.fa[x]]
            x = self.fa[x]
        return x

    def union(self,x,y):
        root_X = self.find(x)
        root_y = self.find(y)
        if root_y == root_X : return False
        self.fa[root_X] = root_y
        return True

    def is_conenct(self,x,y):
        return self.find(x) == self.find(y)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        size = len(edges)
        uf = UF(size)
        for edge in edges:
            if uf.is_conenct(edge[0],edges[1]):
                return edge
            uf.union(edge[0],edge[1])

        return None
