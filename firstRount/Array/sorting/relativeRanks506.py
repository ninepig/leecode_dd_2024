import heapq
from typing import List

'''
非常好的题
一样是利用了最小堆
利用 -val 以及index 作为tumple 
第一个pop出来的反而是第一名。 所以an[i] 是排名
'''
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rankings = []
        for i, val in enumerate(score):
            heapq.heappush(rankings, (-val, i))
        print(rankings)
        ans = [''] * len(score)
        r = 1
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        while len(rankings) != 0:
            _, i = heapq.heappop(rankings)
            if r <= 3:
                ans[i] = rank[r-1]
            else:
                # convert number to string
                ans[i] = str(r)
            r += 1
        return ans


num = [1,3,2,4,5]
sol = Solution()
print(sol.findRelativeRanks(num))

