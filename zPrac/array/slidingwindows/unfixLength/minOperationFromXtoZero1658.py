class Solution:
    '''sliding windows + brainstrom

    a a2 a3 a4 a5 a6
    find largest windows in array sum = sum(array) - x
    '''
    def minOperations(self, nums: List[int], x: int) -> int:
        res = float('inf')
        windows_sum = 0
        left,right = 0,0
        target = sum(nums) - x
        while right < len(nums):
            windows_sum += nums[right]

            while windows_sum > target:
                windows_sum -= nums[left]
                left += 1

            if windows_sum == target:
                ans = max(ans,right - left + 1)

            right +=1

        return len(nums) - res if res != float('inf') else -1