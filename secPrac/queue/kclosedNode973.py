import heapq


class Solution:
    # kclosest 用最小堆, pop out smallest value
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for point in points:
            distance = point[0]*point[0] + point[1]*point[1]
            heapq.heappush(pq,(distance,point))
        res = []
        index = 0
        while index < k:
            point = heapq.heappop()[1]
            res.append(point)

        return res