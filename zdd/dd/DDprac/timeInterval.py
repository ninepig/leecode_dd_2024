class solution:
    def __init__(self, start , end):
        self.divident = 5
        self.start = start
        self.end = end
        self.day_map = {"mon":1 , "tue":2,"wed":3, "thu":4, "fri":5,"sat":6 , "sun":7 }

    '''
    parse 成 day / hour / mins
    day利用map来做
    hour 需要看是否是pm am --》 pm + 12 
    mins 要做取余的操作。 根据divident 
    '''
    def parseTime(self,time):
       splitTime = time.split()
       day, time , am_pm = splitTime[0],splitTime[1],splitTime[2]
       time_array = time.split(":")
       time_array = [int(time_array[i]) for i in range(len(time_array))]
       if am_pm == "pm":
           time_array[0] += 12
       # 取整的操作, 如果他有余数 比如 11分 12 分 13分 则取整 变成10分
       if time_array[1]%self.divident // self.divident == 0:
           time_array[1] = time_array[1] - time_array[1] % self.divident
       #没有余数 直接设置
       return [self.day_map[day] , time_array[0], time_array[1]]

    def printInteveral(self):
        start_time = self.parseTime(self.start)
        end_time = self.parseTime(self.end)
        start_day,start_hour,start_min = start_time[0],start_time[1],start_time[2]
        end_day,end_hour,end_min = end_time[0],end_time[1],end_time[2]
        res = []
        while True:
            start_min += 5
            if start_min >=60:
                start_min = start_min % 60
                start_hour +=1
            if start_hour >= 24:
                start_hour = 0
                start_day += 1
            if (start_day) > (end_day) or (start_hour > end_hour and start_day == end_day) or (start_min > end_min and start_time == end_time and start_day == end_day):
                break
            cur_timestamp = str(start_day)  + ("0" if start_hour <= 9 else "") + str(start_hour) + ("0" if start_min <= 9 else "") + str(start_min)
            res.append(cur_timestamp)
        return res