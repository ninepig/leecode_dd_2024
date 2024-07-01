import collections
import math
from collections import defaultdict, deque
from typing import List


'''
uber 
刚面完，利口巴要舞升级版，除了原题的input之外多加了一个fares，要求从起点到终点的最小费用

白人小哥，uber 高频第一题，一开始聊了bfs 写法，然后interviewer 问有没有optimization， 以为是要union find 的写法，感觉要G， 结果不是，就是dedup 一下。 写完bfs 聊了聊union find 的写法和set intersection 的optimization。然后聊了聊in real life 会怎么implement，
答 cache all stops， 因为stops choose 2 也没多少combination，难的是怎么keep info up to date

UF 可以测试 source / target 是否可以连通， 如果不连通， 则直接返回 -1 ， 不需要一直bfs了
'''

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # 每个车站可以乘坐的公交车
        stations = defaultdict(set)
        for i, stops in enumerate(routes):
            for stop in stops:
                stations[stop].add(i)
        # 每个公交车线路可以到达的车站
        routes = [set(x) for x in routes]
        q = deque([(source, 0)])
        # 已经乘坐了的公交车
        buses = set()
        # 已经到达了的车站
        stops = {source}
        while q:
            pos, cost = q.popleft()
            ## 如果要获得path， 就需要层序遍历， 在每一层都把值统计下。
            if pos == target:
                return cost
            # 当前车站中尚未乘坐的公交车
            for bus in stations[pos] - buses:
                # 该公交车尚未到达过的车站
                for stop in routes[bus] - stops:
                    buses.add(bus)
                    stops.add(stop)
                    q.append((stop, cost + 1))
        return -1

    def numBusesToDestinationFare(self, routes: List[List[int]], source: int, target: int,fare:list[int]) -> int:
        ## build station : bus graph
        stations = defaultdict(list)
        for idx,stops in enumerate(routes):
            for stop in stops:
                stations[stop].append(idx) ## build station---> bus graph, in each station, how many bus can reach
        route_sets = [set(x) for x in routes] ## put each bus stop in a set list

        bus_set = set() ## bus we have take
        stop_set = {source} ## stop we have arrived
        queue = collections.deque([(source,0)])
        min_cost = -math.inf ## min cost
        while queue:
            cur_pos, cur_cost = queue.popleft()
            if cur_cost > min_cost : ## already exceed min cost so far, trim it
                continue
            if cur_pos == target : ## we reach last pos
                if cur_cost < min_cost:
                    min_cost = cur_cost
            for bus in stations[cur_pos] - bus_set: ## remaining bus we can take
                for stop in route_sets[bus] - stop_set: ## remaining stop we can get
                    bus_set.add(bus)
                    stop_set.add(stop)
                    queue.append((stop,cur_cost + fare[bus]))

        return min_cost



    ## 纯纯 利用set来做的
    def numBusesToDestinationPrac(self, routes: List[List[int]], source: int, target: int) -> int:
        station_map = collections.defaultdict(set)
        for i in range(len(routes)):
            for j in range(len(routes[i])):
                station_map[routes[i][j]].add(i) ## a graph , each station's available bus

        bus_sets = [set(x) for x in routes] ## bus's sation list
        queue = collections.deque([(source,0)]) ## queue with inital station
        stops = set()
        stops.add(source)
        bus_token = set()
        while queue:
            stop,cost = queue.popleft()
            ## bfs ending condition
            if stop == target:
                return cost

            for bus in station_map[stop] - bus_token : ## bus we can get in current station
                for stop in bus_sets[bus] - stops : ## stop we can get in
                    bus_token.add(bus)
                    stops.add(stop)
                    queue.append((stop,cost + 1))

        return -1



route = [[7,12],[4,5,15,19],[4,7],[9,15,12,19],[9,12,13]]
source = 15
target = 12
sol = Solution()
print(sol.numBusesToDestination(route,source,target))