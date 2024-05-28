'''
sure trust and safety group
这个贪心法真的太漂亮了，

You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.
https://leetcode.com/problems/maximum-swap/description/

'''


class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = list(str(num))

        i = 0
        ## find decreasing flip point
        while i < len(s) - 1:
            if s[i] < s[i + 1]:
                break
            i += 1

        if i == len(s) - 1:
            return num

        ## find max on right which can be used to flip
        max_idx, max_val = i + 1, s[i + 1]
        for j in range(i + 1, len(s)):
            if s[j] >= max_val:
                max_val = s[j]
                max_idx = j

        ## find most left value smaller than max which means can be swtich
        min_idx = i
        for j in range(i, -1, -1):
            if s[j] < max_val:
                min_idx = j

        s[min_idx], s[max_idx] = s[max_idx], s[min_idx]
        return int(''.join(s))