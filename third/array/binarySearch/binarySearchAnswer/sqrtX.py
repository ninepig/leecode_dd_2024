class Solution:
    '''
    2分 简单 应用题

    '''
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x
        while left <= right:
            mid = left + (right - left) //2
            if mid * mid <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans