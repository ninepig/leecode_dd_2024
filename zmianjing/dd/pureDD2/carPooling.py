from typing import List


class diffArray:
    def __init__(self,nums:List[int]):
        self.diff = [0 for _ in range(len(nums))]
        self.diff[0] = nums[0]
        for i in range(1,len(nums)):
            self.diff[i] = nums[i] - nums[i-1]
    def update(self,left:int, right:int,val:int):
        self.diff[left] += val
        if right + 1 < len(self.diff):
            self.diff[right + 1] -=val

    def result(self):
        res = [0 for _ in range(len(self.diff))]
        res[0] = self.diff[0]
        for i in range(1,len(self.diff)):
            res[i] = res[i-1] + self.diff[i]
        return res

class Solution:
    def carPooling(trips: List[List[int]], capacity: int) -> bool:
        helper = [0 for _ in range(1001)] # dataset size
        dt = diffArray(helper)

        for trip in trips:
            val = trip[0]
            left = trip[1]
            right = trip[2] - 1 ## right already get customer off, so when trip[2] - 1 has right value of customer
            dt.update(left,right , val)

        res = dt.result() # get result for final array and each stop's number

        for num in res:
            if num > capacity: ## 任何一站都没问题
                return False

        return True ## in dd question
        # return max(res)


