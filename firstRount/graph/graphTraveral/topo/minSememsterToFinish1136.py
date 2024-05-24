import collections


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        # edge to graph
        graph = dict()
        for i in range(n):
            graph[i] = []
        for u,v in relations:
            graph[u].append(v)
        indegree = {u:0 for u in graph}
        for u in graph:
            for v in graph[u]:
                indegree[v] += 1
        # put indegree = 0 to queue
        queue = collections.deque([u for u in graph if u == 0])
        ans = 0
        while queue:
            size = len(size)


            for i in range(size):
                cur = queue.popleft()
                n -= 1 #     ## missing here 要判断是否课程全部上完
                for v in graph[cur]:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        queue.append(v)
            ans += 1

        return ans if n == 0 else -1