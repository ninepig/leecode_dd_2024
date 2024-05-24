'''
描述：给定一个字符串 s，再给定一个数组 pairs，其中 pairs[i] = [a, b] 表示字符串的第 a 个字符可以跟第 b 个字符交换。只要满足 pairs 中的交换关系，可以任意多次交换字符串中的字符。

要求：返回 s 经过若干次交换之后，可以变成的字典序最小的字符串。
'''
import collections

'''
特别牛逼的union find 题
利用每个cluster + dict 保存每个簇里含有的char
然后利用排序 把char sort下
再依次输出以获得字典序
'''
class UnionFind:
    def __init__(self,n):
        self.count = n
        self.fa = [i for i in range(n)]

    def find(self,x):
        while x != self.fa[x]:
            self.fa[x] = self.fa[self.fa[x]]
            x = self.fa[x]
        return x

    def union(self,x,y):
        root_x  = self.find(self,x)
        root_y  = self.find(self,y)
        if root_y == root_x :
            return False
        self.fa[root_x] = root_y
        self.count -= 1
        return True

    def is_connect(self,x,y):
        return self.find(x) == self.find(y)

'''
如果第 a 个字符可以跟第 b 个字符交换，第 b 个字符可以跟第 c 个字符交换，那么第 a 个字符、第 b 个字符、第 c 个字符之间就可以相互交换。
我们可以把可以相互交换的「位置」都放入一个集合中。然后对每个集合中的字符进行排序。然后将其放置回在字符串中原有位置即
'''
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        size = len(pairs)
        uf = UnionFind(size)
        # form uf
        for pair in pairs:
            uf.union(pair[0],pair[1])

        mp = collections.defaultdict()
        for i, ch in enumerate(s):
            mp[uf.find(i)].append(ch)

        # 字典序,小的在后面
        for vec in mp.values():
            vec.sort(reverse = True)

        ans = []
        for i in range(size):
            x = uf.find(i)
            ans.append(mp[x][-1])
            mp[x].pop()

        return "".join(ans)