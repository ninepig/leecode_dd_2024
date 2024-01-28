from sortedcontainers import SortedList


class Solution:
    '''用sortedlist 来做windows 易如反掌'''
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        windows = SortedList()
        left , right = 0 , 0
        ans = 0
        while right < len(nums):
            windows.add(nums[right])
            while windows[-1] - windows[0] > limit:
                windows.remove(nums[left])
                left += 1

            ans = max(ans, right - left + 1)
            right += 1

        return ans


