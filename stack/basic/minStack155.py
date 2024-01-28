class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    # 5 , 3 ,4  ---> 5,3,3 (min) , pop 4 的时候 它对应的3 就会出来

    # 当我们push 的时候 把minStack 栈顶的拿出来 和当前值对比,这样 pop的时候永远是最小值,
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.minStack.append(val)
        else:
            self.stack.append(val)
            self.minStack.append(min(val,self.minStack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()


    def top(self) -> int:
        return  self.stack[-1]


    def getMin(self) -> int:
        return self.minStack[-1]


'''
利用不同的类结构来做
'''
class MinStack2:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    class Node:
        def __init__(self, x):
            self.val = x
            self.min = x

    def push(self, val: int) -> None:
        node = self.Node(val)
        if len(self.stack) == 0:
            self.stack.append(node)
        else:
            topNode = self.stack[-1]
            if node.min > topNode.min:
                node.min = topNode.min

            self.stack.append(node)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1].val

    def getMin(self) -> int:
        return self.stack[-1].min