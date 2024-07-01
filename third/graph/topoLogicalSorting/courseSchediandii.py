import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites or len(prerequisites) == 0 : return False
        ## build graph
        graph = collections.defaultdict(list)
        for u,v in prerequisites:
            graph[v].append(u) ## from question, who is pre-requesat, we put in graphd as starting source

        ## building indegree dict
        indegree = {u:0 for u in graph}

        for cur_list in graph:
            for v in cur_list:
                indegree[v] += 1

        deque = collections.deque([u for u in indegree if indegree[u] == 0]) ## 复杂的写法但是习惯就好 indegree = 0 ，进入队列

        courseCanFinish = 0
        while deque:
            cur_course = deque.popleft()
            courseCanFinish += 1
            ## topo 的逻辑， 找可以reach的点， indgree -1， 如果等于0 ， 就可以入栈
            for v in graph[cur_course]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    deque.append(v)

        return courseCanFinish == numCourses

    def canFinishOrder(self, numCourses: int, prerequisites: List[List[int]]) -> list[int]:
        #edge---> graph
        if not prerequisites or len(prerequisites) == 0 : return False
        ## build graph
        graph = collections.defaultdict(list)
        for u,v in prerequisites:
            graph[v].append(u) ## from question, who is pre-requesat, we put in graphd as starting source

        ## building indegree dict
        indegree = {u:0 for u in graph}

        for cur_list in graph:
            for v in cur_list:
                indegree[v] += 1
        queue = collections.deque([u for u in indegree if indegree[u] == 0])
        order = []

        while queue:
            cur = queue.pop()
            order.append(cur)
            for v in graph[cur]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)

        if len(order) != numCourses:
            return []

        return order
