'''数学死记硬背题
base digit  numberCount start
9    1          9         1
90   2         180       10
900  3        2700       100
9000 4       3600        1000


1 先找出base, 算出digit
2 找出对应的number  start + (n-1)/digit
3 找出index (n-1)%digit


'''
class Solution:
    # n is digit
    #
    def findNthDigit(self, n: int) -> int:
        digit = 1
        start = 1
        base = 9
        while n > base:
            n -= base
            digit += 1
            start *= 10
            base = start *digit *  9 # 9--->90--900

        number = start + (n-1)//digit   # 找到第几个数
        index = (n-1) % digit           # 找到这个数里的index

        return int(str(number)[index])