import bisect
import collections


class Solution:
    '''
    1 最基本 排序以后dp
    2 优化 排序以后 二分法 + dp
    3 打印job
    4 mult job
    dp 思路
    dp[i] 代表我们做到i个job 最多能获得的利益
    对于第job[i] 我们可以选择做或者不做
    dp[i] = max(dp[i-1],dp[j] + job[i])
    j在这里表示 如果我们做job i ,之前最多能做到的job 数量
    '''
    def jobMaxProfit(self,start_days:list[int],end_days:list[int],pay_days:list[int],start_limit:int,end_limit:int):
        ## santity check
        if not start_days or not end_days or not pay_days or len(start_days) == 0 or len(end_days) == 0 or len(pay_days) == 0:
            return []
        sorted_job_zip = sorted(zip(start_days,end_days,pay_days),key= lambda x:x[1]) ## sorted by end day
        ## filter for start , end limit
        valid_order = [item for item in sorted_job_zip if item[0] >= start_limit and item[1] <= end_limit]

        size = len(valid_order)
        dp = [0]*(size+1)
        ## tuble 要多包一层
        valid_order = [(0,0,0)] + valid_order ## dummy node for anti ouf of range problem

        for i in range(1,size+1):
            cur = i
            for j in range(i-1,-1,-1): ## reverse from back , to find j of current i
                if valid_order[j][1] <= valid_order[i][0]: ## first j 's end time is smaller than i's start time
                    cur = j
                    break
            dp[i] = max(dp[i-1],valid_order[i][2] + dp[cur])

        return dp[-1]

    # binary search version

    def jobMaxProfitBS(self,start_days:list[int],end_days:list[int],pay_days:list[int],start_limit:int,end_limit:int):
        ## santity check
        if not start_days or not end_days or not pay_days or len(start_days) == 0 or len(end_days) == 0 or len(pay_days) == 0:
            return []
        sorted_job_zip = sorted(zip(start_days,end_days,pay_days),key= lambda x:x[1]) ## sorted by end day
        ## filter for start , end limit
        valid_order = [item for item in sorted_job_zip if item[0] >= start_limit and item[1] <= end_limit]
        end_time_order = [item[1] for item in sorted_job_zip]
        dp = [0] * len(valid_order)
        dp[0] = valid_order[0][2] ## initial with first job's profit
        for i in range(1,len(valid_order)):
            start_time,end_time,job_pay = valid_order[i]
            j = bisect.bisect_right(end_time_order,start_time) - 1 ## we found first item's endtime bigger than start , -1 will located j's pos
            if j >= 0 :
                job_pay += dp[j]
            dp[i] = max(dp[i-1],job_pay)

        return dp[-1]

    ## 利用dp保存打印顺序
    def jobMaxProfitBSprintOrder(self,start_days:list[int],end_days:list[int],pay_days:list[int],start_limit:int,end_limit:int):
        ## santity check
        if not start_days or not end_days or not pay_days or len(start_days) == 0 or len(end_days) == 0 or len(pay_days) == 0:
            return []
        sorted_job_zip = sorted(zip(start_days,end_days,pay_days),key= lambda x:x[1]) ## sorted by end day
        ## filter for start , end limit
        valid_order = [item for item in sorted_job_zip if item[0] >= start_limit and item[1] <= end_limit]
        end_time_order = [item[1] for item in sorted_job_zip]
        dp = [0] * len(valid_order)
        dp[0] = valid_order[0][2] ## initial with first job's profit
        dp_item = [[] for _ in range(len(valid_order))]
        dp_item[0].append(0) ## append first order
        for i in range(1,len(valid_order)):
            start_time,end_time,job_pay = valid_order[i]
            j = bisect.bisect_right(end_time_order,start_time) - 1 ## we found first item's endtime bigger than start , -1 will located j's pos
            if j >= 0 :
                job_pay += dp[j]
            # dp[i] = max(dp[i-1],job_pay)
            if dp[i-1] > job_pay:
                dp[i] = dp[i-1]
                dp_item.extend(dp_item[i-1])
            else:
                dp[i] = job_pay
                dp_item[i].extend(dp_item[j])
                dp_item[i].append(i)

        return dp_item[-1]

    ## 在打印的基础上，我们根据K 每一次打印减少1. 每次把最优解累加
    def jobMaxProfitDpMul(self,start_days:list[int],end_days:list[int],pay_days:list[int],start_limit:int,end_limit:int,k:int):
        if not start_days or not end_days or not pay_days :
            return -1
        ## check start time and end limit time
        ## we sorted by end days
        order = sorted(zip(start_days,end_days,pay_days),key=lambda x:x[1])
        ## filter by start/end limit
        valid_order = [item for item in order if item[0] >= start_limit and item[1] <= end_limit]

        max_profit = 0
        for i in range(k):
            if len(valid_order) > 0:
                profit, idx_list = self.getMaxValueAndIndex(valid_order)
                max_profit += profit
                if len(idx_list) != 0 :
                    ## need reverse otherwise pop will be problem
                    for item in reversed(idx_list):
                        valid_order.pop(item)

        return max_profit

    def getMaxValueAndIndex(self,valid_order):
        valid_order_endtime = [item[1] for item in valid_order]  ## grab end time to new array
        n = len(valid_order)
        ''' we can also use binary search way  to quick locate j 's pos'''
        dp = [0] * n  ## use n this time
        dp_item = [[] for _ in range(n)]
        dp[0] = valid_order[0][2]  ## dp[0] is first job's profit
        dp_item[0].append(0)  ## append first order
        for i in range(1, n):
            start_time, end_time, job_pay = valid_order[i]
            j = bisect.bisect_right(valid_order_endtime, start_time) - 1
            if j >= 0:
                job_pay += dp[j]
            # dp[i] = max(dp[i-1],job_pay)
            if dp[i - 1] > job_pay:
                dp[i] = dp[i - 1]
                dp_item[i].extend(dp_item[i - 1])
            else:
                dp[i] = job_pay
                dp_item[i].extend(dp_item[j])
                dp_item[i].append(i)

        return dp[-1], dp_item[-1]




start_time = 0
end_time = 10
d_starts = [1,2, 3, 5, 7]
d_ends   = [2,6, 5, 10, 11]
d_pays   = [10,5, 2, 4, 1]
test = Solution()
print(test.jobMaxProfit(d_starts,d_ends,d_pays,start_time,end_time))
print(test.jobMaxProfitBS(d_starts,d_ends,d_pays,start_time,end_time))