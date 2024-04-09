import collections

from LinkedList import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if not prerequisites : return True
        # edge --> graph
        graph = dict()
        for i in range(numCourses): # 用numCourse来做
            graph[i] = []
        for u,v in prerequisites: # u is the precourse
            graph[v].append(u)

        # graph --> indegreeOrder
        indegreeDict = {u:0 for u in graph}

        for u in graph:
            for v in graph[u]:
                indegreeDict[v] += 1

        queue = collections.deque([u for u in indegreeDict if indegreeDict[u] == 0])

        while queue:
            cur = queue.pop()
            numCourses -= 1
            for v in graph[cur]:
                indegreeDict[v] -= 1
                if indegreeDict[v] == 0:
                    queue.append(cur)

        return numCourses == 0

    def canFinishOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[]:
        #edge---> graph
        graph = dict()
        for i in range(numCourses):
            graph[i] = []

        # graph ---> indegree v is prerequest, u is current
        for u,v in prerequisites:
            graph[v].append(u)

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

        if len(order) != numCourses:
            return []

        return order
