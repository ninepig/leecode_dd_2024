import collections

from LinkedList import List

'''
topo的应用题
对于第 i 个人，我们要求解的是比第 i 个人更有钱或者和他一样有钱的人中，安静值最小的那个人的编号。
我们可以建立一张有向无环图，由富人指向穷人。这样，对于任意一点来说（比如 x），通过有向边链接的点（比如 y），
拥有的钱都没有 x 多。则我们可以根据 answer[x] 去更新所有 x 能连接到的点的 answer 值。
我们可以先将数组 answer 元素初始化为当前元素编号。然后对建立的有向无环图进行拓扑排序，按照拓扑排序的顺序去更新 x 能连接到的点的 answer 值。'''
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        # build graph dict then poor indegree
        size = len(quiet)
        res = [i for i in range(size)]

        graph = dict()
        for u in range(size):
            graph[u] = []

        for u in richer:
            for v in richer[u]:
                graph[u].append(v)

        # graph to indegree
        indegree = {u:0 for u in graph}
        for u in graph:
            for v in graph[u]:
                indegree[v] += 1
        # put rich into queue
        queue = collections.deque([u for u in graph if u == 0])

        while queue:
            x = queue.popleft()
            for y in graph[x]:
                ## 利用安静值更新, 因为我们知道的是y 肯定比 x 穷, 所以利用x的值去更新y的值, 就可以得到对于y比他富有的人的最低安静值,在这里用编号更新
                if quiet[res[x]] < quiet[res[y]]:
                    res[y] = res[x]
                indegree[y] -= 1
                if indegree[y] == 0:
                    queue.append(y)

        return res