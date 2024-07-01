import collections


class Solution:
    def bfs(self, graph, u):
        visited = set()
        queue = collections.deque([])
        visited.add(u)
        queue.append(u)

        while queue:
            cur = queue.popleft() #保证是从头开始取,左侧,所以保证顺序
            # 找邻居 , 因为不是树(层序) 所以不用考虑有多少个点在当前层,只需要按顺序即可
            for next in graph[cur]:
                if next not in visited:
                    visited.add(next)
                    queue.append(next)
