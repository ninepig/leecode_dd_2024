## // Given a list of time blocks where a particular person is already booked/busy, a start and end time to search between,
# a minimum duration to search for, find all the blocks of time that a person is free for a potential meeting that will last the aforementioned duration.
# // Given: starttime, endtime, duration, meetingslist -> suggestedmeetingtimes
# // Let's assume we abstract the representation of times as simple integers, so a valid time is any valid integer supported by your environment. Here is an example input:
# // meetingslist: [3,20], [-2, 0], [0,2], [16,17], [19,23], [30,40], [27, 33]
# // starttime: -5
# // endtime: 27
# // minduration: 2
# // expected answer:
# // freetime: [-5, -2], [23,27]*
class Solution:
    def getFreeTime(self, starting, ending, duration, meetingList):
        ## santity check
        if not starting or not ending or not duration or not meetingList:
            raise Exception("Wrong input")
        meetingList.sort(key=lambda x: (x[0], x[1]))  ## sort by start time first , then end time  ,ascending

        idx = 0
        ## we found first meeting later than starting time
        while meetingList[idx][0] < starting:
            idx += 1

            ## check between start -- first meeting , if there is slot available
        res = []
        if meetingList[idx][0] > starting and abs(meetingList[idx][0] - starting) >= duration:
            res.append([starting, meetingList[idx][0]])

        temp = meetingList[idx]
        idx += 1

        while idx < len(meetingList) - 1 and meetingList[idx][1] <= ending:  # we need meeting end early than end ,
            if temp[1] < meetingList[idx][0] and abs(meetingList[idx][0] - temp[1]) >= duration:
                res.append([temp[1], meetingList[idx][0]])
                temp = meetingList[idx]
                idx += 1
            # elif temp[1] > meetingList[idx][0]:  a bug  use else to judge
            else:
                temp[1] = max(temp[1], meetingList[idx][1])
                idx += 1

        ## check if there is slot between end time
        if temp[1] < ending and abs(ending - temp[1]) >= duration:
            res.append([temp[1], ending])

        return res


meeting_list = [[3, 20], [-2, 0], [0, 2], [16, 17], [19, 23], [30, 40], [27, 33]]
start = -5
end = 27
duration = 2

sol = Solution()
print(sol.getFreeTime(start, end, duration, meeting_list))
