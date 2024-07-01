class Solution:
    '''

    找规律 1--9 有9个数 9*1 9位
    10--99  90个树 180位
    100--999 900个数 900*3 2700 位置

        找到第n位数 所在的digit
        找到开始的digit
        在计算出所在整数 number 对于当前start是第几位
    '''
    def findNthDigit(self, n: int) -> int:
        digit = 1
        start = 1
        base = 9
        while n > base:
            n -= base
            digit += 1
            start *= 10
            base = start * digit * 9

        number = start + (n - 1) // digit
        digit_idx = (n - 1) % digit
        return int(str(number)[digit_idx])
