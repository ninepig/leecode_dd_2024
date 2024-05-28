from typing import List

'''
Leetcode 189 
rotate array

1 straight forward way

1 2 3 4 5 6 7  k = 3

5 6 7 1 2 3 4

get last 3 + first 4  with python slicing

2 traditional way
rotate all 
rotate first k 
rotate rest 
1 2 3 4 5 6 7 k =3 
7654321
567 1234 


learning TIP 
python
python could assign mul-value in the same time. it won't matter with order. Happen in same time


'''

class Solution:

    def __init__(self):
        pass

    def rotateWithSlicing(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        print(nums)

    def rotate(self,nums: List[int], k: int) -> None:
        k = k % len(nums)
        self.reverse(nums,0,len(nums) - 1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,len(nums) - 1)
        print(nums)

    def reverse(self,nums: List[int], start: int, end: int):
        while (start < end):
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotateWithTemp(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        tmp = nums[-k:]
        for idx in reversed(range(k, len(nums))):
            nums[idx] = nums[idx - k]

        for idx, num in enumerate(tmp):
            nums[idx] = num
nums = [1,2,3,4,5,6,7]
solu = Solution()
solu.rotate(nums,3)