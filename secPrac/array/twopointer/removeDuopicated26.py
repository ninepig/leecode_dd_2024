class Solution:
    ## 这种三指针 可以做成模板了
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
            slow_index = fast

        return write_index


    def removeDuplicatesAnswer(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        slow, fast = 0, 1

        while (fast < len(nums)):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1

        return slow + 1