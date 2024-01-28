import heapq

'''
使用一个大顶堆 queMax 记录大于中位数的数，使用一个小顶堆 queMin 小于中位数的数。

当添加元素数量为偶数： queMin 和 queMax 中元素数量相同，则中位数为它们队头的平均值。
当添加元素数量为奇数：queMin 中的数比 queMax 多一个，此时中位数为 queMin 的队头。
为了满足上述条件，在进行 addNum 操作时，我们应当分情况处理：

num > max{queMin}：此时 num 大于中位数，将该数添加到大顶堆 queMax 中。新的中位数将大于原来的中位数，所以可能需要将 queMax 中的最小数移动到 queMin 中。
num ≤ max{queMin}：此时 num 小于中位数，将该数添加到小顶堆 queMin 中。新的中位数将小于等于原来的中位数，所以可能需要将 queMin 中最大数移动到 queMax 中。'''
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lowerHalf = []
        self.topHalf = []


    def addNum(self, num: int) -> None:
        # 先放入下半部分
        if not self.lowerHalf or num < -self.lowerHalf[0]:
            heapq.heappush(self.lowerHalf,num)
            if len(self.lowerHalf) > len(self.lowerHalf) + 1:
                heapq.heappush(self.topHalf,-heapq.heappop(self.lowerHalf))
        else:
            heapq.heappush(self.topHalf,num)
            if len(self.topHalf) > len(self.lowerHalf):
                heapq.heappush(self.lowerHalf,-heapq.heappop(self.topHalf))

    def findMedian(self) -> float:
        if len(self.lowerHalf) > len(self.topHalf):
            return -self.lowerHalf[0]
        return  (-self.lowerHalf[0] + self.topHalf)/2