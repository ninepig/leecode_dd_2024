# you are given 2 strings.  startTime : "mon 10:45 am" and  endTime: "mon 11:00 am".
# you need to output all the times between starttime and endtime in the interval of 5 minutes.
# output: ["11045", "11050","11055", "111000"].
# in output each string represents the day+time+minute. eg: 11045: 1+10+45 => monday represents 1. tuesday 2 etc.
# Also, the output should be in 24hr format and input will be in 12hr format. you are required to do input validations as they can have invalid time formats.

# follow up 就是 different interval， multiple days， input validation （这个口头聊了聊没写）

# https://www.1point3acres.com/bbs/thread-1050277-1-1.html

class solution:
    def __init__(self):
        self.day_dict = {"mon":1,"tue":2,"wed":3,"thu":4,"fri":5,"sat":6,"sun":7}

    def printTimeInterval(self,start:str,end:str,interval:int):
        ## sanity check
        if not start or len(start) == 0 or not end or len(end) == 0 or not interval:
            raise Exception("wrong input")

        ## parse start end time
        start_day,start_hour,start_min = self.parseTime(start)
        end_day,end_hour,end_min = self.parseTime(end)
        cur_day,cur_hour,cur_min = start_day,start_hour,start_min
        # print(start_day,start_hour,start_min)
        # print(end_day, end_hour, end_min)
        if start_day > end_day :
            end_day += 7 ## skip a week

        while True:
            cur_time_string = str(1 if cur_day == 8 else cur_day % 8) + str(("0" + str(cur_hour)) if cur_hour < 10 else str(cur_hour)) + str(("0" + str(cur_min)) if cur_min < 10 else str(cur_min))
            print(cur_time_string)
            cur_min += interval
            if cur_min >= 60:
                cur_min = 0
                cur_hour += 1
            if cur_hour >= 24:
                cur_hour = 0
                cur_day += 1
            if cur_day > end_day or (cur_day == end_day and cur_hour > end_hour) or (cur_day == end_day and cur_hour == end_hour and cur_min > end_min):
                break
        return

    def parseTime(self,time:str):
        time_array = time.split(" ")
        if time_array[0] not in self.day_dict:
            raise Exception("days error")

        days,hour_min,am_pm = time_array[0],time_array[1],time_array[2]
        hour_min_array = time_array[1].split(":")
        hour = int(hour_min_array[0])
        min = int(hour_min_array[1])
        if am_pm == "pm":
            hour += 12

        return int(self.day_dict[days]),hour,min



start = "tue 10:45 am"
end = "mon 11:00 pm "
sol = solution()
sol.printTimeInterval(start,end,5)

