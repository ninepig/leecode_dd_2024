'''
You are given an array arr which consists of only zeros and ones,
 divide the array into three non-empty parts such that all of these parts represent the same binary value.

If it is possible, return any [i, j] with i + 1 < j, such that:

arr[0], arr[1], ..., arr[i] is the first part,
arr[i + 1], arr[i + 2], ..., arr[j - 1] is the second part, and
arr[j], arr[j + 1], ..., arr[arr.length - 1] is the third part.
All three parts have equal binary values.
If it is not possible, return [-1, -1].

Note that the entire part is used when considering what binary value it represents.
For example, [1,1,0] represents 6 in decimal, not 3. Also, leading zeros are allowed, so [0,1,1] and [1,1] represent the same value.
'''
class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        # count number of ones
        ones = sum(arr)
        if ones % 3 != 0:
            return [-1, -1]
        elif ones == 0:  # special case: all zeros
            return [0, 2]

        # find the start index of each group of ones
        ## 因为 1出现的个数肯定是3的倍数， 所以 3个 1开始的起点是我们要找的目标
        c = 0
        starts = []
        for i, d in enumerate(arr):
            if d == 1:
                if c % (ones // 3) == 0:
                    starts.append(i)
                c += 1

        # scan the groups in parallel to compare digits
        i, j, k = starts
        while k < len(arr):  # note that the last/rightmost group must include all digits till the end
            if arr[i] == arr[j] == arr[k]:
                i += 1
                j += 1
                k += 1
            else:
                return [-1, -1]
        return [i - 1, j]