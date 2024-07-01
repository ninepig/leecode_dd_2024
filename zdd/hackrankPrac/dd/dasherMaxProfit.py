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
import bisect


class solution:
    def getMaxAmount(self, start_time: int, end_time: int, d_starts: list[int], d_ends: list[int], d_pays: list[int]):
        ## santity check
        if not d_starts or not d_ends or not d_pays:
            raise Exception("wrong input")

        ## zip them togher and sort by end time
        valid_order = sorted(zip(d_starts, d_ends, d_pays), key=lambda x: x[1])
        ## filter again
        valid_order = [item for item in valid_order if item[0] >= start_time and item[1] <= end_time]
        n = len(valid_order)
        dp = [0] * (n + 1)
        valid_order = [(0, 0, 0)] + valid_order  ## adding dummy node

        for i in range(1, n + 1):
            cur = i
            for j in range(i - 1, -1, -1):
                if valid_order[j][1] <= valid_order[i][0]:  ## we try to first end time which  smaller than i's start time
                    cur = j
                    break
            dp[i] = max(dp[i - 1], dp[j] + valid_order[i][2])

        return dp[-1]

    def getMaxAmountBS(self, start_time: int, end_time: int, d_starts: list[int], d_ends: list[int], d_pays: list[int]):
        ## santity check
        if not d_starts or not d_ends or not d_pays:
            raise Exception("wrong input")

        valid_order = sorted(zip(d_starts, d_ends, d_pays), key=lambda x: x[1])
        ## filter again
        valid_order = [item for item in valid_order if item[0] >= start_time and item[1] <= end_time]
        end_time_array = [item[1] for item in valid_order]

        n = len(valid_order)
        dp = [0] * n
        dp[0] = valid_order[0][2]

        for i in range(1, n):
            cur_start, cur_end, cur_profit = valid_order[i]
            ## we use binarty search to find first bigger end time for j in end_time_array, then we minis 1 to get j
            j = bisect.bisect_right(end_time_array, cur_start) - 1
            if j >= 0:  ## j is valid
                cur_profit += dp[j]

            dp[i] = max(dp[i - 1], cur_profit)

        return dp[-1]

    def getMaxAmountBSWithIndex(self, start_time: int, end_time: int, d_starts: list[int], d_ends: list[int],
                                d_pays: list[int]):
        ## santity check
        if not d_starts or not d_ends or not d_pays:
            raise Exception("wrong input")

        valid_order = sorted(zip(d_starts, d_ends, d_pays), key=lambda x: x[1])
        ## filter again
        valid_order = [item for item in valid_order if item[0] >= start_time and item[1] <= end_time]
        end_time_array = [item[1] for item in valid_order]

        n = len(valid_order)
        dp = [0] * n
        dp[0] = valid_order[0][2]
        dp_item = [[] for _ in range(n)]
        dp_item[0].append(0)

        for i in range(1, n):
            cur_start, cur_end, cur_profit = valid_order[i]
            ## we use binarty search to find first bigger end time for j in end_time_array, then we minis 1 to get j
            j = bisect.bisect_right(end_time_array, cur_start) - 1
            if j >= 0:  ## j is valid
                cur_profit += dp[j]
            # dp[i] = max(dp[i-1], cur_profit)
            if dp[i - 1] > cur_profit:
                dp[i] = dp[i - 1]
                ## 这里是dp_item[i] 而不是别的
                dp_item[i].extend(dp_item[i - 1])
            else:
                dp[i] = cur_profit
                dp_item[i].extend(dp_item[j])
                dp_item[i].append(i)

        return dp[-1], dp_item[-1]

    def getMaxAmountNorder(self, start_time: int, end_time: int, d_starts: list[int], d_ends: list[int],
                           d_pays: list[int], N: int):
        ## santity check
        if not d_starts or not d_ends or not d_pays:
            raise Exception("wrong input")

        valid_order = sorted(zip(d_starts, d_ends, d_pays), key=lambda x: x[1])
        ## filter again
        valid_order = [item for item in valid_order if item[0] >= start_time and item[1] <= end_time]

        res = 0

        for i in range(N):
            if len(valid_order) >= 0:  ##
                cur_profit, cur_indx = self.helper(valid_order)
                if len(cur_indx) > 0:
                    res += cur_profit
                    for item in reversed(cur_indx):  ## we store idx there
                        valid_order.pop(item)  ## pop out index

        return res

    def helper(self, valid_order):
        ## santity check

        end_time_array = [item[1] for item in valid_order]

        n = len(valid_order)
        dp = [0] * n
        dp[0] = valid_order[0][2]
        dp_item = [[] for _ in range(n)]
        dp_item[0].append(0)

        for i in range(1, n):
            cur_start, cur_end, cur_profit = valid_order[i]
            ## we use binarty search to find first bigger end time for j in end_time_array, then we minis 1 to get j
            j = bisect.bisect_right(end_time_array, cur_start) - 1
            if j >= 0:  ## j is valid
                cur_profit += dp[j]
            # dp[i] = max(dp[i-1], cur_profit)
            if dp[i - 1] > cur_profit:
                dp[i] = dp[i - 1]
                ## 这里是dp_item[i] 而不是别的
                dp_item[i].extend(dp_item[i - 1])
            else:
                dp[i] = cur_profit
                dp_item[i].extend(dp_item[j])
                dp_item[i].append(i)

        return dp[-1], dp_item[-1]


start_time = 0
end_time = 10
d_starts = [1, 2, 3, 5, 7]
d_ends = [2, 6, 5, 10, 11]
d_pays = [10, 5, 2, 4, 1]

sol = solution()
print(sol.getMaxAmountNorder(start_time, end_time, d_starts, d_ends, d_pays, 2))
