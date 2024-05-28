## leetcode 901
'''
单调栈
找左侧比第一个比当前节点大的value
对于单调递增栈
左侧第一个比他大的。就是当当前元素入栈的时候的元素，栈顶的元素
所以逻辑是每次栈顶被pop的时候记录时间。 利用stack元素类型（ values，span） 来做


'''
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1] < price:
            top = self.stack.pop()
            span += top[1]
        self.stack.append([price, span])

        return span




