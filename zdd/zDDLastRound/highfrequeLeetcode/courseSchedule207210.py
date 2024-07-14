import collections
from typing import List


class Solution:
    #o（v+e)
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

    def canFinishOrder(self, numCourses: int, prerequisites: List[List[int]]) -> list:
        #edge---> graph , 用这种 default 会出问题
        graph = dict()
        for i in range(numCourses):
            graph[i] = []
        # graph = collections.defaultdict(list)
        # graph ---> indegree v is prerequest, u is current
        for u,v in prerequisites:
            graph[v].append(u)
        print(graph)
        # {0: [1, 2], 1: [3], 2: [3], 3: []}
        ## using default dict 可能会出现某个node 没有outdegree 所以就会出现空。 所以会报错
        ## defaultdict(<class 'list'>, {0: [1, 2], 1: [3], 2: [3]})
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


sol = Solution()
num = 4
edges = [[1,0],[2,0],[3,1],[3,2]]

print(sol.canFinishOrder(num,edges))