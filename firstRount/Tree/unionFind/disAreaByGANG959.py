'''经典集合题
利用union find
一定要画图做, index之间的关系也需要画图
https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0959.%20%E7%94%B1%E6%96%9C%E6%9D%A0%E5%88%92%E5%88%86%E5%8C%BA%E5%9F%9F.md
'''
class UF:
    def __init__(self,n):
        self.fa = [i for i in range(n)]
        self.count = n

    def find(self,x):
        while x != self.fa[x]:
            self.fa[x] = self.fa[self.fa[x]]
            x = self.fa[x]
        return x

    def union(self,x,y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_y == root_x : return False
        self.fa[root_x] = root_y
        self.count -= 1

    def isConnect(self,x,y):
        return self.find(x) == self.find(y)

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        length = len(grid)
        size = 4 * length*length
        uf = UF(size)
        for i  in range(size):
            for j in range(size):
                ch = grid[i][j] # 当前格子的符号
                index = 4*(i*size + j) # 画个图就明白了
                ## 区块内部
                if ch == '/':
                    uf.union(index , index + 1)
                    uf.union(index + 2, index + 3)
                elif ch == '\\':
                    uf.union(index + 1 , index + 2)
                    uf.union(index , index + 3)
                else:
                    uf.union(index, index + 1)
                    uf.union(index+ 1, index + 2)
                    uf.union(index + 2, index + 3)
                ## 连接2个区块
                if j + 1 < size:
                    uf.union(index + 2 , index + 4)
                if i + 1 < size:
                    uf.union(index + 3 , index + 4 * size + 1) #这个一定要画图做

        return uf.count