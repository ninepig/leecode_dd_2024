
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        size = len(nums)
        rotation = k % size
        self.reverse(nums,0,size-1)
        self.reverse(nums,0,rotation-1)
        self.reverse(nums,rotation,size - 1)

    def reverse(self, nums, start, end):
        while start < end:
            tmp = nums[start]
            nums[start] = nums[end]
            nums[end] = tmp
            start += 1
            end -=1

'''
没有考虑到可以大于n的长度
不要用小技巧,就是纯纯的手写就行了
o(n)
inplace 
space o(1)
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)

    def reverse(self, nums: List[int], left: int, right: int) -> None:
        while left < right :
            tmp = nums[left]
            nums[left] = nums[right]
            nums[right] = tmp
            left += 1
            right -= 1