from sortedcontainers import SortedDict

'''
Design Meeting Scheduler. Here there are n given meeting rooms. Book a meeting in any meeting room at given interval(starting time, end time). Also send notifications to all person who are invited for meeting.
You should use calender for tracking date and time. And also history of all the meetings which are booked and meeting room.
write an API for client who will give date and time and API should return meeting room with booked scheduled time. client should also query for history of last 20 booked meetings.
Is meeting room available? etc

'''

## 普通的做法
class MyCalendar:
    def __init__(self):
        self.booked = []

    def book(self, start: int, end: int) -> bool:
        if any(l < end and start < r for l, r in self.booked):
            return False
        self.booked.append((start, end))
        return True

## treemap 在python中的形式
class MyCalendar:
    def __init__(self):
        self.booked = SortedDict()

    def book(self, start: int, end: int) -> bool:
        ## bs 找到比end 小的第一个 start值的 index
        i = self.booked.bisect_left(end)
        if i == 0 or self.booked.items()[i - 1][1] <= start:
            self.booked[start] = end
            return True
        return False

# [10,20],[15,25],[20,30]
sol = MyCalendar()
print(sol.book(10,20))
print(sol.book(15,25))
print(sol.book(20,30))