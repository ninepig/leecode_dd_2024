'''
应用题
恰好包含k个 = k - k-1
159 340的后续
'''


class Solution:
    def subarraysMostKDistinct(self, nums, k):
        windows = dict()
        left, right = 0, 0
        ans = 0
        while right < len(nums):
            if nums[right] in windows:
                windows[nums[right]] += 1
            else:
                windows[nums[right]] = 1
            while len(windows) > k:
                windows[nums[left]] -= 1
                if windows[nums[left]] == 0:
                    del windows[nums[left]]
                left += 1
            ans += right - left + 1
            right += 1
        return ans

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.subarraysMostKDistinct(nums, k) - self.subarraysMostKDistinct(nums, k - 1)