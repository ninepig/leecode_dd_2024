class Solution:
    '''
    300的followup
    当 nums[j] < nums[i]，而且 dp[j] + 1 > dp[i] 时，说明第一次找到 dp[j] + 1长度且以nums[i]结尾的最长递增子序列，
    则以 nums[i] 结尾的最长递增子序列的组合数就等于以 nums[j] 结尾的组合数，即 count[i] = count[j]。

    当 nums[j] < nums[i]，而且 dp[j] + 1 == dp[i] 时，说明以 nums[i] 结尾且长度为 dp[j] + 1 的递增序列已找到过一次了，
    则以 nums[i] 结尾的最长递增子序列的组合数要加上以 nums[j] 结尾的组合数，即 count[i] += count[j]。

    然后根据遍历 dp 数组得到的最长递增子序列的长度 max_length，然后再一次遍历 dp 数组，将所有 dp[i] == max_length 情况下的组合数 coun[i] 累加起来，
    即为最长递增序列的个数
    '''
    def findNumberOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        dp = [1] * size
        count = [1] * size
        for i in range(size):
            for j in range(i):
                if nums[i] > nums[j] :
                    # dp[i] = max(dp[i],dp[j] + 1)
                    if dp[j] + 1 > dp[i] :  # which means we never been to dpi before
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i] : # which means we have this lis before
                        count[i] += count[j] # we need add count together

        res = 0
        max_length = max(dp) # longest value
        for i in range(size):
            if dp[i] == max_length:
                res += count[i]

        return res