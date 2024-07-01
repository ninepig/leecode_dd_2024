class Solution:
    '''
    滑动数组,subarray number 记得累加
    '''
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        windows_prod = 0
        left , right = 0,0
        ans = 0
        while right < len(nums):
            windows_prod *= nums[right]
            while windows_prod > k:
                windows_prod /= nums[left]
                left += 1

            ans += (right - left + 1)
            right += 1

        return ans