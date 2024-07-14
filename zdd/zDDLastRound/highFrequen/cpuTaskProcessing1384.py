## 是一道task scheduler：给一串tasks，相对应的耗时，以及每个task最早可以被处理的时间，打印出每个task被处理的时间段。
## https://leetcode.com/problems/single-threaded-cpu/solutions/4181746/python-minheap-solution/
## 输出略有不同
## https://leetcode.cn/problems/single-threaded-cpu/solutions/913221/pai-xu-you-xian-dui-lie-pythonxu-yao-shi-hm73/
## 改进这道题的输出。 原题是输出index 现在是输出时间段 更简单一点

from typing import List
import heapq

'''
很小概率。 感觉是ml 的池子
'''

class Solution:
    # nlogn
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [[duration, i, start] for i, (start, duration) in enumerate(tasks)]
        tasks.sort(key=lambda x: (x[2]))                # 按照开始时间将各个任务排序
        time = tasks[0][2]                              # 当前时间
        res = []                                        # 最终结果
        queue = []                                      # 优先队列，先按照持续时间排序，后按照下标排序，最后按照开始时间排序
        n = len(tasks)                                  # 任务总数
        res_time_frame = []
        while len(res) != n:                            # 只要还没凑够n个任务，就要继续
            while tasks and tasks[0][2] <= time:    # 对于当前时间time，将tasks中所有开始时间小于等于time的任务入队
                heapq.heappush(queue, tasks.pop(0))       #
            if not queue:                               # 如果优先队列中没有任务，则快进到下一个任务开始时间
                time = tasks[0][2]
                continue
            duration, index, start = heapq.heappop(queue)   # 按照持续时间从低到高，下标从低到高的顺序，获取优先队列中的元素
            res.append(index)                           # 执行任务
            res_time_frame.append([time,time+duration])
            time = time + duration
            # 任务结束后的当前时间
        print(res)
        print(res_time_frame)
        return res


s = Solution()
# print(s.getOrder([[1,2],[2,4],[3,2],[4,1]]))
# print(s.getOrder([[7,10],[7,12],[7,5],[7,4],[7,2]]))
print(s.getOrder([[5,6],[9,4],[3,9],[3,7],[1,1],[6,9],[9,1]]))
# print(s.getOrder([[5,2],[7,2],[9,4],[6,3],[5,10],[1,1]]))
# print(s.getOrder([[19,13],[16,9],[21,10],[32,25],[37,4],[49,24],[2,15],[38,41],[37,34],[33,6],[45,4],[18,18],[46,39],[12,24]]))
