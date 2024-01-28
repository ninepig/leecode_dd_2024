from collections import deque

class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if self.empty(): return -1

        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

        return self.queue.pop()


    def top(self):
        """
        :rtype: int
        """
        if self.empty(): return -1

        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
        x = self.queue.popleft()
        self.queue.append(x)

        return x


    def empty(self):
        """
        :rtype: bool
        """
        return  bool(self.queue)