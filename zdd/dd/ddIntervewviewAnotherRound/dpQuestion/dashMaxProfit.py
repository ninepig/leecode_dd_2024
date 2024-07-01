from bisect import bisect_right

'''
https://www.1point3acres.com/bbs/thread-1054210-1-1.html
https://www.1point3acres.com/bbs/thread-1053309-1-1.html
https://www.1point3acres.com/bbs/thread-1052843-1-1.html

After solving it, a follow-up was given as "If the dasher is allowed to handle up to N orders at the same time, 
what will be the max profit?" That's to say, according to the interviewer, 
that a dasher can handle no more than N fully/partially overlapping orders.
'''
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
        jobs = sorted(zip(start_days,end_days,pay_days),key=lambda x:x[1]) # using zip and sort by end_day
        valid_job = [job for job in jobs if job[0] >= start_limit and job[1] <= end_limit] ## filter jobs by start and end limits

        n = len(valid_job)
        valid_job = [[0,0,0]] + valid_job  ## setting dummy job  just in case stack overflow
        dp = [0 for _ in range(n + 1)]
        for i in range(1,n + 1):
            cur = i
            ## dp tansfer --> dp[i] = max (dp[i-1], dp[j] + job[i][2])
            ## if we pick ith day job, we need find lastest end day of previous job which ealier than i's start day.
            ## we loop from end to begin
            for j in range(i-1, -1, -1):
                if valid_job[j][1]<= valid_job[i][0]:
                    cur = j
                    break
            dp[i] = max(dp[i - 1] , dp[cur] + valid_job[i][2])

        return dp[-1]



    def jobMaxProfitDPBS(self,start_days:list[int],end_days:list[int],pay_days:list[int],start_limit:int,end_limit:int):
        jobs = sorted(zip(start_days,end_days,pay_days),key=lambda x:x[1]) # using zip and sort by end_day
        valid_job = [job for job in jobs if job[0] >= start_limit and job[1] <= end_limit] ## filter jobs by start and end limits
        end_time_sorted = [job[1] for job in jobs] ## get sorted ending time array

        n = len(valid_job)
        dp = [0]*n
        dp[0] = valid_job[0][2]
        for i in range(1,n):
            start_time,end_time,current_pay = valid_job[i][0],valid_job[i][1],valid_job[i][2]
            ## we use start time and binary search to find latest job j if we choose job i
            j = bisect_right(end_time_sorted, start_time) - 1 ## bisect_right will choose first right pos , so we need minus 1 to get first valid endtime
            if j >= 0 :
                current_pay += dp[j]

            dp[i] = max(dp[i-1],current_pay)

        return dp[-1]



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

test = Solution()
print(test.jobMaxProfit(d_starts,d_ends,d_pays,start_time,end_time))
print(test.jobMaxProfitDPBS(d_starts,d_ends,d_pays,start_time,end_time))

