class FenwickTree:
    def __init__(self,n):
        self.size = n
        self.tree =[0 for _ in range(n + 1)]

    def __lowbit(self,index):
        return index & (-index)

    def update(self,index ,delta):

        while index <= self.size :
            self.tree[index] += delta
            index += self.__lowbit(index)

    def query(self,index):
        res = 0

        while index > 0 :
            res += self.tree[index]
            index -= self.__lowbit(index)

        return res