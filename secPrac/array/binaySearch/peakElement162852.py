class Solution:
    '''peak element
    binary search
    --> num[mid] < num[mid + 1] means uphill
    nums[mid] < num[mid-1] means downhill'''
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums : return -1
        size = len(nums)
        left , right = 0 , size -1
        # can get a specific number, so , we use <=
        while left <= right:
            mid = left + (right - left) //2
            # found a peak need consider mid -1 . mid +1 out of range problem TODO
            if nums[mid - 1 ]<nums[mid] > nums[mid + 1]:
                return mid
            if nums[mid] < nums[mid + 1]:
                # peak on right
                left = mid + 1
            else: # peak on left
                right = mid - 1

        return -1

    ## Same as 852
