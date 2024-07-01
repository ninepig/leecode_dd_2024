class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left < right :
            mid = left + (right - left) //2
            temp = mid * mid
            if temp== x:
                return mid
            elif temp > x:
                right = mid + 1
            else:
                left = mid - 1

        return left ## approaching way

class Solution:
    # we want first on left side
    def mySqrtApproching(self, x: int) -> int:
        left = 0
        right = x
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans