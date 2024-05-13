import collections

# 基本的 anagram题 用collection counter 即可

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False

        return collections.Counter(s) == collections.Counter(t)