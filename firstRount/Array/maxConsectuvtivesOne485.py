from typing import List

'''
global vs local.
taking care of when to check global 

'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        global_max_value,local_max_value = 0, 0

        for idx, elem in enumerate(nums):
            if elem == 1:
                local_max_value += 1
                if global_max_value < local_max_value:
                    global_max_value = local_max_value
            else:
                local_max_value = 0

        return global_max_value

sol = Solution()
num = [1,1,0,1,1,1]
sol.findMaxConsecutiveOnes(num)