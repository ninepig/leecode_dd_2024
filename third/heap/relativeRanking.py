import heapq
from typing import List

'''
找相对排序
最大堆，用tuple形式 （-num,indx)
'''

class solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        if not score or len(score) == 0 :
            return []
        heap = []
        for i,v in enumerate(score):
            heapq.heappush(heap,(-v,i)) ## push as a maxheap

        res = ["" for _ in range(len(score))]

        index = 0

        while heap:
            _,pos = heapq.heappop(heap)
            index+=1
            if index == 1:
                res[pos] = "gold"
            elif index == 2:
                res[pos] = "silver"
            elif index == 3:
                res[pos] = "bronze"
            else:
                res[pos] = str(index)

        return res

sol = solution()
# test = [5,4,3,2,1]
# print(sol.findRelativeRanks(test))

test =  [10,3,8,9,4]
print(sol.findRelativeRanks(test))