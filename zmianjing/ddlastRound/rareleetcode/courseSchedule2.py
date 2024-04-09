'''
have not find question in DD interview
just be topo sorting
'''
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:

        ## 构图是个graph graph是 u：[]
        graph = dict()
        for i in range(numCourses):
            graph[i] = []

        for edge in prerequisites:
            u,v = edge[1],edge[0]
            graph[u].append(v)

        ## build indgree array ---> indgree 是个大的dict  这两个做法很重要
        indgree = {u:0 for u in graph} ## contruct dict
        for u in graph:
            for v in graph[u]:
                indgree[v] += 1 ## count indgree

        queue = []
        for u in indgree:
            if indgree[u] == 0:
                queue.append(u)

        res = []

        while queue:
            cur = queue.pop(0) ## either deque or we have to pop first item
            res.append(cur)
            for v in graph[cur]:
                indgree[v] -= 1
                if indgree[v] == 0:
                    queue.append(v)

        if len(indgree) != len(res):
            return [] ## can not make topo sorting. since we still have node  not visit

        return res