from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ## using 3 pointers to do this
        ## left, right , index
        ## if we found left is a 0 , we move that to right
        ## if we found left is not a 0, indx ++
        # if not nums or len(nums) == 0:
        #     return
        # size = len(nums)
        # left , right , idx = 0,size - 1,0
        # while idx < right :## stop when we reach right , right always point to 0
        #     if nums[left] == 0:
        #         nums[left] , nums[right] = nums[right],nums[left]
        #         right -= 1
        #         ## we can confirm right is 0
        #     else:
        #         idx += 1
        #         left += 1

        ## 没仔细读题，这个题要求其他的保持相对的顺序，那就不能left right 换了
        ## 这个就是个双指针 index题
        ## 利用原数组当返回空间的做法 节省空间

        if not nums or len(nums) == 0:
            return
        size = len(nums)
        left,idx = 0,0
        for i in range(size):
            if nums[left] != 0:
                nums[idx] = nums[left]
                idx += 1
            left += 1

        ## fill 0, idx to size
        for i in range(idx,size):
            nums[i] = 0



