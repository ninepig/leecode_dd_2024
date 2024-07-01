class UnionFind:
    def __init__(self,n):
        ## uf 可以在类里加很多东西做文章
        self.pa = [i for i in range(n)]
        self.count = n ## count 用来表示 cluster的数量
        self.size = [1 for _ in range(n)] ## 小岛类问题 面积 很少用到，可以维护联通量的面积

    def union(self,a,b):
        a_parent = self.find(a)
        b_parent = self.find(b)
        if a_parent == b_parent:
            return False
        if self.size[a_parent] > self.size[b_parent]:
            self.pa[b_parent] = a_parent
            self.size[a_parent] += self.size[b_parent]
        else:
            self.pa[a_parent] = b_parent
            self.size[b_parent] += self.size[a_parent]
        self.count -= 1
        return True

    def find(self,a):
        if self.pa[a] != a:
            self.pa[a] = self.find(self.pa[a])
        return self.pa[a]

    def isConnect(self,a,b):
        return self.find(a) == self.find(b)