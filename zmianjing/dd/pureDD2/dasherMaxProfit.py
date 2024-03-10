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
from bisect import bisect_right

'''
two step 
1 for a valid list within start / endtime

2 dp 
state: dp[n] means maxprofit we can get till we do before n job
dp[0] = 0 
dp[:] = 0 initial
transfer ==> dp[n] --> max value (if we do this job, if we dont do this job)
if we dont do this job ==> dp[n] = dp[n-1] 
if we do this job == dp[n] = curJobMoney + dp[k] 
k is the last job we can do which does not affect begin of current job 
transfer => dp[n] = max(dp[n-1))
output dp[-1]  


'''
class Solution:
    def maxProfit(self,d_starts:list[int],d_end:list[int],d_pays:list[int],start_time:int,end_time:int):
        zip_items = zip(d_starts,d_end,d_pays)
        valid_items = [ item for item in zip_items if item[0] > start_time and item[1] < end_time]
        valid_items.sort(key=lambda x:x[1]) # sort by end time
        # jobs = sorted(valid_items, key=lambda x: x[1])  # sorted by end time 两种写法
        size = len(valid_items)
        dp = [0 for _ in range(size + 1)]
        for i in range(1,size + 1):
            cur = i # find last job we can get if we choose i's job
            for j in range(cur - 1, -1, -1):
                if valid_items[j][1] <= valid_items[i][1]:
                    cur = j
                    break
            dp[i] = max(dp[i-1] , valid_items[i-1][2] + dp[cur])

        # 二分法
        for i in range(1,size + 1):
            '''
            其中 k 表示满足结束时间小于等于第 i−1 份工作开始时间的兼职工作数量（因为兼职工作是按照结束时间从小到大进行排序的，
            所以选择第 i−1 份兼职工作后，我们只能继续选择前 k 份兼职工作），可以通过二分查找获得。
            bisect.bisect_left returns the leftmost place in the sorted list to insert the given element. 
            bisect.bisect_right returns the rightmost place in the sorted list to insert the given element.
            我们用第i-1份工的开始时间去search，在结束时间内找最右侧的值，小于等于第i-1份工开始的时间。 这个就是第k份工的结束时间（最大化，所以用bisect_right）
            '''
            k = bisect_right(valid_items, valid_items[i - 1][1], hi=i)
            dp[i] = max(dp[i - 1], dp[k] + valid_items[i - 1][2]) # i is the index from 1 , so we need -1 here
        # return dp[n]

        return dp[-1]





