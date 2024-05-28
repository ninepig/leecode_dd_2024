import math
import heapq


class Solution:
    def getPeakOrder(self, order: list[int]):
        '''
        1 pop out the peak with smaller orderId

        bf way
        1 loop to find any peak, store : peak value : index to a dict
        2 check the loop, pop the target
        3 loop again

        better way
        since we want smaller value , we can use priroty queue to avoid loop again
        if we use pq, we need a btter way to record pop item
        we can use complexDs to record node's left/right neightbour
        when we pop item , we can have record of it's left,right item
        then we check node's left right to see if we need push to queue again

        '''
        ## sanity check
        if not order or len(order) == 0:
            return []
        ## we must use -math.inf to do this
        order = [-math.inf] + order + [-math.inf]  ## we add dummy node for better processing
        neighbour = dict()
        for i in range(1, len(order) - 1):
            neighbour[order[i]] = [order[i - 1], order[i + 1]]

        pq = []
        for i in range(1, len(order) - 1):
            if order[i - 1] < order[i] and order[i] > order[i + 1]:
                heapq.heappush(pq, order[i])

        if len(pq) == 0:
            return order  ## no peak, 123456

        res = []
        while pq:
            cur_peak = heapq.heappop(pq)
            res.append(cur_peak)
            ## check peak item 's left ,right
            left, right = neighbour[cur_peak]
            if left != -math.inf:
                neighbour[left][1] = right
                if neighbour[left][0] < left and left > neighbour[left][1]:  ## we found a peak
                    heapq.heappush(pq, left)

            if right != -math.inf:
                neighbour[right][0] = left
                if neighbour[right][0] < right and right > neighbour[right][1]:  ## we found apeak
                    heapq.heappush(pq, right)
            neighbour.pop(cur_peak)
        return res


sol = Solution()
test = [3, 1, 5, 4, 2]
test2 = [30, 10, 50, 40, 20, 70, 15, 16]
print(sol.getPeakOrder(test2))
