class MyCircularQueue:

    '''利用两根指针 小技巧题'''
    def __init__(self, k: int):
        self.capacity = k
        self.front = 0
        self.rear = 0
        self.array = [ 0 for _ in range(self.capacity)]


    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.capacity
        self.array[self.rear] = value
        return True


    # deque 就是移动指针 ， 不需要对数组进行操作
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return  self.array[self.front%self.capacity]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return  self.array[self.rear%self.capacity]


    def isEmpty(self) -> bool:
        return self.front == self.rear


    def isFull(self) -> bool:
        return (self.rear + 1) % self.capacity == self.front % self.capacity
