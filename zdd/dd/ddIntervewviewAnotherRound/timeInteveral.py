# you are given 2 strings.  startTime : "mon 10:45 am" and  endTime: "mon 11:00 am".
# you need to output all the times between starttime and endtime in the interval of 5 minutes.
# output: ["11045", "11050","11055", "111000"].
# in output each string represents the day+time+minute. eg: 11045: 1+10+45 => monday represents 1. tuesday 2 etc.
# Also, the output should be in 24hr format and input will be in 12hr format. you are required to do input validations as they can have invalid time formats.

# follow up 就是 different interval， multiple days， input validation （这个口头聊了聊没写）


# https://www.1point3acres.com/bbs/thread-1050277-1-1.html

class solution:
    '''
    yes, we need
    step 1 parse time 
         --> day hour mins
         --> weekday --> number dict
         --> divide by interval when we parse mins
    step 2 output inteteval 

    followup :
    1different interval --> add one more parameter
    2 mult days? different days? should be input change to a list
    3 input validation
    ---> adding some rules
    '''

    # Need clearify  if this case will happen --> sat 10:40 am -- mon 11:00 am --> cross days
    ## todo time formart parse
    def __init__(self):
        self.weekday_dict = {"mon":1,"tue":2,"wed":3,"thu":4,"fri":5,"sat":6,"sun":7}
    def printInteveral(self,start:str, end:str,interval:int):
        if not start or not end:
            print("wrong input")
            return
        start_time = self.parseInput(start,interval)
        end_time = self.parseInput(end,interval)

        cur_day,cur_hour,cur_min = start_time[0],start_time[1],start_time[2]
        end_day,end_hour,end_min = end_time[0],end_time[1],end_time[2]

        if cur_day > end_day: ## cross days problem
            end_day += 7

        while True:
            ## 这里要余8 因为 第一天可能比后面大， 第一天是sun 第二天是mon
            cur_timestamp = str(cur_day % 8)  + ("0" if cur_hour <= 9 else "") + str(cur_hour) + ("0" if cur_min <= 9 else "") + str(cur_min)
            print(cur_timestamp)
            cur_min += interval
            if cur_min >=60 :
                cur_min = 0
                cur_hour +=1
            if cur_hour >= 24:
                cur_hour = 0
                cur_day += 1
            if cur_day > end_day or (cur_day == end_day and cur_hour > end_hour) or (cur_day == end_day and cur_hour == end_hour and cur_min > end_min):
                break ## no more place to input

        return 0

    def parseInput(self, time_str:str,interval:int):
        infos = time_str.split(" ")
        day = self.weekday_dict[infos[0]]
        # mon 10:45 am
        time = infos[1]
        am_pm = infos[2]
        tims_detail = time.split(":")
        hour, min = int(tims_detail[0]),int(tims_detail[1]) ## dont forget this
        if am_pm == "pm":
            hour += 12
        ## we dont need do this , otherwise will ruin the start time, we always have start time/end time
        # min -=  min % interval ## make sure min is 40, 45, 50

        return day, hour, min


if __name__ == '__main__':
    test = solution()
    # print(test.parseInput("mon 10:45 am",5))
    print(test.printInteveral("sun 10:45 am","tue 11:45 am",6))

        