# 酒店和景点
# 你在一个城市旅游，每个景点有个 景点分数，你自己住在酒店也算一个景点，你总是从自己酒店出发，最后回到酒店(酒店是point
# 0 )。已知从一个点到另一个点需要的时间，求在给定的时间内，最多可以浏览的景点分数。
# 这道题在领口里有原题 - 尔灵流五
# 用BFS + heap做就行
import collections


class Solution:
    ## wrost case , node^maxTime--> brutal force way
    def maximalPathQuality(self, values: list[int], edges: list[list[int]], maxTime: int) -> int:
        d = collections.defaultdict(list)
        n = len(values)

        for edge in edges:
            d[edge[0]].append([edge[1], edge[2]])
            d[edge[1]].append([edge[0], edge[2]])

        visited = [0] * n
        ans = 0

        def dfs(node, curTime, total):
            nonlocal ans
            if curTime > maxTime:
                return

            if visited[node] == 0:
                total += values[node]

            if node == 0:
                if total > ans:
                    ans = total

            visited[node] += 1

            for vertex, time in d[node]:
                dfs(vertex, curTime + time, total)

            visited[node] -= 1

        dfs(0, 0, 0)
        return ans
