# https://www.fastprep.io/problems/get-minimum-cost
import heapq
from typing import List

'''
第一次买一个价格
第二次买就价格升级
所以用一个pq 每次把最新的价格放进去。。永远买最便宜的即可
'''
class Solution:
    def getMinimumCost(self, a: List[int], b: List[int], m: int) -> int:
        pqueue = []

        # Initial population of the priority queue
        for i in range(len(a)):
            heapq.heappush(pqueue, (a[i], i))

        tot = 0
        for i in range(m):
            # Extracting the element with the minimum cost
            min_cost, idx = heapq.heappop(pqueue)
            tot += min_cost
            # Calculate new cost
            ncost = min_cost + b[idx]
            # Adding the next cost for the same index
            heapq.heappush(pqueue, (ncost, idx))

        return tot
