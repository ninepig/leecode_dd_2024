class Solution:
    def guess(num: int) -> int:
        pass
    def guessNumber(self, n: int) -> int:
        left , right = 0, n
        while left <= right:
            mid = left + (right - left ) // 2
            if self.guess(mid) == 0:
                return mid
            elif self.guess(mid) == -1 :
                right = mid -1
            else:
                left = mid + 1

        return 0