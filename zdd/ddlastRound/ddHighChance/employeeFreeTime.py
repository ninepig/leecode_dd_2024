# // Given a list of time blocks where a particular person is already booked/busy, a start and end time to search between,
# a minimum duration to search for, find all the blocks of time that a person is free for a potential meeting that will last the aforementioned duration.
# // Given: starttime, endtime, duration, meetingslist -> suggestedmeetingtimes
# // Let's assume we abstract the representation of times as simple integers, so a valid time is any valid integer supported by your environment. Here is an example input:
# // meetingslist: [3,20], [-2, 0], [0,2], [16,17], [19,23], [30,40], [27, 33]
# // starttime: -5
# // endtime: 27
# // minduration: 2
# // expected answer:
# // freetime: [-5, -2], [23,27]*

class solution:
    def availableTime(self,schedule:list[list[int]],start:int, end:int, duration:int):
        if not schedule :
            return []
        ## preprocess schedule to make that fit in endtime and starttime
        post_schedule = []
        for item in schedule:
            if item[0] <= start and item[1] <= start:
                continue
            elif item[0] >= end and item[1] >= end:
                continue
            elif item[0] <= start and item[1] > start:
                post_schedule.append([start, item[1]])
            elif item[0] < end and item[1] >= end:
                post_schedule.append([item[0], end])
            else:
                post_schedule.append(item)

        print(post_schedule)

        post_schedule.sort(key = lambda x:x[0]) ## order by start time
        res = []
        temp = post_schedule[0]
        ## located first slot , CHECK if first schedule can eat start time . if not, adding that to res
        if start < temp[0] and abs(temp[0] - start) >= duration:
            res.append([start,temp[0]])

        for item in post_schedule[1:]: # removed first item
            ##previous end time smaller than current item's start time , and difference is bigger than durantion, we can adding.
            ## if we can , temp  = curr item

            if temp[1] < item[0] and abs(item[0] - temp[1]) >= duration:
                res.append([temp[1],item[0]])
                temp = item
            ## 如果没有足够间隔  我们只看上一个间隔结束的线
            else:## if we can not, we update new end
                temp[1] = temp[1] if temp[1] > item[1] else item[1]

        ## located last slot
        if temp[1] < end and abs(end - temp[1]) >= duration:
            res.append([temp[1],end])

        return res


meeting_list = [ [3,20], [-2, 0], [0,2], [16,17], [19,23], [30,40], [27, 33]]
start = -5
end = 27
duration = 2

sol = solution()
print(sol.availableTime(meeting_list,start,end,duration))
