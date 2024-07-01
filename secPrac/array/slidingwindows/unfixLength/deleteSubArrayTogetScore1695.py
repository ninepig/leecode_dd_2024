class Solution:
    '''
    1 consequence
    2 not repeat
    ---> sliding windows
    '''
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        windows = dict()
        left , right = 0 , 0
        max_ans = 0
        pre_sum = 0
        while right < len(nums):
            pre_sum += nums[right]
            if nums[right] not in windows:
                windows[nums[right]] = 1
            else:
                windows[nums[right]] += 1
            while windows[nums[right]] > 1:
                windows[nums[left]] -= 1
                pre_sum -= nums[left]
                left += 1

            max_ans = max(pre_sum,max_ans)
            right += 1

        return max_ans
