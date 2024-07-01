class TimeIntervals:
    def __init__(self, start, end):
        self.n = 5
        self.start = start
        self.end = end
        self.dayMap = {"mon":1, "tue":2, "wed":3, "thu":4, "fri":5, "sat":6, "sun":7}

    def parseTime(self, t, start=False):
        splitTime = t.split()
        day, time, amPm = splitTime[0], splitTime[1], splitTime[2]

        time = time.split(":")
        time=[int(time[i]) for i in range(len(time))]

        if amPm=="pm":
            time[0]+=12
        #time[1]-time[1]%5 if time[1]%5//5==0 else time[1] 作用就是把13变成10 3 变成0 , 把小于5的余数舍弃
        return [self.dayMap[day], time[0], time[1]-time[1]%5 if time[1]%5//5==0 else time[1]]

    def printTimeIntervals(self):
        start = self.parseTime(self.start, True)
        end = self.parseTime(self.end)
        endDay, endHour, endMin = end[0], end[1], end[2]
        curDay, curHour, curMin = start[0], start[1], start[2]
        # curMins = self.getMins(curDay, curHour, curMin)
        while True:
            curMin+=5
            if curMin>=60:
                curMin=curMin%60
                curHour+=1
            if curHour>=24:
                curHour=0
                curDay+=1
            if curDay>endDay or (curHour>endHour and curDay==endDay) or (curMin>endMin and curHour==endHour and curDay==endDay):
                break
            print(str(curDay)+("0" if curHour<=9 else "")+str(curHour)+("0" if curMin<=9 else "")+str(curMin))

if __name__ == "__main__":
    o = TimeIntervals("mon 10:13 am", "tue 11:00 am")
    o.printTimeIntervals()