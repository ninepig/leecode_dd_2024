class uf:
    def __init__(self, size: int):
        self.fa = [i for i in range(size)]
        self.count = size

    #path compress way to boost find process
    def find(self,x:int):
        while self.fa[x] != x:
            self.fa[x] = self.fa[self.fa[x]]
            x = self.fa[x]
        return x

    def union(self, x:int, y:int):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_y == root_x:
            return False # they already in same union
        self.fa[root_x] = root_y
        self.count -= 1
        return True


    def is_connected(self,x:int,y:int):
        return self.find(x) == self.find(y)