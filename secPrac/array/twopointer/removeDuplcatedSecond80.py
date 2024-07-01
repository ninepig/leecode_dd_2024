'''
输入：nums = [1,1,1,2,2,3]
输出：5, nums = [1,1,2,2,3]
解释：函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3。 不需要考虑数组中超出新长度后面的元素。
输入：nums = [0,0,1,1,1,1,2,3,3]
输出：7, nums = [0,0,1,1,2,3,3]
解释：函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3。不需要考虑数组中超出新长度后面的元素。



元素最多只允许出现2次
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0 :
            return 0
        size = len(nums)
        write_index = 0
        slow_index = 0
        while slow_index < size:
            fast = slow_index
            while fast < size and nums[fast] == nums[slow_index]:
                fast += 1
            nums[write_index] = nums[slow_index]
            write_index += 1

            if fast - slow_index > 1 :
                nums[write_index] = nums[slow_index]
                write_index += 1

            slow_index = fast

        return write_index

    # 双指针
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        if size <= 2:
            return size
        slow, fast = 2, 2
        while (fast < size):
            if nums[slow - 2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow