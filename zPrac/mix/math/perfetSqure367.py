class Solution:
    ##binary way , approching way let could equal to right
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num
        while left < right:
            mid = left + (right - left) // 2
            if mid*mid == num:
                return True
            elif mid*mid < num:
                left = mid + 1
            else:
                right = mid - 1

        return left *left ==num # -1 means not exist