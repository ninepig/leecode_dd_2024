'''
给你一个restaurant list，让你从头到尾给这些restaurant打广告，
两个相同的restaurant之间有冷冻期，每天只能给一个restaurant打广告，求给所有restaurant打完广告要多少天
这个题应该就是 他们说的shecudle 1/2
'''
import collections


## 621 --> n means duration
##--> max means most number of task
## --> tot means how many task is equal to max
## --> math.max(len(tasks), (max - 1)*(n + 1) + tot
# def leastInterval(self, tasks: list[str], n: int) -> int:
#     cnts = [0] * 26
#     for c in tasks:
#         cnts[ord(c) - ord('A')] += 1
#     maxv, tot = 0, 0
#     for i in range(26):
#         maxv = max(maxv, cnts[i])
#     for i in range(26):
#         tot += 1 if maxv == cnts[i] else 0
#     return max(len(tasks), (n + 1) * (maxv - 1) + tot)

def leastDays(self, ads:list[str], coolDown:int) -> int:
    counter = collections.Counter(ads)
    max_ads = max(counter.values()) ## the most number of ads
    task_max_count = 0
    for value in counter.values():
        if value == max_ads:
            task_max_count += 1

    return max(len(ads),(max_ads - 1 ) * (coolDown + 1) + task_max_count)


'''
给你一个下标从 0 开始的正整数数组 tasks ，表示需要 按顺序 完成的任务，其中 tasks[i] 表示第 i 件任务的 类型 。
同时给你一个正整数 space ，表示一个任务完成 后 ，另一个 相同 类型任务完成前需要间隔的 最少 天数。
在所有任务完成前的每一天，你都必须进行以下两种操作中的一种：
1 完成 tasks 中的下一个任务
2 休息一天
请你返回完成所有任务所需的 最少 天数。
'''

## 不知道会以什么形式出 如果是按照顺序打广告 那就是应该这么做
## 贪心 维护一个最后出现的日子
def taskSchedulerII(self, tasks: list[int], space: int) -> int:
    ans, last = 0, {}
    for t in tasks:
        ans += 1  # 完成该任务，天数+1
        if t in last:
            ##对于 t 最小的当前天 取决于 上次出现 + space + 1 或者现在那天大 ，选大的
            ans = max(ans, last[t] + space + 1)  # 看看是否要间隔 space 天
        last[t] = ans  # 记录上一次完成时间
    return ans

