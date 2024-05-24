'''
描述：给定一个由字符串方程组成的数组 equations，每个字符串方程 equations[i] 的长度为 4，有以下两种形式组成：a==b 或 a!=b。a 和 b 是小写字母，表示单字母变量名。

要求：判断所有的字符串方程是否能同时满足，如果能同时满足，返回 True，否则返回 False

a != b a == b
'''

'''
标准的uf题
a == b 的时候 说明联通
全部走一遍
再看 x != y 看是否 x y 联通 如果联通 false
'''


class UF:
    # n is the size of uf , in this case, we can use 26
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

    def isConnect(self,x,y):
        return  self.find(x) == self.find(y)


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UF(26)
        for eq in equations:
            if eq[1] == '=':
                index1 = ord(eq[0]) - 97
                index2 = ord(eq[3]) - 97
                uf.union(index1,index2)

        for eq in eq:
            if eq[1] =='!':
                index1 = ord(eq[0]) - 97
                index2 = ord(eq[3]) - 97
                uf.union(index1,index2)
                if not uf.isConnect(index1,index2):
                    return False

        return True
