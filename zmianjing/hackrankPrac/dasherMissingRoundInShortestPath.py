import collections


class Solution:
    def getShortestPath(self, g_nodes, from_city, to_city, weight):
        ## santity check
        if not from_city or not to_city or not weight:
            raise Exception("Wrong input")

        '''
        we want to reach g_nodes from 1 and with shortest path
        so we can use bfs to do this 
        1first build graph (duel dirctions)
        2 travel from 1 node, maintain a shortest distance, update shortest path and distance once we find a short one
        3 mark the node in res
        '''
        queue = collections.deque()
        min_distance = 999
        path = []
        graph = collections.defaultdict(list)
        lengh = len(from_city)

        for i in range(lengh):
            from_c = from_city[i]
            to_c = to_city[i]
            ## we append idx to graph for better access or we can append a tuble
            graph[from_c].append(i)
            graph[to_c].append(i)

        queue.append((1, 0, set()))

        while queue:
            cur_city, cur_dist, visited = queue.popleft()
            if cur_city == g_nodes:  ## we arrived
                if cur_dist < min_distance:
                    min_distance = cur_dist
                    path = []  ## if we need refresh path
                path.append(list(visited))  ## we get path to gnode.

            if cur_dist < min_distance:  ## only we can bfs when we not reach min distance
                for edge in graph[cur_city]:  ## found city we can arrivve
                    if edge not in visited:  ## not visited
                        if to_city[edge] == cur_city:
                            ## bug here , we need add weight
                            queue.append((from_city[edge], cur_dist + weight[edge], visited | {edge}))
                        else:
                            queue.append((to_city[edge], cur_dist + weight[edge], visited | {edge}))

        res = ['NO'] * lengh
        for path_list in path:
            for item in path_list:
                res[item] = 'YES'

        return res


sol = Solution()
ans = sol.getShortestPath(
    5,
    [1, 2, 3, 4, 5, 1, 5],
    [2, 3, 4, 5, 1, 3, 3],
    [1, 1, 1, 1, 3, 2, 1]
)
print(ans)