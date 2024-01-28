class Solution:
    # 空间 o(1) without modify num, uses only constant extra space.
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]

        return -1
    # binary search way
    def findDuplicate(self, nums: List[int]) -> int:
        size = len(nums)
        left = 1
        right = size -1
        while left < right:
            mid = left + (right - left) // 2
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
            if cnt <= mid : # target number on right , approaching method
                left = mid + 1
            else:
                right = mid
        return left
    
    # treat nums as a fast/slow list, repeated mumber means cycle in array list
    # treat as cycle list list
    def  findDuplicateFastSlow(self, nums: List[int]) -> int:
        slow, fast = nums[0],nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[slow]]

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
