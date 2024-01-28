from collections import Counter


class Solution:
    # 最简单的方法 排序
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counterS = Counter(s)

        for c in t:
            if c in counterS and counterS[c] != 0 :
                counterS[c] -= 1
            else:
                return False

        return True


