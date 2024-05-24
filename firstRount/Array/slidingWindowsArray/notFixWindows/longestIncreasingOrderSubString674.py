class Solution:
    '''最基本的不固定数组'''
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        left , right = 0 , 0
        size = len(nums)
        windows_len = 0
        max_res = 0
        while right < size :
            windows_len += 1

            # keep find large one , if not , reset windows
            if right > 0 and nums[right - 1] > nums[right]:
                left = right
                windows_len = 0

            max_res = max(windows_len,max_res)

            right += 1

        return max_res
    #DP version
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        size = len(nums)
        dp = [1 for _ in range(size)]

        for i in range(1, size):
            if nums[i - 1] < nums[i]:
                dp[i] = dp[i - 1] + 1

        return max(dp)