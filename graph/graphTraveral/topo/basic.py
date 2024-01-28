import collections

from LinkedList import List


class Solution:
    # 拓扑排序，graph 中包含所有顶点的有向边关系（包括无边顶点）
    def topologicalSortingKahn(self, graph: dict):
        indegrees = {u: 0 for u in graph}  # indegrees 用于记录所有顶点入度
        for u in graph:
            for v in graph[u]:
                indegrees[v] += 1  # 统计所有顶点入度

        # 将入度为 0 的顶点存入集合 S 中
        S = collections.deque([u for u in indegrees if indegrees[u] == 0])
        order = []  # order 用于存储拓扑序列

        while S:
            u = S.pop()  # 从集合中选择一个没有前驱的顶点 0
            order.append(u)  # 将其输出到拓扑序列 order 中
            for v in graph[u]:  # 遍历顶点 u 的邻接顶点 v
                indegrees[v] -= 1  # 删除从顶点 u 出发的有向边
                if indegrees[v] == 0:  # 如果删除该边后顶点 v 的入度变为 0
                    S.append(v)  # 将其放入集合 S 中

        if len(indegrees) != len(order):  # 还有顶点未遍历（存在环），无法构成拓扑序列
            return []
        return order  # 返回拓扑序列

    def findOrder(self, n: int, edges):
        # 构建图
        graph = dict()
        for i in range(n):
            graph[i] = []

        for u, v in edges:
            graph[u].append(v)

        return self.topologicalSortingKahn(graph)



    # 构建图 把各个边构成图
    def FindOrderPrac(self,n:int, edges):
        # 构建indgree的过程 , edge---> 图--->indegree图
        graph = dict()
        for i in range(n):
            graph[i] = []

        # 有向图
        for u,v in edges:
            graph[u].append(v)

        return self.topologicalSortingKahnPrac(graph)


    def topologicalSortingKahnPrac(self, graph):
        ##构建indegree dict
        indegree = { u:0 for u in graph}
        for u in graph:
            for v in graph[u]:
                indegree[v] += 1

        queue = collections.deque([])
        for u in indegree:
            if indegree[u] == 0:
                queue.append(u)

        order = []

        while queue:
            cur = queue.pop()
            order.append(cur)
            for v in graph[cur]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)

        if len(indegree) != len(order):
            # 有环
            return []

        return order


def topoPrac(self, n: int, edges:List[List[int]]):
     # edge---> graph
    graph = dict()
    for i in range(n):
         graph[i] = []
    for u,v in edges:
        graph[u].append(v)

    # graph---> indegreeDict

    indegreeDict = {u:0 for u in graph}
    for u in graph:
        for v in graph[u]:
            indegreeDict[v] += 1

    queue = collections.deque([u for u in indegreeDict if indegreeDict[u] == 0])
    order = []

    while queue:
        cur = queue.pop()
        order.append(cur)
        for v in graph[cur]:
            indegreeDict[v] -= 1
            if indegreeDict[v] == 0:
                queue.append(v)

    if len(indegreeDict) != len(order):
        return []
    return order





