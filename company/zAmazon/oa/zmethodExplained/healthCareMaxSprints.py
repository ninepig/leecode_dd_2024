#https://www.fastprep.io/problems/get-max-points-from-sprints
'''
Amazon Care is a healthcare and wellbeing portal for its employees.

To promote physical fitness, on the portal they launched a "GetFit" tournament consisting of n sprints. Each sprint lasts for a given number of days and includes several tasks such as push-ups, running, etc. Some tasks are scheduled for each day of the sprint. The ith sprint lasts for days[i] days, and each sprint starts just after the other. That is, if the ithsprint ends on day d, the (i + 1)th sprint starts on day (d + 1). During each sprint, completing the required tasks scheduled on the jth day of the sprint earns the participant j points.

The tournaments are periodic, i.e., as soon as the last sprint of a tournament ends, the first sprint of the next tournament begins. Each tournament, however, has the same schedule of sprints. More formally, the tournament schedule can be considered cyclic in nature and after the last sprint, the first sprint starts again.

An employee decides to participate. However, due to a tight schedule, the employee cannot complete all tasks every day. Instead, the employee will complete the tasks of exactly k consecutive days, hoping to achieve the maximum number of points.

Given the sprint days of n sprints, and the number of days for which the employee competes for k, find the maximum points the employee can score. The training can start and end on any day of any sprint.
'''

from typing import List

## form a array, and sliding windows
def get_max_points(days:List[int], k:int) -> int:
    schedule = []  #  [2,3,2] -> [1,2,1,2,3,1,2]
    for d in days:
        schedule.extend([i+1 for i in range(d)])
    # print(schedule)

    ## Lets use 2 pointers and  try to find the max point
    ans = sum(schedule[:k])

    l, r = 1, k+1
    while r < len(schedule):
        curSum = sum(schedule[l:r])
        ans = max(ans, curSum)
        r += 1
        l += 1

    return ans


days = [2,3,2]
k = 4

print(get_max_points(days,k))