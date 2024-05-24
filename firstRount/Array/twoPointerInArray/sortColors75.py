from typing import List

'''
双指针 + 模拟过程
使用两个指针 left、right，分别指向数组的头尾。left 表示当前处理好红色元素的尾部，right 表示当前处理好蓝色的头部。
再使用一个下标 index 遍历数组，如果遇到 nums[index] == 0，就交换 nums[index] 和 nums[left]，同时将 left 右移。如果遇到 nums[index] == 2，就交换 nums[index] 和 nums[right]，同时将 right 左移。
直到 index 移动到 right 位置之后，停止遍历。遍历结束之后，此时 left 左侧都是红色，right 右侧都是蓝色。'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left , right = 0, len(nums) - 1
        index = 0
        while index <= right:
            if index < left:
                index += 1
            elif nums[index] == 0:
                nums[index],nums[left] = nums[left],nums[index]
                left += 1
            elif nums[index] == 2:
                nums[index],nums[right] = nums[right],nums[index]
                right -= 1
            else:
                index +=1
            