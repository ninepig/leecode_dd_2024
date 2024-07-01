class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # self.stack.append(val)
        # # if val is smaller than min so far , pop that
        # while self.min_stack and self.min_stack[-1] > val:
        #     self.min_stack.pop(-1)
        # self.min_stack.append(val) # which means a monotonic increasing stack

        ## 这样做更方便点,只需要在插入时候考虑,minStack 不考虑单调栈,只放入当前最小值. 不需要单调栈就行了,也就是每次都会把最小值插入

        if not self.stack:
            self.stack.append(val)
            self.min_stack.append(val)
        else:
            self.stack.append(val)
            self.min_stack.append(min(val, self.min_stack[-1])) #每次都会把最小值插入

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# 在常数时间内检索到最小元素的栈。