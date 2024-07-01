'''
https://www.1point3acres.com/bbs/thread-1054210-1-1.html
https://www.1point3acres.com/bbs/thread-1053309-1-1.html
https://www.1point3acres.com/bbs/thread-1052843-1-1.html

After solving it, a follow-up was given as "If the dasher is allowed to handle up to N orders at the same time,
what will be the max profit?" That's to say, according to the interviewer,
that a dasher can handle no more than N fully/partially overlapping orders.
'''
import bisect


# TODO CHECK FOLLWUP

class Solution:
    '''
    Time O(NlogN) for sorting
    Time O(NlogN) for binary search for each job
    Space O(N)
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
    def jobMaxProfit(self,start_days:list[int],end_days:list[int],pay_days:list[int],start_limit:int,end_limit:int):
        ## santity check
        if not start_days or not end_days or not pay_days :
            return -1
        ## check start time and end limit time
        ## we sorted by end days
        order = sorted(zip(start_days,end_days,pay_days),key=lambda x:x[1])
        ## filter by start/end limit
        valid_order = [item for item in order if item[0] >= start_limit and item[1] <= end_limit]
        print(valid_order)
        '''
        dp[i] = maxValue if we can make till i 's job
        dp[0] = 0 
        tansfer state
        take i 's job or not take i's job
        dp[i] = max( dp[j] + job[i] , dp[i-1) ## dp[j] means max value before we take i's job , if we take i's job, last job we can take is j
        '''
        n = len(valid_order)
        dp = [0] * (n + 1)
        # dp_item = [[] for _ in  range(n + 1)]

        ## bug2 tuble + 数组 要包多一层
        valid_order = [(0,0,0)] + valid_order ## adding dummy node to avoid range issue,since we need reverse check
        # valid_order = [0, 0, 0] + valid_order
        for  i in range(1,n+1):
            cur = i
            ## bug, starting from i - 1 item , not i
            for j in range(i - 1,-1,-1):
                if valid_order[j][1] <= valid_order[i][0]: ## we find j's end time smaller than i's start time
                    cur = j
                    break
            dp[i] = max(dp[i - 1], dp[cur] + valid_order[i][2])

        return dp[-1]


    def jobMaxProfitDp(self,start_days:list[int],end_days:list[int],pay_days:list[int],start_limit:int,end_limit:int):
        ## santity check
        if not start_days or not end_days or not pay_days :
            return -1
        ## check start time and end limit time
        ## we sorted by end days
        order = sorted(zip(start_days,end_days,pay_days),key=lambda x:x[1])
        ## filter by start/end limit
        valid_order = [item for item in order if item[0] >= start_limit and item[1] <= end_limit]
        valid_order_endtime = [item[1] for item in valid_order] ## grab end time to new array

        n = len(valid_order)
        ''' we can also use binary search way  to quick locate j 's pos'''
        dp = [0] * n ## use n this time
        dp[0] = valid_order[0][2] ## dp[0] is first job's profit
        for i in range(1,n):
            start_time,end_time,job_pay = valid_order[i]
            ## we use i's start time to search in order, first right idx will be the first end time bigger than i
            ## so we mins 1 to get target, which is first endtime samller than i
            j = bisect.bisect_right(valid_order_endtime,start_time) - 1
            if j >= 0:
                job_pay += dp[j]
            dp[i] = max(dp[i-1],job_pay)

        return dp[-1]


    def jobMaxProfitPrintOrder(self,start_days:list[int],end_days:list[int],pay_days:list[int],start_limit:int,end_limit:int):
        ## santity check
        if not start_days or not end_days or not pay_days :
            return -1
        ## check start time and end limit time
        ## we sorted by end days
        order = sorted(zip(start_days,end_days,pay_days),key=lambda x:x[1])
        ## filter by start/end limit
        valid_order = [item for item in order if item[0] >= start_limit and item[1] <= end_limit]
        print(valid_order)
        '''
        dp[i] = maxValue if we can make till i 's job
        dp[0] = 0 
        tansfer state
        take i 's job or not take i's job
        dp[i] = max( dp[j] + job[i] , dp[i-1) ## dp[j] means max value before we take i's job , if we take i's job, last job we can take is j
        '''
        n = len(valid_order)
        dp = [0] * (n + 1)
        dp_item = [[] for _ in  range(n + 1)]

        ## bug2 tuble + 数组 要包多一层
        valid_order = [(0,0,0)] + valid_order ## adding dummy node to avoid range issue,since we need reverse check
        # valid_order = [0, 0, 0] + valid_order
        for  i in range(1,n+1):
            cur = i
            ## bug, starting from i - 1 item , not i
            for j in range(i - 1,-1,-1):
                if valid_order[j][1] <= valid_order[i][0]: ## we find j's end time smaller than i's start time
                    cur = j
                    break
            # dp[i] = max(dp[i - 1], dp[cur] + valid_order[i][2])
            if dp[i - 1] > dp[cur] + valid_order[i][2]:
                dp[i] = dp[i - 1]
                dp_item[i].extend(dp_item[i-1])
            else:
                dp[i] = dp[cur] + valid_order[i][2]
                dp_item[i].extend(dp_item[cur])
                dp_item[i].append(i)

        print(dp[-1])
        print(dp_item[-1])
        return dp[-1]

    def jobMaxProfitDpPrintOrder(self,start_days:list[int],end_days:list[int],pay_days:list[int],start_limit:int,end_limit:int):
        ## santity check
        if not start_days or not end_days or not pay_days :
            return -1
        ## check start time and end limit time
        ## we sorted by end days
        order = sorted(zip(start_days,end_days,pay_days),key=lambda x:x[1])
        ## filter by start/end limit
        valid_order = [item for item in order if item[0] >= start_limit and item[1] <= end_limit]
        valid_order_endtime = [item[1] for item in valid_order] ## grab end time to new array

        n = len(valid_order)
        ''' we can also use binary search way  to quick locate j 's pos'''
        dp = [0] * n ## use n this time
        dp_item = [[] for _ in range(n)]
        dp[0] = valid_order[0][2] ## dp[0] is first job's profit
        dp_item[0].append(0) ## append first order
        for i in range(1,n):
            start_time,end_time,job_pay = valid_order[i]
            ## we use i's start time to search in order, first right idx will be the first end time bigger than i
            ## so we mins 1 to get target, which is first endtime samller than i
            j = bisect.bisect_right(valid_order_endtime,start_time) - 1
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
        print(dp[-1])
        print(dp_item[-1])
        return dp[-1],dp_item[-1]

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
print(test.jobMaxProfitDp(d_starts,d_ends,d_pays,start_time,end_time))
# print(test.jobMaxProfitPrintOrder(d_starts,d_ends,d_pays,start_time,end_time))
# print(test.jobMaxProfitDpPrintOrder(d_starts,d_ends,d_pays,start_time,end_time))
print(test.jobMaxProfitDpMul(d_starts,d_ends,d_pays,start_time,end_time,3))