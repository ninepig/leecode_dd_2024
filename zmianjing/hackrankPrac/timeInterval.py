# you are given 2 strings.  startTime : "mon 10:45 am" and  endTime: "mon 11:00 am".
# you need to output all the times between starttime and endtime in the interval of 5 minutes.
# output: ["11045", "11050","11055", "111000"].
# in output each string represents the day+time+minute. eg: 11045: 1+10+45 => monday represents 1. tuesday 2 etc.
# Also, the output should be in 24hr format and input will be in 12hr format. you are required to do input validations as they can have invalid time formats.

class solution:
    def __init__(self):
        self.daysToInt = {
            'mon': 1,
            'tue': 2,
            'wed': 3,
            'thu': 4,
            'fri': 5,
            'sat': 6,
            'sun': 7,
        }

    def printPath(self, start_time, end_time, interval):
        ## santit check
        if not start_time or not end_time:
            raise Exception("wrong input")

        start_day, start_hour, start_min = self.parseTime(start_time)
        end_day, end_hour, end_min = self.parseTime(end_time)
        print(start_day, start_hour, start_min)
        print(end_day, end_hour, end_min)
        if start_day > end_day:
            end_day += 7

        while True:
            out_put_day = str(1 if start_day == 8 else start_day % 8)
            out_put_hour = "0" + str(start_hour) if start_hour < 10 else str(start_hour)
            out_put_min = "0" + str(start_min) if start_min < 10 else str(start_min)
            print(out_put_day, out_put_hour, out_put_min)
            start_min += interval
            if start_min >= 60:
                start_min = start_min % 60
                start_hour += 1
            if start_hour >= 24:
                start_hour %= 24
                start_day += 1
            ## bug ...
            if start_day > end_day or (start_day == end_day and start_hour > end_hour) or (
                    start_day == end_day and start_hour == end_hour and start_min > end_min):
                print("break")
                break

    # mon 10:45 am
    def parseTime(self, time_str):
        times = time_str.split(" ")
        day = self.daysToInt[times[0]]  ## need check sanitty ,we assume input is valid
        am_pm = times[2]
        hour_mins = times[1].split(":")
        hour = int(hour_mins[0])
        mins = int(hour_mins[1])

        if am_pm == "pm":
            hour += 12
        return day, hour, mins


test = "mon 10:45 pm"
sol = solution()
sol.printPath("mon 10:45 am", "mon 11:00 pm", 5)