class Solution:
    '''
    基本题
    双指针 ---》 回文数
    '''
    def isPalindrome(self, s: str) -> bool:
        size = len(s)
        left , right = 0 , size - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue

            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False

        return True
