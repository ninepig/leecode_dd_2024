class Solution:
    '''类似53
    但是因为可能有正负值， 所以要维护之前一个最小值，一个最大值，
    '''
    def maxProduct(self, nums: List[int]) -> int:
        size = len(nums)

        max_dp = [0] * size
        min_dp = [0] * size
        max_dp[0] = nums[0]
        min_dp[0] = nums[0]

        for i in range(1,size):
            max_dp[i] = max(max_dp[i-1]*nums[i],nums[i],min_dp[i-1]*nums[i])
            min_dp[i] = min(max_dp[i-1]*nums[i],nums[i],min_dp[i-1]*nums[i])

        return max(max_dp)

    '''
    利用一个变量来滚动保存'''
    def maxProductNoarray(self, nums: List[int]) -> int:
        if not nums: return
        res = nums[0]
        pre_max = nums[0]
        pre_min = nums[0]
        for num in nums[1:]:
            cur_max = max(pre_max * num, pre_min * num, num)
            cur_min = min(pre_max * num, pre_min * num, num)
            res = max(res, cur_max)
            pre_max = cur_max
            pre_min = cur_min
        return res

