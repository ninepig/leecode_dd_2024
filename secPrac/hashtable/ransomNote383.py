import collections


class Solution:
    '''
    给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。

    如果可以，返回 true ；否则返回 false 。
    '''
    # 用conuter
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter_ransom = collections.Counter(ransomNote)
        magazine_ransom = collections.Counter(magazine)

        for key,value in counter_ransom.items():
            if key not in magazine_ransom:
                return False
            else:
                if value > magazine_ransom[key]:
                    return False
        return True

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