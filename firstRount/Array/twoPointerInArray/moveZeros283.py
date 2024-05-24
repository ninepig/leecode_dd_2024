
'''
最基本的快慢指针题
无论如何0都会到最后 遍历完以后
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow , fast = 0 ,  0
        for i in range(len(nums)):
            if nums[fast] != 0:
                nums[slow],nums[fast] = nums[fast],nums[slow]
                slow += 1
            fast += 1
