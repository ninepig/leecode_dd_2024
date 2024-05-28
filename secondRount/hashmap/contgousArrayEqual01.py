'''
Initialize a hash map to store prefix sums along with their indices.
Initialize variables for sum, maximum subarray length, and iterate through the input array.
For each element in the array, update the sum according to the element (decrement by 1 for 0, increment by 1 for 1).
If the sum becomes zero at any index, update the maximum length to the current index plus one.
If the sum is encountered again (which means there is a subarray with equal 0s and 1s between the previous occurrence and the current index), update the maximum length if the current subarray length is greater than the previously stored maximum length.
Return the maximum subarray length.

https://leetcode.com/problems/contiguous-array/description/
leetcode 525
'''

class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        mp = {}
        sum_val = 0
        max_len = 0
        for i, num in enumerate(nums):
            sum_val += 1 if num == 1 else -1
            if sum_val == 0:
                max_len = i + 1
            elif sum_val in mp:
                max_len = max(max_len, i - mp[sum_val])
            else:
                mp[sum_val] = i
        return max_len