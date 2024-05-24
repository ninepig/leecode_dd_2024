class MyCircularQueue:
    '''双指针queue design法 front + rear  size + 1 ---> cycle queue

    我们约定：self.size 为循环队列的最大元素个数。队头指针 self.front 指向队头元素所在位置的前一个位置，而队尾指针 self.rear 指向队尾元素所在位置。

初始化空队列：创建一个空队列，定义队列大小为 self.size + 1。令队头指针 self.front 和队尾指针 self.rear 都指向 0。即 self.front = self.rear = 0。
判断队列是否为空：根据 self.front 和 self.rear 的指向位置进行判断。根据约定，如果队头指针 self.front 和队尾指针 self.rear 相等，则说明队列为空。否则，队列不为空。
判断队列是否已满：队头指针在队尾指针的下一位置，即 (self.rear + 1) % self.size == self.front，则说明队列已满。否则，队列未满。
插入元素（入队）：先判断队列是否已满，已满直接抛出异常。如果不满，则将队尾指针 self.rear 向右循环移动一位，并进行赋值操作。此时 self.rear 指向队尾元素。
删除元素（出队）：先判断队列是否为空，为空直接抛出异常。如果不为空，则将队头指针 self.front 指向元素赋值为 None，并将 self.front 向右循环移动一位。
获取队头元素：先判断队列是否为空，为空直接抛出异常。如果不为空，因为 self.front 指向队头元素所在位置的前一个位置，所以队头元素在 self.front 后一个位置上，返回 self.queue[(self.front + 1) % self.size]。
获取队尾元素：先判断队列是否为空，为空直接抛出异常。如果不为空，因为 self.rear 指向队尾元素所在位置，所以直接返回 self.queue[self.rear]。
    '''

    def __init__(self, k: int):
        self.front = 0
        self.rear = 0
        self.size = k + 1
        self.queue = [ 0 for _ in range(self.size)]

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        #环形 取 mod 来找位置
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.front = (self.rear + 1) % self.size
        return True


    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.queue[(self.front + 1) % self.size]

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.queue[(self.rear + 1) % self.size]

    def isEmpty(self) -> bool:
        return self.front == self.rear

    def isFull(self) -> bool:
        return (self.rear + 1) % self.size == self.front
