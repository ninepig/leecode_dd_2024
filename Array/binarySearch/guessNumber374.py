'''
经典二分法
'''


def guess(mid):
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        left , right = 0, n
        while left <= right :
            mid = left + (right - left) // 2
            guessNumber = guess(mid)
            if guessNumber == 1 :
                left = mid + 1
            elif guessNumber == -1 :
                right = mid - 1
            else:
                return mid

        return 0