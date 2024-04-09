'''
To solve this problem, we can use a greedy approach.
We start with a variable miss that represents the smallest number that
cannot be formed by summing up any combination of the numbers in the array.
Initially, miss is set to 1, since we can always form 1 by taking an empty combination.
We also initialize a variable i to 0, which represents the index of the next number that we need to consider adding to the array.

We then loop while miss is less than or equal to n,
 which means that we still need to add more numbers to the array.
 If i is less than the length of the array and the next number in the array is less than or equal to miss,
  we add that number to the sum and increment i.
  Otherwise, we add miss to the array and update miss to be the new smallest number that cannot be formed by
   summing up any combination of the numbers in the array.

The reason why this greedy approach works is that whenever we add a number to the array,
we can form all the numbers up to miss + number - 1. If we then update miss to be miss + number, we can now form all the numbers up to 2 * miss - 1. Therefore, we keep increasing miss until we can form all the numbers up to n.
https://leetcode.com/problems/patching-array/solutions/3242439/330-solution-with-step-by-step-explanation/




Explanation
大神解释
Let miss be the smallest sum in [0,n] that we might be missing. Meaning we already know we can build all sums in [0,miss).
Then if we have a number num <= miss in the given array, we can add it to those smaller sums to build all sums in [0,miss+num).
If we don't, then we must add such a number to the array, and it's best to add miss itself, to maximize the reach.
'''
class Solution:
  def minPatches(self, nums: list[int], n: int) -> int:
    miss, i, patches = 1, 0, 0
    while miss <= n:
        if i < len(nums) and nums[i] <= miss:
            miss += nums[i]
            i += 1
        else:
            miss *= 2
            patches += 1
    return patches