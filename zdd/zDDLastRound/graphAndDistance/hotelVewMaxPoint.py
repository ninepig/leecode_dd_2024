import collections
import math


class Solution:
    ## wrost case , node^maxTime--> brutal force way
    def maximalPathQuality(self, values: list[int], edges: list[list[int]], maxTime: int) -> int:
        path_time_graph = collections.defaultdict(list)
        for edge in edges:
            path_time_graph[edge[0]].append([edge[1],edge[2]])
            path_time_graph[edge[1]].append([edge[0],edge[2]])

        max_value = 0
        visited = [0] * len(values)

        def dfs(node,cur_time,total):
            nonlocal max_value

            if cur_time > maxTime:
                return ## we dont consider time bigger than max time

            if visited[node] == 0 : ## first time to this node
                total += visited[node]

            if node == 0: # we get back to starting point
                if total > maxTime:
                    max_value = total

            visited[node] += 1

            for next_node,time in path_time_graph[node]:
                dfs(next_node,cur_time + time, total)

            visited[node] -= 1 ## using backtrack

        dfs(0,0,0)

        return max_value