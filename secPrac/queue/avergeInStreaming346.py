from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        self.array = []
        self.sum = 0
        self.size = size



    def next(self, val: int) -> float:
        self.array.append(val)
        self.sum += val
        if len(self.array) <= self.size:
            return self.sum // len(self.array)
        else:
            num = self.array.pop(0)
            self.sum -= num
            return self.sum // self.size

    # 答案
    # def next(self, val: int) -> float:
    #     if len(self.queue) < self.size:
    #         self.queue.append(val)
    #     else:
    #         if self.queue:
    #             self.sum -= self.queue[0]
    #             self.queue.pop(0)
    #         self.queue.append(val)
    #     self.sum += val
    #     return self.sum / len(self.queue)