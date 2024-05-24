class Solution:
    '''描述：给定两个字符串 a 和 b。

要求：寻找重复叠加字符串 a 的最小次数，使得字符串 b 成为叠加后的字符串 a 的子串，如果不存在则返回 -1。
不断重复 重复 a, 直到长度 大于b 然后看b是否存在
'''
    def repeatedStringMatch(self, a: str, b: str) -> int:
        count = 1
        len_b = len(b)
        len_a = len(a)
        s = a
        len_s = len_a
        while len_s < len_b:
            s = s + a
            len_s = len(s)
            count += 1

        if s.find(b) != -1:
            return count

        return -1

        # a ="abcd" b ="cdabcdab"
        # handle rotation https://leetcode.com/problems/repeated-string-match/solutions/108086/java-solution-just-keep-building-oj-missing-test-cases/
        ## second
        s = s + a
        count += 1
        if s.find(b)!= -1:
            return count
        return -1
