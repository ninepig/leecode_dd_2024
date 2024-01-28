import collections


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counter = collections.Counter(s)
        val = 0
        for value in counter.values():
            if val == 0:
                val = value
            elif val != value:
                return False

        return True