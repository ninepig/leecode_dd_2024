class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        size = len(nums)
        slow ,fast = 0 , 0
        while fast < size:
            if nums[fast] != val:
                # 交换 而不是赋值 做错了自己
                # nums[slow] = nums[fast]
                nums[slow],nums[fast] = nums[fast],nums[slow]
                slow += 1

            fast += 1
        # slow 就是长度 而不是slow+1
        return slow