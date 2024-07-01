import collections
import math


class Solution:
    def getMissingPath(self, g_nodes, from_city, to_city, weight):
        ## sanitty check, missing some other check, different length .. ..
        if not g_nodes or not from_city or not to_city or not weight:
            return []

        queue = collections.deque()
        min_distance = math.inf
        path = []
        graph = collections.defaultdict(list)  ## we need build graph first
        length = len(from_city)

        for i in range(length):
            cur_from_city = from_city[i]
            cur_to_city = to_city[i]
            graph[cur_from_city].append(i)  ## we add index for better getting weight and city
            graph[cur_to_city].append(i)

        ## mini typo bug
        queue.append((1, 0, set()))  ## adding current city, current distance, set to queue

        while queue:
            cur_city, cur_dist, visited = queue.popleft()
            if cur_city == g_nodes:  # we reach
                if cur_dist < min_distance:
                    min_distance = cur_dist
                    path = []
                path.append(list(visited))
            if cur_dist < min_distance:  ## if larger , no need to keep doing this
                for edge in graph[cur_city]:  ## check where we can go
                    if edge not in visited:
                        if to_city[edge] == cur_city:
                            queue.append((from_city[edge], cur_dist + weight[edge], visited | {edge}))
                        elif from_city[edge] == cur_city:
                            queue.append((to_city[edge], cur_dist + weight[edge], visited | {edge}))

        res = ['NO'] * length
        for item in path:
            for edge in item:
                res[edge] = 'YES'

        print(res)

        return res


sol = Solution()
ans = sol.getMissingPath(
    5,
    [1, 2, 3, 4, 5, 1, 5],
    [2, 3, 4, 5, 1, 3, 3],
    [1, 1, 1, 1, 3, 2, 1]
)
