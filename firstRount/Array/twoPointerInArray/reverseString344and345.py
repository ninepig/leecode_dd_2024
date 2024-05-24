class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left , right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return None

    def reverseVowels(self, s: str) -> str:

        vowels = ['a','e','i','o','u']

        left , right = 0, len(s) - 1
        while left < right:
            while left < right:
                if not str.lower(s[left]) in vowels:
                    left += 1
                    continue
            while left < right :
                if not str.lower(s[left]) in vowels:
                    right -= 1
                    continue
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return s