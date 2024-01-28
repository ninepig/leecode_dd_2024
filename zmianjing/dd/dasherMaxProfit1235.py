from bisect import bisect_right


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
    ## normal dp
    def maxProfit2(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # 将所有兼职组装为列表形式[[start, end, profit]]
        zip_list = list(zip(startTime, endTime, profit))

        valid_jobs = [item for item in zip_List if item[0] >= start_time and item[1] <= end_time]
        ## 剩下的就和1235的做法一样了
        jobs = sorted(valid_jobs, key=lambda x: x[1])  # sorted by end time
        # 根据endTime排序这些兼职
        # 防止第一个兼职判断的时候越界，添加一个虚拟兼职，开始时间和结束时间还有收益都为0
        # jobs = [[0, 0, 0]] + jobs # if we dont add this change line 53
        n = len(valid_jobs)
        # 设置dp状态,总共n个真实兼职和1个虚拟兼职
        dp = [0 for _ in range(n + 1)]
        # 遍历每一个兼职
        for i in range(1, n + 1):
            cur = i
            # 对于第i个兼职，查找jobs[j][1] <= jobs[i][0]的第一个兼职，即逆序查找兼职的结束时间刚好<=当前兼职开始时间的第一个兼职
            for j in range(i - 1, -1, -1):
                # 找到了, 令cur=j,然后停止查找，找不到cur = i
                if jobs[j][1] <= jobs[i][0]:
                    cur = j
                    break
            # 当前的状态即为
            # max(前一个状态的最大收益, 当前兼职的收益+之前找到的前一个兼职状态的最大收益)
            ## wenjing 这里如果没有之前的哨兵， 应该是 job[i-1][2]
            dp[i] = max(dp[i - 1], jobs[i - 1 ][2] + dp[cur])
        # 返回最后一个状态的收益
        return dp[-1]


    ## binary dp
    def maxProfit(self, startTime:int, endTime:int,d_starts:list,d_ends:list,d_pays:list):
        ## first check startTime and endTime while do zip
        zip_List = list(zip( d_ends, d_starts, d_pays))
        condition_list = [item for item in zip_List if item[0] >= start_time and item[1] <= end_time]
        ## 剩下的就和1235的做法一样了
        valid_delivery = sorted(condition_list, key=lambda x: x[0]) # sorted by end time
        #官方题解 https://leetcode.cn/problems/maximum-profit-in-job-scheduling/description/
        # 以end time 给工作排序, dp[i] 表示前i份兼职工作可以获得的最大报酬. 区间[0,i-i] 的所有兼职工作可以获得的最大报酬
        # dp[0] = 0 means , 没有兼职的时候酬劳为0
        # state
        # dp[i] = max(dp[i-1], dp[k] + profit[i - 1])
        # 在第i-1份工作之前 我们最多可以做到第k份工作, 这样比较就是
        n = len(valid_delivery)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            '''
            其中 k 表示满足结束时间小于等于第 i−1 份工作开始时间的兼职工作数量（因为兼职工作是按照结束时间从小到大进行排序的，
            所以选择第 i−1 份兼职工作后，我们只能继续选择前 k 份兼职工作），可以通过二分查找获得。
            bisect.bisect_left returns the leftmost place in the sorted list to insert the given element. 
            bisect.bisect_right returns the rightmost place in the sorted list to insert the given element.
            我们用第i-1份工的开始时间去search，在结束时间内找最右侧的值，小于等于第i-1份工开始的时间。 这个就是第k份工的结束时间（最大化，所以用bisect_right）
            '''
            k = bisect_right(valid_delivery, valid_delivery[i - 1][1], hi=i)
            dp[i] = max(dp[i - 1], dp[k] + valid_delivery[i - 1][2]) # i is the index from 1 , so we need -1 here
        return dp[n]



'''
https://leetcode.cn/problems/maximum-profit-in-job-scheduling/solutions/1009447/dong-tai-gui-hua-xiang-xi-zhu-shi-by-van-qmc5/
https://leetcode.cn/problems/maximum-profit-in-job-scheduling/solutions/1913089/dong-tai-gui-hua-er-fen-cha-zhao-you-hua-zkcg/

dp[i]
代表到i个job最大化的收益
收益最大化： 
1要么不选这个job 最大值是dp[i - 1] （规模减小）
2要么选这个job ，但是dp[k] 代表再选这个job同时，我们能做的最晚完成的job k 

'''
# class Solution:
#     def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
#         jobs = sorted(zip(endTime, startTime, profit))  # 按照结束时间排序
#         f = [0] * (len(jobs) + 1)
#         for i, (_, st, p) in enumerate(jobs):
#             j = bisect_right(jobs, (st, inf), hi=i)  # hi=i 表示二分上界为 i（默认为 n）
#             f[i + 1] = max(f[i], f[j] + p)  # 为什么是 j 不是 j+1：上面算的是 > st，-1 后得到 <= st，但由于还要 +1，抵消了
#         return f[-1]

# 如何给zip 加上condition
# a = [1,2,3,4,5]
# b = [ [], [], ["a", "b"], ["e", "f"], [] ]
# l = [elt for elt in zip(a,b) if elt[1]]
# print(l)
start_time = 3
end_time = 10
d_starts = [2, 3, 5, 7]
d_ends = [6, 5, 10, 11]
d_pays = [5, 2, 4, 1]
# test = zip(d_starts,d_ends,d_pays)
zip_List= list(zip(d_starts,d_ends,d_pays))
condition_list = [item for item in zip_List if item[0] >= start_time and item[1] <= end_time ]
# 正确的写法,先 zip , 再list 这个zip的iteroter , 再加上condition
valid_delivery = condition_list.sort(key=lambda  x : x[1])

print(valid_delivery)

# print(list(test))

