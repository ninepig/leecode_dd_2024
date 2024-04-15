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



观察
s means missing number
assumme we have every number  [0,s-1]  we can iterative visit x= num[i]
so we can get [x, x+s-1] every number

we sort nums ,
if x <= missing, so we can get every number from [0, x+s-1]
if x> missing, this means, we can not get missing. so we have to add some number to nums , using greedy
we add missing number, which we can get maximum is [0,2s - 1]

when missing number bigger than n, we get all number from [1,n]

链接：https://leetcode.cn/problems/patching-array/solutions/2551840/yong-gui-na-fa-zheng-ming-pythonjavacgo-mvyu1/

'''


class Solution:
  def minPatches(self, nums: list[int], n: int) -> int:
    miss, i, patches = 1, 0, 0
    while miss <= n:
        if i < len(nums) and nums[i] <= miss: ## if we can not find missing , then we need add that
            miss += nums[i] ## we can get every number from s+n[i] --> so missing += n[i]
            i += 1
        else:
            #max mum we can get is [missing, 2*missing -1]  since we add missing number 
            miss *= 2
            patches += 1
    return patches

test =[1,3]
n = 6
sol = Solution()
print(sol.minPatches(test,n))