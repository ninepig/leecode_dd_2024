# 酒店和景点
# 你在一个城市旅游，每个景点有个 景点分数，你自己住在酒店也算一个景点，你总是从自己酒店出发，最后回到酒店(酒店是point
# 0 )。已知从一个点到另一个点需要的时间，求在给定的时间内，最多可以浏览的景点分数。
# 这道题在领口里有原题 - 尔灵流五
# 用BFS + heap做就行
import collections


class Solution:
    ## wrost case , node^maxTime--> brutal force way
    def maximalPathQuality(self, values: list[int], paths: list[list[int]], maxTime: int) -> int:
        ## maintain a graph, node's content is target node with consuming time
        graph = collections.defaultdict(set)
        for path in paths:
            u,v,t = path[0],path[1],path[2]
            graph[u].add((v,t))
            graph[v].add((u,t))

        result = 0
        visited = collections.defaultdict(int)

        def dfs(u,maxTime,points):
            if u == 0:
                nonlocal result
                result = max(points,result)

            visited[u] += 1 ## visited this point

            for v,t in graph[u]:
                if maxTime - t >= 0:
                    ## we can dfs to search
                    dfs(v,maxTime - t , points + values[v] if v not in visited else 0) ## we only add point if we never vist that
            visited[u] -= 1 ## backtrack
            if visited[u] == 0:
                del visited[u]

        dfs(0,maxTime,values[0])

        return result
