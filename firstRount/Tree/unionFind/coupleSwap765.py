# https://leetcode.com/problems/couples-holding-hands/solutions/117520/java-union-find-easy-to-understand-5-ms/
'''
Each component is a cyclic permutation. Let's assume there are n1 nodes in C1 component, n2 nodes in C2 component and so on.
Total number of nodes N = n1 + n2 + ... nk
To resolve 1 connected component with d nodes will take d-1 swaps.
So, to resolve components C1, C2, .. Ck we require Total Swaps = (n1 - 1) + (n2 - 1) + ... (nk - 1)
Total swaps = (n1 + n2 + .. nk) - (1 + 1 + ... k times) = N - k
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
        if root_y == root_x :
            return False
        self.fa[root_x] = root_y
        return True
    def is_connect(self,x,y):
        return self.find(x) == self.find(y)

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        size =len(row)
        uf = UF(size)
        couple = size / 2
        cycle = couple

        for i in range(0,size,2):
            # check if couples has been in same cycle
            if uf.union(row[i]//2 , row[i+1]//2):
                cycle -= 1
        #to resolve components C1, C2, .. Ck we require Total Swaps = (n1 - 1) + (n2 - 1) + ... (nk - 1)
        return int(couple - cycle)
