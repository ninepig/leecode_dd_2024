'''
经典的双指针
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left , right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -=1
                continue

            if s[left].lower() == s[right].lower():
                right -= 1
                left +=1
                continue
            else:
                return False
        return True