'''
https://leetcode.com/discuss/interview-question/1302606/DoorDash-onsite-interview-(new-question!)

Given a sequence of timestamps & actions of a dasher's activity within a day, we would like to know the active time of the dasher. Idle time is defined as the dasher has NO delivery at hand. (That means all items have been dropped off at this moment and the dasher is just waiting for another pickup) Active time equals total time minus idle time. Below is an example. Dropoff can only happen after pickup. 12:00am means midnight and 12:00pm means noon. All the time is within a day.

Timestamp(12h) | Action
8:30am | pickup
9:10am | dropoff
10:20am| pickup
12:15pm| pickup
12:45pm| dropoff
2:25pm | dropoff

total time = 2:25pm-8:30am = 355 mins;
idle time = 10:20am-9:10am = 70 mins;
active time = total time-idle time = 355-70 = 285 mins;
'''

from datetime import datetime
import bisect

def time_to_minutes(time_str):
    time_obj = datetime.strptime(time_str, "%I:%M %p")
    minutes_since_midnight = time_obj.hour * 60 + time_obj.minute
    return minutes_since_midnight


A = [('8:30 am' , 'pickup'),('9:10 am' , 'dropoff'),('10:20 am', 'pickup'),('12:15 pm', 'pickup'),('12:45 pm', 'dropoff'),('2:25 pm' , 'dropoff')]

'''
这个题是用stack的话 比较简单
但其实可以不用stack。。直接用一个top就行
因为只要 p 不为0 的情况下 一直就是在工作状态
所以我们只需要在p 等于0 的时候计算即可
'''
# stack = []
top = None
ans = 0
pickup = 0
for t, action in A:
    t_min = time_to_minutes(t) - time_to_minutes('12:00 am')
    if action == 'pickup':
        if pickup == 0:
            # stack.append(t_min)
            top = t_min
        pickup += 1
    else:
        pickup -= 1 #dropoff
        if pickup == 0:
            ans += t_min - top

print(ans) # 285 min

