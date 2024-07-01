'''
描述：给定一个数组
nums，元素值只有
0
0、
1
1、
2
2，分别代表红色、白色、蓝色。

要求：将数组进行排序，使得红色在前，白色在中间，蓝色在最后。

标准的双指针
把0放在最前，2放在最后面
1不进行操作
维护一个idx指针
一个right 指针
如果发现0
把左侧的换过来
idx + 0
如果发现是2
右侧的换过来
right - 1


https://algo.itcharge.cn/Solutions/0001-0099/sort-colors/#%E8%A7%A3%E9%A2%98%E6%80%9D%E8%B7%AF
pivot
'''

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        left , right = 0, len(nums) - 1  ## left代表是0元素的indx， 同理right代表2的index(从右开始）
        index = 0
        while index <= right: ## 如果index >right, 说明排序结束了
            if index < left: ##indx小于0的位置，所以可以无脑往前走
                index += 1
            elif nums[index] == 0 : #当前元素是0，把left 换过来
                nums[left],nums[index] = nums[index],nums[left]
                left += 1
            elif nums[index] == 2 : #当前元素是2 ，把right 换过来
                nums[right],nums[index] = nums[index],nums[right]
                right -= 1
            else:
                index += 1 ## we meet 1, we can just move indx

