import heapq
'''
k close node
也就是离点 距离最近的k个点
维护距离的最大堆
如果距离小于堆顶
。。。
'''
class Solution:
    def kClosest(self, points, k):
        hp = []
        for point in points:
            x,y =point
            distance = x*x +y*y
            t=(-distance, point)
            if len(hp) < k:
                heapq.heappush(hp,t)
            else:
                if -distance > hp[0][0]:
                    #heapq.heappop(hp)
                    #heapq.heappush(hp, [-distance, point])
                    heapq.heapreplace(hp, t)
        return [point for _, point in hp]
