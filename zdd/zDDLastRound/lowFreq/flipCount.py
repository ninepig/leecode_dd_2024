'''
还有一道是新题。大概意思是有一个数组，可以set（所有元素变成1）， unset（所有元素变成0），flip（所有1变成0,0变成1），问怎么用O（1）来实现这个几个操作。
基本解题思路是，我们不可以用数组来记录真是的数值，因为这样子子flip就是O（N）。我们用一个全局变量来记录flip的奇偶性，
然后数组就记录真实值和flip的区别，the real value at index i = （flip_count + value at index i ）% 2
https://leetcode.com/problems/design-bitset/solutions/1748431/python3-java-c-all-operations-o-1-flipped-string-flip-flag/


实际题目 如果有set  unset 也就是全部置1 or 0的操作 其实就不需要
'''


class Bitset:
    '''
    一个是否flip的flag
    一个记录多少ones的varibale
    '''
    def __init__(self, size: int):
        self.l = [0] * size
        self.ones = 0
        self.flipp = False

    ## 如果有flip 我们如果是1 那就+1， 同时设为0
    ## 如果没有flip 我们是0 那就+1， 同时设为1
    def fix(self, idx: int) -> None:
        if self.flipp:
            if self.l[idx] == 1: self.ones += 1
            self.l[idx] = 0
        else:
            if self.l[idx] == 0: self.ones += 1
            self.l[idx] = 1

    def unfix(self, idx: int) -> None:
        if self.flipp:
            if self.l[idx] == 0: self.ones -= 1
            self.l[idx] = 1
        else:
            if self.l[idx] == 1: self.ones -= 1
            self.l[idx] = 0

    ## 其实 这两个不需要数组
    def set(self) -> None:
        self.flipp = False
        self.ones = len(self.l)

    def unset(self)-> None:
        self.flipp = False
        self.ones = 0

    def flip(self) -> None:
        self.flipp = not self.flipp
        self.ones = len(self.l) - self.ones

    def all(self) -> bool:
        return self.ones == len(self.l)

    def one(self) -> bool:
        return self.ones > 0

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        return ''.join([str(0 if i else 1) for i in self.l]) if self.flipp else ''.join([str(i) for i in self.l])