from collections import Counter

'''很少见 就一个ml面试出了 应该不可能'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cntr, w, matched = Counter(s1), len(s1), 0

        for i in range(len(s2)):
            if s2[i] in cntr:
                cntr[s2[i]] -= 1
                if cntr[s2[i]] == 0:
                    matched += 1
            if i >= w and s2[i-w] in cntr:
                if cntr[s2[i-w]] == 0:
                    matched -= 1

            if matched == len(cntr):
                return True

        return False