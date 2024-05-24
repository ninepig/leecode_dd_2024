'''

1 preSum

python learning
enumerate(xxx)

'''
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum,rightSum = 0,sum(nums)
        for idx,elem in enumerate(nums):
            rightSum -= elem
            if leftSum == rightSum:
                return idx
            leftSum += elem
        return -1

    '''
    # Time Complexity : O(n)
# Space Complexity : O(1)
class Solution(object):
    def pivotIndex(self, nums):
        # Initialize leftSum & rightSum to store the sum of all the numbers strictly to the index's left & right respectively...
        leftSum, rightSum = 0, sum(nums)
        # Traverse elements through the loop...
        for idx, ele in enumerate(nums):
            rightSum -= ele
            # If the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right...
            if leftSum == rightSum:
                return idx      # Return the pivot index...
            leftSum += ele
        return -1       # If there is no index that satisfies the conditions in the problem statement...'''