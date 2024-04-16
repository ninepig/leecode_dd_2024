# 酒店和景点
# 你在一个城市旅游，每个景点有个 景点分数，你自己住在酒店也算一个景点，你总是从自己酒店出发，最后回到酒店(酒店是point
# 0 )。已知从一个点到另一个点需要的时间，求在给定的时间内，最多可以浏览的景点分数。
# 这道题在领口里有原题 - 尔灵流五
# 用dfs
import collections


class solution:
    def getMaxPoiint(self, values, edges, maxTime):
        '''
        1 build graph
        2 using dfs to keep travel
        3 arrive start hotel. updated max score
        4 in dfs , when it over max time, stop
        '''

        graph = collections.defaultdict(list)

        for edge in edges:
            s, d, t = edge[0], edge[1], edge[2]
            graph[s].append([d, t])
            graph[d].append([s, t])

        max_value = 0
        visited = [0 for _ in range(len(values))]

        def dfs(cur_pos, cur_time, total):
            nonlocal max_value
            if cur_time > maxTime:
                return  ## we can not make in time
            if visited[cur_pos] == 0:  # have not visited this node
                total += values[cur_pos]
            if cur_pos == 0:  ## we reach target
                max_value = max(max_value, total)  ## updated value

            visited[cur_pos] += 1  ## updated vistied map
            for neighbour, time in graph[cur_pos]:
                dfs(neighbour, time + cur_time, total)

            visited[cur_pos] -= 1  ## back track

        dfs(0, 0, 0)

        return max_value


values = [0, 32, 10, 43]

edges = [[0, 1, 10], [1, 2, 15], [0, 3, 10]]

max_time = 49
sol = solution()

print(sol.getMaxPoiint(values, edges, max_time))