'''
这个题就是 k 可能等于0
所以要考虑全部情况
如果是k
那只要记录有多少数相等即可。 因为是unique pair
'''
import collections
'''
这个题也比较简单
'''

class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        counter = collections.Counter(nums)
        res = 0
        if k == 0:
            for key,v in counter.items():
                if v > 1: ## we have duplicated , which mean we can form (2,2) diff = 0
                    res += 1
        if k != 0:
            for key,v in counter.items():
                if (key + k) in counter:
                    res += 1 ## unique one, so can only plus 1 not vlaue

        return res

