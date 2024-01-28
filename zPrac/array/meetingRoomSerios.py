'''
252
Given an array of meeting time intervals consisting of
 start and end times [[s1,e1],[s2,e2],…] (si < ei), determine if a person could attend all meetings.
'''
import heapq


def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
    intervals.sort(key=lambda x:x[0])
    end1 = intervals[0][1]
    for i in range(1,len(intervals)):
        if end1 > intervals[i][0]:
            return False
        else:
            end1 = intervals[i][1]
        # if intervals[i - 1][1] > intervals[i][0]: return False
    return True



'''
253
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],…] (si < ei), 
find the minimum number of conference rooms required.
'''
def minMeetingRoomsHeap(self, intervals: List[List[int]]) -> int:
    # heap
    minHeap = []
    intervals.sort(key=lambda x:x[0])
    for start, end in intervals:
        if minHeap and minHeap[0] <= start : # not need this meeting room
            heapq.pop(minHeap)
        # need one new meeting room
        heapq.heappush(minHeap,end)

    return len(minHeap) # how many meeting room in same time


'''
贪心
对于当前会议start，我们找最早可以end的时间
如果 end > start
无论如何我们需要一个meetingrooom
新的如果 start》 end
我们不需要meetingroom 直接找下一个结束的时间  
'''
def minMeetingRoomTwoArray(self, intervals):

    start_time= [x[0] for x in intervals]
    end_time = [x[1] for x in intervals]

    start_time.sort()
    end_time.sort()
    room = 0
    j = 0 # j is index for end time,
    for i in range(len(start_time)):
        if start_time[i] < end_time[j]:
            room += 1
        else:
            j += 1 # we dont need a meeting room, we just find a bigger end time


