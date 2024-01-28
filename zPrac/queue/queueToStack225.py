class MyStack:

    def __init__(self):
        self.pushQueue = []
        self.popQueue = []

    # 非常巧妙的方法 画图一目了然
    # pushQueue push以后，把popqueue有的都连到尾部， 最后交换push pop
    def push(self, x: int) -> None:
        self.pushQueue.append(x)
        while self.popQueue:
            self.pushQueue.append(self.popQueue.pop(0)) # push what popQueue have from left to the end of push queue
        self.pushQueue , self.popQueue = self.popQueue , self.pushQueue

    def pop(self) -> int:
        return self.popQueue.pop(0)

    def top(self) -> int:
        return self.popQueue[0]

    def empty(self) -> bool:
        return len(self.popQueue) == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()