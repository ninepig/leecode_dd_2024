# https://www.fastprep.io/problems/amazon-maximum-user-traffic
# Time O(N*M) Worse Case N^2, Best CAse N Average
# 答案有差分数组的做法
'''

In order to ensure a hassle-free user experience during the festive season, Amazon maintains logs of the days when its users use the Amazon Shopping app.

The user traffic of a day is said to be the maximum number of users logged into the application during that day. If a user uses the application from day login[i] to day logout[i], it increases the traffic of each day from login[i] to logout[i] (both inclusive) by 1. That is, if login[i] = 4 and logout[i] = 6, then this user increases the traffic of days 4, 5 and 6 by 1.

Given the login and logout day data of n users, find the number of days on which the user traffic is maximum.

Note that all logins take place before all logouts on a single day.

Function Description

Complete the function maximumUserTraffic in the editor below.

maximumUserTraffic has the following parameter(s):

int login[n]: an array of integers with login[i] denoting the login day of i^th user.
int logout[n]: an array of integers with logout[i] denoting the logout day of i^th user.
Returns

int: the number of days having maximum user traffic

'''
from typing import List

'''
基本的数组题
'''

class Solution:
  def maximumUserTraffic(self, login: List[int], logout: List[int]) -> int:
    dates = [0 for _ in range(max(logout) + 1)]

    # O_N
    for i in range(len(login)):
      lin, lout = login[i], logout[i]
      # O_M
      for j in range(lin, lout + 1):
        dates[j] += 1
    counter = 0
    maxTraffic = max(dates)

    # O_N
    for date in dates:
      if date == maxTraffic:
        counter += 1

    return counter

