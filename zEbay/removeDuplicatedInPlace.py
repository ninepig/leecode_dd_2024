# Write a program to remove duplicates from a sorted array in place
class solution:
    def removeSortedArray(self,nums:list[int]):
        if not nums or len(nums) == 0:
            return nums
        slow, fast = 0, 1
        while fast in range(len(nums)):
            if nums[slow] == nums[fast]:
                fast += 1
            else:
                nums[slow + 1] = nums[fast]
                fast += 1
                slow += 1

        # return slow + 1
        return nums ## only slow + 1 has useful data , rest is useless