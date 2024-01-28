class StockSpanner:
    ## 单调栈, 左侧第一个比当前元素的值, 同时我们需要记录span
    ## 左侧第一个 ---> 单调递增栈 外加 push当前元素时的栈顶元素
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and price > self.stack[-1][0]:
            temp = self.stack.pop()
            span += temp[1] # keep adding till we find left element
        # insert price
        self.stack.append((price,span))
        # we found target top, so we return span at that time
        return span

