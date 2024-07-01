class Solution:

    '''dp , 到目前n pos ， sum '''
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        dp = [0 for _ in range(size)]

        dp[0] = nums[0]
        for i in range(1, size):
            if dp[i - 1] < 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i - 1] + nums[i]
        return max(dp)

    ## 更直观的答案， 局部 和全局 其实就是只用了两个变量的dp
    '''贪心题
     对于当前preSum 如果小于0 ， 那就没必要保留了
     '''
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        subMax = nums[0]
        ansMax = nums[0]
        for i in range(1, size):
            # 约等于这一行
            # subMax = max(ansMax + nums[i] , nums[i])
            if subMax < 0:
                subMax = nums[i]
            else:
                subMax += nums[i]
            ansMax = max(ansMax, subMax)
        return ansMax