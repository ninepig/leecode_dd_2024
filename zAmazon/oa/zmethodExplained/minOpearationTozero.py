#https://www.fastprep.io/problems/amazon-minimum-operations-to-make-array-elements-zero
'''
In this problem, you are given an integer array and you need to perform some operations on the array to make all the elements equal to 0. In one operation, you can select a prefix of the given array and increment or decrement all the elements of the prefix by 1.

You have an array, arr, consisting of n integers. Find the minimum number of operations required to convert every element of this array to 0.

A prefix is a contiguous group of items that includes the first element in the cart. For example, [1], [1, 2], [1, 2, 3] etc are prefixes of [1, 2, 3, 4, 5].

Note: It is guaranteed that it is always possible to convert every element of the array to 0.
'''
from typing import List


'''
计算前面每个数的difference
然后取决于最后一个数的大小。 因为prefix是可以一起加减的 只有最后一个数是需要单独操作的
'''
class Solution:
    def amazonMinOperations(self, arr: List[int]) -> int:
        cur = arr[0]
        operations = 0
        for i in range(1, len(arr)):
            target = arr[i]
            operations += abs(cur - target)
            cur = target

        operations += abs(cur)
        return operations


test = [1,2,3]
sol = Solution()
print(sol.amazonMinOperations(test))