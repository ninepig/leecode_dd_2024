'''
双指针
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s or len(s) == 0:
            return True
        left = 0
        right = len(s) - 1
        while left < right:
            if not s[left].isalpha():
                left += 1
            elif not s[right].isalpha():
                right -= 1
            else:
                if s[left].lower() != s[right].lower():
                    return False
                left +=1
                right -=1

        return True