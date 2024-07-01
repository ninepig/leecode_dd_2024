class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if not s[left].isalpha():
                left += 1
                continue #不能忘记了
            if not s[right].isalpha():
                right -=1
                continue #不能忘记了
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True