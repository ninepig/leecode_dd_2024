class UnionFind:
    def __init__(self,n):
        # init forest
        self.fa = [i for i in range(n)]
        ## 增加了这个就能算出 uf之中count数
        self.count = n

    def find(self,x):
        while self.fa[x] != x:
            ## path compression, point to fa'fa in one loop, to reduce tree height
            self.fa[x] = self.fa[self.fa[x]]
            x = self.fa[x]
        return x

    def union(self,x,y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_y == root_x:
            return False # they belong same union

        # connect
        self.fa[root_x] = root_y
        self.count -= 1
        return True

    def is_connect(self,x,y):
        return self.find(x) == self.find(y)
