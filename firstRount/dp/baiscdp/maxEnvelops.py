from typing import Tuple, List


class Solution:
    '''
    1,8
    2,3
    5,4
    5,2
    6,7
    6,4
    after sorting , that will be a LISequence problem
    '''
    def maxEnvelopes(self,envelopes: List[Tuple[int, int]]) -> int:
        # sorted by width first, then des order by height
        if not envelopes : return 0
        envelopes.sort(key= lambda x: (x[0],-x[1])) # sort by width first, then des by height
        height = [item[1] for item in envelopes]

        return self.lengthOfLIS(envelopes)

    def lengthOfLIS(self,nums: List[int]) -> int:
        if not nums: return 0
        #state, initial
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i],dp[j] + 1)

        res = max(dp)
        return res