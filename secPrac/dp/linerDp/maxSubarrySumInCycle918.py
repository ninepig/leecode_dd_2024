'''
53的变形题
对于环
我们有两种可能
1 类似53 连续的数组
2 头尾相连， 这样就是让中间的数组最小
res = max(sum - min_middle, max_middle)
'''
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_num , min_num = nums[0],nums[0]
        max_dp, min_dp = nums[0],nums[0]
        for i in range(len(nums)):
            max_dp = max(max_dp + nums[i] , nums[i]) ## local max
            min_dp = max(min_dp + nums[i] , nums[i]) ## local min
            max_num = max(max_num,max_dp) # global max
            min_num = min(min_num,min_dp) # global min
        sum_num = sum(nums)
        if max_num < 0:
            return max_num
        return max(sum_num - min_num , max_num)