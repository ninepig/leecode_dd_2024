class uf:
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
            return False # in same connection

        self.fa[root_x] = root_y #x 的根节点连接到 y 的根节点上，成为 y 的根节点的子节点
        return True

    def is_connected(self,x,y):
        return self.find(x) == self.find(y)