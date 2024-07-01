import heapq
from bisect import bisect_right, bisect, bisect_left

##
# https://leetcode.com/problems/maximum-profit-in-job-scheduling/solutions/1430983/python-from-brute-force-to-dp-binary-search-clean-concise/

# not binary
# https://leetcode.cn/problems/maximum-profit-in-job-scheduling/solutions/597016/python3-dong-tai-gui-hua-er-fen-cha-zhao-ovu5/

# binary https://leetcode.cn/problems/maximum-profit-in-job-scheduling/solutions/1913089/dong-tai-gui-hua-er-fen-cha-zhao-you-hua-zkcg/
from math import inf
from typing import List


class solution:
    '''
    You're a dasher, and you want to try planning out your schedule. You can view a list of deliveries along with their associated start time, end time, and dollar amount for completing the order.
     Assuming dashers can only deliver one order at a time, determine the maximum amount of money you can make from the given deliveries.
    The inputs are as follows:
    int start_time: when you plan to start your schedule
    int end_time: when you plan to end your schedule
    int d_starts[n]: the start times of each delivery[i]
    int d_ends[n]: the end times of each delivery[i]
    int d_pays[n]: the pay for each delivery[i]
    The output should be an integer representing the maximum amount of money you can make by forming a schedule with the given deliveries.
    '''

    ## heap version
    def jobSchedulingHeap(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        n = len(startTime)
        events = []
        for i in range(n):
            events.append((startTime[i], endTime[i], profit[i]))

        heapq.heapify(events)
        # 当前的最大收益
        max_profix = 0
        while events:
            e = heapq.heappop(events)
            if e[1] > 0:
                # 该任务结束那天，可能的最大收益是max_profix加上当前任务的收益
                heapq.heappush(events, (e[1], 0, max_profix + e[2]))
            else:
                # 判断做这个任务是否能带来更多收益
                max_profix = max(max_profix, e[2])
        return max_profix

    '''
        d_starts = [1,2, 3, 5, 7]
        d_ends = [2, 6, 5, 10, 11]
        d_pays = [10,5, 2, 4, 1]
    '''

    ## normal dp
    # https://leetcode.cn/problems/maximum-profit-in-job-scheduling/solutions/1009447/dong-tai-gui-hua-xiang-xi-zhu-shi-by-van-qmc5/
    def jobSchedulingDP(self, startTime: List[int], endTime: List[int], profit: List[int],start_limit:int, end_limit:int) -> int:
        # 将所有兼职组装为列表形式[[start, end, profit]]
        zip_list = list(zip(startTime, endTime, profit))
        valid_jobs = [item for item in zip_List if item[0] >= start_limit and item[1] <= end_limit]
        ## 剩下的就和1235的做法一样了
        jobs = sorted(valid_jobs, key=lambda x: x[1])  # sorted by end time
        # 根据endTime排序这些兼职
        n = len(jobs)
        # 防止第一个兼职判断的时候越界，添加一个虚拟兼职，开始时间和结束时间还有收益都为0
        jobs = [[0, 0, 0]] + jobs
        # 设置dp状态,总共n个真实兼职和1个虚拟兼职
        dp = [0 for _ in range(n + 1)]
        # 遍历每一个兼职
        for i in range(1, n + 1):
            cur = i
            # 对于第i个兼职，查找jobs[j][1] <= jobs[i][0]的第一个兼职，即逆序查找兼职的结束时间刚好<=当前兼职开始时间的第一个兼职
            print(cur)
            for j in range(i - 1, -1, -1):
                # 找到了, 令cur=j,然后停止查找，找不到cur = i
                if jobs[j][1] <= jobs[i][0]:
                    cur = j
                    break
            # 当前的状态即为
            # max(前一个状态的最大收益, 当前兼职的收益+之前找到的前一个兼职状态的最大收益)
            dp[i] = max(dp[i - 1], jobs[i][2] + dp[cur])
        # 返回最后一个状态的收益
        return dp[-1]


    #https://leetcode.com/problems/maximum-profit-in-job-scheduling/solutions/4514876/dp-approach
    def jobSchedulingDPbs(self, startTime: List[int], endTime: List[int], profit: List[int], start_limit: int,
                      end_limit: int) -> int:

        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        jobs = [item for item in jobs if item[0] >= start_limit and item[1] <= end_limit]
        sorted_end_times = [x[1] for x in jobs]
        n = len(jobs)

        dp = [0] * n
        dp[0] = jobs[0][2]

        for i in range(1, n):
            current_start, _, current_profit = jobs[i]
            # Find the latest job that finishes before the current job starts
            j = bisect_right(sorted_end_times, current_start) - 1
            if j >= 0:
                current_profit += dp[j]

            dp[i] = max(current_profit, dp[i - 1])

        return dp[-1]

'''
https://leetcode.cn/problems/maximum-profit-in-job-scheduling/solutions/1009447/dong-tai-gui-hua-xiang-xi-zhu-shi-by-van-qmc5/
https://docs.python.org/3/library/bisect.html
dp[i]
代表到i个job最大化的收益
收益最大化： 
1要么不选这个job 最大值是dp[i - 1] （规模减小）
2要么选这个job ，但是dp[k] 代表再选这个job同时，我们能做的最晚完成的job k 

'''
start_time = 0
end_time = 10
d_starts = [1,2, 3, 5, 7]
d_ends   = [2,6, 5, 10, 11]
d_pays   = [10,5, 2, 4, 1]
# test = zip(d_starts,d_ends,d_pays)
zip_List= list(zip(d_starts,d_ends,d_pays))
condition_list = [item for item in zip_List if item[0] >= start_time and item[1] <= end_time ]
print(condition_list)
# 正确的写法,先 zip , 再list 这个zip的iteroter , 再加上condition
valid_delivery = sorted(condition_list,key=lambda  x : x[1])

print(valid_delivery)

test = solution()
print(test.jobSchedulingDPbs(d_starts,d_ends,d_pays,start_time,end_time))
print(test.jobSchedulingDP(d_starts,d_ends,d_pays,start_time,end_time))
