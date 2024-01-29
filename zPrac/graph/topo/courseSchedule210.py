from collections import deque
from typing import List

class Solution:
    def findOrderDFS(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = self.buildGraph(numCourses,prerequisites)
        visit = [False] * numCourses
        onPath =[False] * numCourses
        postOrder = []
        self.cycle = False

        for start in range(numCourses):
            self.dfs(graph,visit,onPath,postOrder,start)

        if self.cycle :
            return []

        return postOrder[::-1]


    def dfs(self, graph, visit, onPath, postOrder, start):
        if start in onPath:
            self.cycle = True
        if visit[start] or self.cycle:
            return
        visit[start] = True
        onPath[start] = True
        for neigh in graph[start]:
            self.dfs(graph,visit,onPath,postOrder,neigh)

        onPath[start] = False
        postOrder.append(start) ## 后续order


    def buildGraph(self, numCourses,prerequisites):
        graph = [[]for _ in range(numCourses)]
        for edge in prerequisites:
            from_v, to_v = edge[1],edge[0]
            graph[from_v].append(to_v)

        return graph


    def findOrderBFS(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = self.buildGraph(numCourses,prerequisites)
        indegree = [0 for _ in range(numCourses)]

        for edge in prerequisites:
            indegree[edge[1]] += 1
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        count = 0
        res = []
        while q :
            cur = q.popleft()
            count += 1
            res.append(cur)
            for neighbour in graph[cur]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    q.append(neighbour)

        if count != neighbour:
            return [] # topo not exist
        return res

