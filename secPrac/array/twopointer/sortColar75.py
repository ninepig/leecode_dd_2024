class Solution:
    ## 快速排序的思想...1是中间的pivot
    def sortColors(self, nums: List[int]) -> None:
        left = 0
        index = 0
        right = len(nums) - 1
        while index <= right: # stop loop when index bigger than right
            if index < left:
                index += 1 ## already swap with left, so need go to place not check
            elif nums[index] == 0:
                nums[left],nums[index] = nums[index],nums[left]
                left += 1
            elif nums[index] == 2:
                nums[right],nums[index] = nums[index],nums[right]
                right -= 1
            else:
                index += 1


