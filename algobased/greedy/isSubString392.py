class Solution:

    # subsequeence.. 不是string
    # 所以要一个一个比较,看看能否达到s的尾部
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) < len(t):
            return False

        size_s =len(s)
        size_t = len(t)
        i , j = 0, 0
        while i < size_t and j < size_s:
            if s[i] == s[j]:
                i += 1
            j += 1

        return i == size_s

class SolutionAns:
    def isSubsequence(self, s: str, t: str) -> bool:
        size_s = len(s)
        size_t = len(t)
        i, j = 0, 0
        while i < size_s and j < size_t:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == size_s