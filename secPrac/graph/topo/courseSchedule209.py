from collections import deque
from typing import List


class Solution:
    '''
    check if has cycle
    topo sort
    1 dfs
    类比贪吃蛇游戏，visited 记录蛇经过过的格子，而 onPath 仅仅记录蛇身。onPath 用于判断是否成环，类比当贪吃蛇自己咬到自己（成环）的场景。
    2 bfs
    '''
    def canFinishDFS(self,numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = self.buildGraph(numCourses,prerequisites)
        visited = [False for _ in range(numCourses)]
        onPath = [False for _ in range(numCourses)]
        self.hasCycle = False

        for i in range(numCourses):
            self.travel(graph,visited,onPath,i)

        return not self.hasCycle

    def buildGraph(self, numCourses,prerequisites):
        graph = [[] for _ in range(numCourses)] # adjacent list to build graph
        for edge in prerequisites:
            from_v, to_v = edge[1] , edge[0]
            graph[from_v].append(to_v)

        return graph
    #dfs to travel every node
    def travel(self, graph, visited, onPath, node):
        if node in onPath:
            self.hasCycle = True
        if visited[node] or self.hasCycle:
            return
        visited[node] = True
        onPath[node] = True
        for neighbourin in graph[node]:
            self.travel(graph,visited,onPath,neighbourin)
        onPath[node] = False

    def canFinishBfs(self,numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = self.buildGraph()
        indegree = [0 for _ in range(numCourses)] # 我们用numbercorse来做图，所以直接用这个来做入度 没问题
        for edge in prerequisites:
            to_node = edge[0]
            indegree[to_node] += 1

        ## 入度为0的先入队
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        number = 0

        while q:
            cur = q.popleft()
            number += 1
            for neighbour in graph[cur] :
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    q.append(neighbour)
        # 判断走完所有的图 是否和所有course一致
        return number == numCourses

