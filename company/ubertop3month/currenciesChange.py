## https://www.1point3acres.com/bbs/thread-1037138-1-1.html
## leetcode 399
from collections import defaultdict, deque
from typing import List

'''
uber的题 就是399
会给初始 value

有向 加权图
构图 + bfs 来做

'''
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1.0 / val))

        def bfs(init, goal,init_v):
            if init not in graph or goal not in graph:
                return -1.0
            explored = {init}
            # q = deque([(init, 1.0)])
            q = deque([(init, init_v)])
            while q:
                node, v = q.popleft()
                if node == goal:
                    return v
                for nxt, cost in graph[node]:
                    if nxt not in explored:
                        explored.add(nxt)
                        q.append((nxt, v * cost))
            return -1.0

        # return [bfs(i, g) for i, g in queries]
        return [bfs(i, g, init_v) for i, g,init_v in queries]


    def calcEquationPrac(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        ## santity check
        graph = defaultdict(list)
        for idx,equation in enumerate(equations):
            graph[equation[0]].append((equations[1],values[idx]))
            graph[equation[1]].append((equations[0],1/values[idx]))

        def bfs(s,t,i):
            visited = set()
            visited.add(s)
            queue = deque([(s,i)])
            while queue:
                cur, value = queue.popleft()
                if cur == t:
                    return value
                for node,cost in graph[cur]:
                    if node not in visited:
                        value *=cost
                        visited.add(node)
                        queue.append((node,value))

            return -1 ## not exist
        res = []
        for query in queries:
            start,target,init_value = query[0],query[1],query[2]
            res.append(bfs(start,target,init_value))

        return res
