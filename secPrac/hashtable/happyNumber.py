class Solution:
    '''
    编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」 定义为：

对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果这个过程 结果为 1，那么这个数就是快乐数。
如果 n 是 快乐数 就返回 true ；不是，则返回 false

n = 19
next = 1^2 + 9^2
    '''

    # 利用dict来保存是否出现过计算的 避免计算
    def isHappy(self, n: int) -> bool:
        store_map = []

        while n != 1:
            new_n = self.cal_digit(n)
            if new_n in store_map:
                return False
            store_map[n] = new_n
            n = new_n
        return True

    def cal_digit(self, n):
        res = 0
        while n > 0  :
            digit = n % 10
            n /= 10
            res += digit * digit
        return res


# 答案
    class Solution:
        def getNext(self, n: int):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum

        def isHappy(self, n: int) -> bool:
            num_set = set()
            while n != 1 and n not in num_set:
                num_set.add(n)
                n = self.getNext(n)
            return n == 1