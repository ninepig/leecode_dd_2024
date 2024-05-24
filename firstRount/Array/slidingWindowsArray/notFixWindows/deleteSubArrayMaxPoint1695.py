class Solution:
    '''本质就是0003的变种'''
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left, right = 0 , 0
        size = len(nums)
        ans = -1
        windows_dict = dict()
        windows_sum = 0

        while right < size:
            windows_sum += nums[right]
            if nums[right] in windows_dict:
                windows_dict[nums[right]] += 1
            else:
                windows_dict[nums[right]] = 1

            while windows_dict[nums[right]] > 0:
                windows_sum -= nums[left]
                windows_dict[nums[left]] -= 1
                left -= 1

            ans = max(ans, windows_sum)
            right += 1

        return ans