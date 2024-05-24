class StockSpanner:

    def __init__(self):
        self.stack = []
    '''
    这道题转化为 左侧第一个比右侧大的
    所以递增栈,即将出栈的元素就是我们的目标元素
    公式
    '''
    def next(self, price: int) -> int:
        span = 1
        while self.stack and price >= self.stack[-1][0]:
            top = self.stack.pop()
            span += top[1]
        self.stack.append([price, span])
        return span