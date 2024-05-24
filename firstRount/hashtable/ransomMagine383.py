from collections import Counter


class Solution:
    '''
    判断 ransomNote 能不能由 magazines 里面的字符构成。如果可以构成，返回 True；否则返回 False
    counter计数
    '''
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magaCounter = Counter(magazine)

        for i in ransomNote:
            if ransomNote[i] not in magaCounter:
                return False
            else:
                magaCounter[ransomNote[i]] -= 1
                if magaCounter[ransomNote] < 0:
                    return False

        return True

    # 不用counter
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_counts = [0 for _ in range(26)]

        for ch in magazine:
            num = ord(ch) - ord('a')
            magazine_counts[num] += 1

        for ch in ransomNote:
            num = ord(ch) - ord('a')
            if magazine_counts[num] == 0:
                return False
            else:
                magazine_counts[num] -= 1

        return True