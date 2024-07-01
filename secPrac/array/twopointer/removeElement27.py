class Solution:
    '''基本双指针'''
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums or len(nums) == 0:
            return 0
        slow = 0
        fast = 0
        size = len(nums)
        while fast < size:
            if nums[fast] == val:
                fast += 1
            else:
                nums[slow] = nums[fast]
                slow +=1
                fast +=1

        return slow