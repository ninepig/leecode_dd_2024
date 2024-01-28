'''这道题就是next permutation'''
from typing import List


class Solution:
    # 越界问题
    def nextGreaterElement(self, target: int) -> int:
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums = [int(x) for x in str(target)]
        n = len(nums)
        i = n - 1

        # 127431
        #从后往前扫描，找到第一个降序的 2
        # 把2后面的 reverse
        # 121347
        # 找到第一个比2大的， 3
        # 交换 131247 这个就是next permutation 。不难 就是公式
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1

        if i == 0:
            return - 1

        self.reverse(nums, i, n - 1)
        if i > 0:
            for j in range(i, n):
                if nums[j] > nums[i - 1]:
                    self.swap(nums, i - 1, j)
                    break

        res = sum(d * 10 ** i for i, d in enumerate(nums[::-1]))
        return res if res < 2 ** 31 else -1 #越界 很重要

    def reverse(self, nums, i, j):
        while i < j :
            nums[i],nums[j] = nums[j],nums[i]
            i += 1
            j -= 1

    def swap(self, nums, i, j):
        """
        contains i and j.
        """
        nums[i], nums[j] = nums[j], nums[i]


    '''
    previous permutation
    13245 
    从后往前找 第一个 num[i-1] > num[i]的。 最大的i值
    找到3
    然后把3往后的reverse 
    13542
    然后把3 和 2交换（第一个比他小的数） ，就和next permutation相反
    12543 这个就是previous permutation了
    '''
    def previousSmallerElement(self, target: int) -> int:
        nums = [int(x) for x in str(target)]
        n = len(nums)
        i = n - 1
        idx = 0
        while i > 0 :
            if nums[i - 1] > nums[i]:
               idx = i - 1
               break
            i -= 1
        if i == 0 :
            return -1 # no previous permutation

        ## reverse number from idx
        self.reverse(nums,idx + 1 , n - 1)
        ## search first element smaller than num[idx]
        for j in range(idx+1, n):
            if nums[j] < nums[idx]:
                self.swap(nums,j,idx) # sawp 3 and 2
                break

        res = sum(d * 10 ** i for i, d in enumerate(nums[::-1]))
        return res

    ## 1053
    '''因为只能换一次
    13245
    同样先找到3 
    13245 因为只能换一次， 所以就从后面开始找 找到最高位，比3小的换
    12345 只能做到这个
    12543 没办法做到这个 
    '''
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr

        n = len(arr)
        # Traverse in reversed order.
        # Stop when you find the first nondecreasing number (from the perspective of the reversed traversal).
        for i in reversed(range(0, n - 1)):
            if arr[i] > arr[i + 1]:
                break
        # If `i` has surpassed arr's lower index bound, that means the array is sorted. Return arr.
        if i < 0:
            return arr
        # Traverse in reversed order. Find the largest j that is less than A[i].
        for j in reversed(range(i, n)):
            # If there are duplicate largest nums, keep decrementing j until you reach the leftmost idx of the duplicates.
            if arr[j] < arr[i] and arr[j] != arr[j - 1]:
                break
        # Swap.
        arr[i], arr[j] = arr[j], arr[i]

        return arr


solution = Solution()
test = 13245
# print(solution.nextGreaterElement(test))
print(solution.previousSmallerElement(test))