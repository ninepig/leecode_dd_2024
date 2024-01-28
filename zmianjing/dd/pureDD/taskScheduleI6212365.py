from collections import Counter

class Solution:
    '''脑经急转弯题
    https://leetcode.cn/problems/task-scheduler/solutions/1924711/by-ac_oier-3560
    如果我们有个m个相同的任务
    前m-1个需要等待n时间 所以总共的时间 为（m-1）*（n+1） + 1 的时间
    假设最多的任务是 max。 有tot个max数量的任务
    剩余的任务就是塞在这个max任务之中解决
    所以时间的就是 数组的长度 vs （m-1）*（n+1）+tot ， tot个任务 就是在n+1个里塞不进去，塞在队尾
    '''
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnts = [0] * 26
        for c in tasks:
            cnts[ord(c) - ord('A')] += 1
        maxv, tot = 0, 0
        for i in range(26):
            maxv = max(maxv, cnts[i])
        for i in range(26):
            tot += 1 if maxv == cnts[i] else 0
        return max(len(tasks), (n + 1) * (maxv - 1) + tot)


    #https://leetcode.cn/problems/task-scheduler/solutions/10379/python-xiang-jie-by-jalan
    def leastInterval2(self, tasks: List[str], n: int) -> int:
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        length = len(tasks)
        if length <= 1:
            return length

        # 用于记录每个任务出现的次数
        task_map = dict()
        for task in tasks:
            task_map[task] = task_map.get(task, 0) + 1
        # 按任务出现的次数从大到小排序
        task_sort = sorted(task_map.items(), key=lambda x: x[1], reverse=True)

        # 出现最多次任务的次数
        max_task_count = task_sort[0][1]
        # 至少需要的最短时间
        res = (max_task_count - 1) * (n + 1)

        for sort in task_sort:
            if sort[1] == max_task_count:
                res += 1

        # 如果结果比任务数量少，则返回总任务数
        # 这种情况其实不能叫做特殊情况，而是一大类。整个题目解法存在两类：1.
        # 任务执行过程中存在冷却这种情况。2.
        # 不存在冷却这种情况。 楼主【特殊情况】实际上是不存在冷却这一大类。
        return res if res >= length else length


class Solution:
    ## 简单易懂。。。太直接了
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        ans, last = 0, {}
        for t in tasks:
            ans += 1  # 完成该任务，天数+1
            if t in last:
                ans = max(ans, last[t] + space + 1)  # 看看是否要间隔 space 天
            last[t] = ans  # 记录上一次完成时间
        return ans
