# you are given 2 strings.  startTime : "mon 10:45 am" and  endTime: "mon 11:00 am".
# you need to output all the times between starttime and endtime in the interval of 5 minutes.
# output: ["11045", "11050","11055", "111000"].
# in output each string represents the day+time+minute. eg: 11045: 1+10+45 => monday represents 1. tuesday 2 etc.
# Also, the output should be in 24hr format and input will be in 12hr format. you are required to do input validations as they can have invalid time formats.

# follow up 就是 different interval， multiple days， input validation （这个口头聊了聊没写）
## 见招拆招。。不会很难。。

# https://www.1point3acres.com/bbs/thread-1050277-1-1.html

class solution:
    def __init__(self):
        self.dayDict= {
            "mon":1,
            "tue":2,
            "wed":3,
            "thu":4,
            "fri":5,
            "sat":6,
            "sun":7
        }
    def getTimeInterval(self,start:str, end:str,interval:int):
        if not start or not end:
            raise Exception("wrong input")
        start_day,start_hour,start_mins = self.parse(start)
        print(start_day, start_hour ,start_mins)
        end_day,end_hour,end_mins = self.parse(end)
        print(end_day, end_hour ,end_mins)
        ## edge case , if start day > end_day
        if start_day > end_day:
            end_day += 7 ## one more week to end day
        res =[]
        while True:
            ##拆开写比较好。连起来很难debug
            output_days = str(1 if start_day == 8 else start_day % 8)
            output_hour = ("0" + str(start_hour)) if start_hour < 10 else str(start_hour)
            output_min = ("0" + str(start_mins)) if start_mins < 10 else str(start_mins)
            # cur_time_string = (str(1 if start_day == 8 else start_day % 8) + str(("0" + str(start_hour)) if start_hour < 10 else str(start_hour))
            #                    + str(("0" + str(start_mins)) if start_mins < 10 else str(start_mins)))
            print(output_days + output_hour + output_min)
            res.append(output_days + output_hour + output_min)
            start_mins += interval
            if start_mins >= 60:
                start_hour += 1
                start_mins = start_mins % 60
            if start_hour > 24:
                start_day +=1
                start_hour = start_hour%24
            if (start_day > end_day) or (start_day == end_day and start_hour > end_hour) or (start_day == end_day and start_hour == end_hour and start_mins > end_mins):
                break

        return res

    def parse(self, time):
        try:
            time_array = time.split(" ")
            day = self.dayDict[time_array[0]]
            am_pm = time_array[2]
            hour_mins = time_array[1].split(":")
            hour = int(hour_mins[0])
            min = int(hour_mins[1])
            if am_pm == "pm":
                hour += 12
            return day,hour,min
        except:
            print("input parsing error")

start = "tue 10:45 am"
end = "mon 11:00 pm "
sol = solution()
sol.getTimeInterval(start,end,5)