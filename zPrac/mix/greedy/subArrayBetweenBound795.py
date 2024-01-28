class Solution:
    '''贪心题
    between right and left => max< RIGHT - MAX< LEFT'''
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        return self.numSubarraySmallerK(nums,nums[right]) - self.numSubarraySmallerK(nums,nums[left])
    '''
    贪心法
    如果当前value 大于k 则说明subarray在这边没法+1
    如果小于k 则说明对于当前数 subarry 可以加1'''
    def numSubarraySmallerK(self, nums, max):
        count = 0
        ans = 0
        for i in range(nums):
            if nums[i] < max:
                count += 1
            else:
                count = 0
            ans += count

        return ans