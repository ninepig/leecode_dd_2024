#https://www.fastprep.io/problems/amazon-count-faults
'''
A team of analysts at Amazon needs to analyze the stock prices of Amazon over a period of several months.

A group of consecutively chosen months is said to be maximum profitable if the price in its first or last month is the maximum for the group. More formally, a group of consecutive months [l, r] (1 ≤ l ≤ r ≤ n) is said to be maximum profitable if either:

stockPrice[l] = max(stockPrice[l], stockPrice[l + 1], ..., stockPrice[r])
or, stockPrice[r] = max(stockPrice[l], stockPrice[l + 1], ..., stockPrice[r])
Given prices over n consecutive months, find the number of maximum profitable groups which can be formed. Note that the months chosen must be consecutive, i.e., you must choose a subarray of the given array.
'''
class Solution:
    def countFaults(self, n: int, logs: List[str]) -> int:
        status_map = {}
        cnt = 0
        for log in logs:
            s_id, status = log.split()

            if status == "success":
                status_map[s_id] = []
            else:
                if s_id in status_map:
                    status_map[s_id].append(status)
                    if len(status_map[s_id]) == 3:
                        cnt += 1
                        status_map[s_id] = []
                else:
                    status_map[s_id] = [status]

        return cnt
