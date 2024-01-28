class Solution:
    '''关键是连续的
    这个滑动窗口 自己做一开始没想明白 看了答案才想明白的
    '''
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0 :
            return 0
        ans = 0
        left = 0
        right = 0
        window_lens = 0

        while right < len(nums):
            window_lens += 1
            if right > 0 and nums[right] < nums[right - 1]:
                left = right
                window_lens = 1

            ans = max(ans, window_lens) 
            right += 1

        return ans
