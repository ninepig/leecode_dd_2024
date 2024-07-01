class Solution:
    '''因为search range 所以要用排除法'''
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) <= 0 :
            return [-1,-1]
        size = len(nums)
        left , right = 0 , size -1
        ans = [-1,-1]

        # located left
        while left < right :
            mid = left + (right - left) //2
            ## focus on left side , 左侧第一个出现
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        if nums[left] != target:
            return ans

        ans[0] = left

        left , right = 0 , size -1
        while left < right:
            mid = left + (right - left)//2
            ## focus on right side,右侧第一个出现
            ## left == right -->end loop
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid

        if nums[left] == target:
            nums[1] = target

        return ans
