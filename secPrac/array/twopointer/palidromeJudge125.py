class Solution:
    '''
    consider lowercase and digit
    '''
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            # if str.isalpha(s[left]) and str.isalpha(s[right]):
            #     if str.lower(s[left]) != str.lower(s[right]):
            #         return False
            #     else:
            #         left += 1
            #         right -= 1
            # elif str.isdigit(s[left]) and str.isdigit(s[right])
            if not s[left].isalnum():
                left += 1
                continue
            if not s[left].isalnum():
                right -= 1
                continue

            if s[left].lower() == s[right].lower():
                left+=1
                right -=1
            else:
                return False

        return True