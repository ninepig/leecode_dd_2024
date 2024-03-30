'''

Given list of OrderActivity and basePay/minute for one Dasher, calculate the total pay of the dasher. Consider this is for one dasher, and all activities happened within single day
class OrderActivity {
    int hour; // the hour of this event happened
    int minute;
    OrderStatus status;
    String orderId;
    String dasherId;
}
enum OrderStatus {
    ACCEPTED;
    FULFILED;
}
For example, the basePay is 0.3/minute
at 6:15, dasher accepted the order A  // from 15-30, 1 order is open, pay = 15 minutes * 0.3
at 6:30, dasher accepted the order B  // from 30-35, 2 order is open, pay = 5 minutes * 0.3 * 2
at 6:35, dasher fulfilled the order A  // from 35-40, 1 order is open, pay = 5 minutes * 0.3
at 6:40, dasher fulfilled the order B  // total pay = add all above together

'''
class orderActivity:
    def __init__(self,hour,min,status,orderId):
        self.hour = hour
        self.min = min
        self.status = status
        self.orderId= orderId
        # self.dasherId = str

class orderCount:
    def __init__(self,orderid):
        self.id = orderid
        self.pickhour = -1
        self.pickmin = -1
        self.fullhour = -1
        self.fullmin = -1


class solution:
    ## question 1 , basic, only accepted and fulliled status
    ## in each order , check start, end time if valid
    ## we can have a  dict - > record orderid -->[accecpt, fulliedtime]
    ## check the order map and count the total money
    def getTotalIncome(self,start_time:str, end_time:str, order_list:list[orderActivity]):
        if not start_time or not end_time or not order_list or len(order_list) == 0:
            return 0
        start_hour,start_min = int(start_time.split(":")[0]),int(start_time.split(":")[1])
        end_hour,end_min = int(end_time.split(":")[0]),int(end_time.split(":")[1])
        print(start_hour,start_min)
        print(end_hour,end_min)

        order_set= dict() ## order_id : [starting,endtime]
        waiting_time_map = dict()
        for order in order_list:
            if order.orderId in order_set:
                ## order already in dict
                if order.status == "accept":
                    ## invalid
                    continue ## ask interviewer how to handle this
                if order.status == "fullfilled":
                    order_set[order.orderId].fullhour = order.hour
                    order_set[order.orderId].fullmin = order.min
            else:
                if order.status == "fullfilled":
                    continue ## invalid
                if order.status == "accept":
                    order_set[order.orderId] = orderCount(order.orderId)
                    order_set[order.orderId].pickmin = order.min
                    order_set[order.orderId].pickhour = order.hour
        print(len(order_set))
        income = 0
        for item in order_set.values():
            if item.fullhour == -1 or item.fullmin == -1 or item.pickhour == -1 or item.pickmin == -1:
                print("invalid order")
                continue  ## invalid order
            ## not valid for starting time
            if start_hour > item.pickhour:
                print("invalid order")
                continue
            if start_hour == item.pickhour:
                if start_min > item.pickmin:
                    print("invalid order")
                    continue
            ## not valid for ending time
            if end_hour < item.fullhour:
                print("invalid order")
                continue
            if end_hour == item.fullhour:
                if end_min < item.fullmin:
                    print("invalid order")
                    continue
            ## count salary , assume not system error which fullhour smaller than picktime
            duration = (item.fullhour - item.pickhour)*60 + item.fullmin - item.pickmin
            income += duration * 0.3
        return income

    ## 2 more status, waiting, endWaiting
    def getTotalIncomeWithWaiting(self, start_time: str, end_time: str, order_list: list[orderActivity]):
        if not start_time or not end_time or not order_list or len(order_list) == 0:
            return 0
        start_hour,start_min = int(start_time.split(":")[0]),int(start_time.split(":")[1])
        end_hour,end_min = int(end_time.split(":")[0]),int(end_time.split(":")[1])
        print(start_hour,start_min)
        print(end_hour,end_min)

        order_set= dict() ## order_id : [starting,endtime]
        waiting_time_map = dict()
        for order in order_list:
            if order.orderId in order_set:
                ## order already in dict
                if order.status == "accept":
                    ## invalid
                    continue ## ask interviewer how to handle this
                if order.status == "fullfilled":
                    order_set[order.orderId].fullhour = order.hour
                    order_set[order.orderId].fullmin = order.min
            else:
                if order.status == "fullfilled":
                    continue ## invalid
                if order.status == "accept":
                    order_set[order.orderId] = orderCount(order.orderId)
                    order_set[order.orderId].pickmin = order.min
                    order_set[order.orderId].pickhour = order.hour
            if order.orderId not in waiting_time_map:
                if order.status == "endwaiting":
                    continue
                elif order.status == "waiting":
                    waiting_time_map[order.orderId] = orderCount(order.orderId)
                    waiting_time_map[order.orderId].pickmin = order.min
                    waiting_time_map[order.orderId].pickhour = order.hour
            else:
                if order.status == "waiting":
                    continue
                elif order.status == "endwaiting":
                    waiting_time_map[order.orderId].fullmin = order.min
                    waiting_time_map[order.orderId].fullhour = order.hour

        print(len(order_set))
        income = 0
        ## pick up income
        for item in order_set.values():
            if item.fullhour == -1 or item.fullmin == -1 or item.pickhour == -1 or item.pickmin == -1:
                print("invalid order")
                continue  ## invalid order
            ## not valid for starting time
            if start_hour > item.pickhour:
                print("invalid order")
                continue
            if start_hour == item.pickhour:
                if start_min > item.pickmin:
                    print("invalid order")
                    continue
            ## not valid for ending time
            if end_hour < item.fullhour:
                print("invalid order")
                continue
            if end_hour == item.fullhour:
                if end_min < item.fullmin:
                    print("invalid order")
                    continue
            ## count salary , assume not system error which fullhour smaller than picktime
            duration = (item.fullhour - item.pickhour)*60 + item.fullmin - item.pickmin
            income += duration * 0.3

        print("order income",income)
        ## wait time income  since we can not get over lap waiting time. so we need remove overlap part
        waiting_time = []
        ## get waiting time list
        for order in waiting_time_map.values():
            start = order.pickhour * 60 + order.pickmin ## did not handle edge case
            end = order.fullhour  * 60 + order.fullmin ## waiting start , end time
            waiting_time.append([start,end])
        waiting_time.sort(key=lambda x:x[0])
        print("waiting time",waiting_time)
        start = waiting_time[0][0]
        end = waiting_time[0][1]
        waiting_min = 0

        for i in range(1,len(waiting_time)):
            if waiting_time[i][0] > end : # which means we dont have overlap
                waiting_min += end - start
                start = waiting_time[i][0]
                end = waiting_time[i][1]
            else: # we have overlap
                end = waiting_time[i][1]
        waiting_min += end - start
        waiting_income = waiting_min * 0.3
        print("waiting income",waiting_income)

        return income + waiting_income

##todo follow up 2：input又多了一个2d string array，每一行‍‍是一个peak time的开始和结束，这期间dasher的收入翻倍
    def getTotalIncomeWithWaitingAndPeak(self, start_time: str, end_time: str,peak_start_time,str,peak_end_time:str, order_list: list[orderActivity]):
        if not start_time or not end_time or not order_list or len(order_list) == 0:
            return 0
        start_hour, start_min = int(start_time.split(":")[0]), int(start_time.split(":")[1])
        end_hour, end_min = int(end_time.split(":")[0]), int(end_time.split(":")[1])

        peak_start_hour, peak_start_min = int(peak_start_time.split(":")[0]), int(peak_start_time.split(":")[1])
        peak_end_hour, peak_end_min = int(peak_end_time.split(":")[0]), int(peak_end_time.split(":")[1])
        peak_start_mins = peak_start_hour * 60 + peak_start_min
        peak_end_mins = peak_end_hour * 60 + peak_end_min
        order_set = dict()  ## order_id : [starting,endtime]
        waiting_time_map = dict()
        for order in order_list:
            if order.orderId in order_set:
                ## order already in dict
                if order.status == "accept":
                    ## invalid
                    continue  ## ask interviewer how to handle this
                if order.status == "fullfilled":
                    order_set[order.orderId].fullhour = order.hour
                    order_set[order.orderId].fullmin = order.min
            else:
                if order.status == "fullfilled":
                    continue  ## invalid
                if order.status == "accept":
                    order_set[order.orderId] = orderCount(order.orderId)
                    order_set[order.orderId].pickmin = order.min
                    order_set[order.orderId].pickhour = order.hour
            if order.orderId not in waiting_time_map:
                if order.status == "endwaiting":
                    continue
                elif order.status == "waiting":
                    waiting_time_map[order.orderId] = orderCount(order.orderId)
                    waiting_time_map[order.orderId].pickmin = order.min
                    waiting_time_map[order.orderId].pickhour = order.hour
            else:
                if order.status == "waiting":
                    continue
                elif order.status == "endwaiting":
                    waiting_time_map[order.orderId].fullmin = order.min
                    waiting_time_map[order.orderId].fullhour = order.hour

        print(len(order_set))
        income = 0
        ## pick up income
        for item in order_set.values():
            if item.fullhour == -1 or item.fullmin == -1 or item.pickhour == -1 or item.pickmin == -1:
                print("invalid order")
                continue  ## invalid order
            ## not valid for starting time
            if start_hour > item.pickhour:
                print("invalid order")
                continue
            if start_hour == item.pickhour:
                if start_min > item.pickmin:
                    print("invalid order")
                    continue
            ## not valid for ending time
            if end_hour < item.fullhour:
                print("invalid order")
                continue
            if end_hour == item.fullhour:
                if end_min < item.fullmin:
                    print("invalid order")
                    continue
            ## count salary , assume not system error which fullhour smaller than picktime
            item_full_start_min = item.fullhour * 60 + item.fullmin
            item_full_end_min = item.pickhour*60 + item.pickmin
            duration = item_full_end_min - item_full_start_min

            if item_full_start_min > peak_start_mins and item_full_end_min > peak_end_mins:
                income += duration * 0.3 * 2
            elif item_full_start_min < peak_start_mins and item_full_end_min < peak_end_mins:
                income += (peak_start_min - item_full_start_min) * 0.3 + (item_full_end_min - peak_start_min)*0.3*2
            elif item_full_start_min > peak_start_mins and peak_end_mins < item_full_end_min:
                income += (peak_end_mins - item_full_start_min) *0.3*2 + (item_full_end_min - peak_end_mins) *0.3
            else:
                income += duration * 0.3

        print("order income", income)
        ## wait time income  since we can not get over lap waiting time. so we need remove overlap part
        waiting_time = []
        ## get waiting time list
        for order in waiting_time_map.values():
            start = order.pickhour * 60 + order.pickmin  ## did not handle edge case
            end = order.fullhour * 60 + order.fullmin  ## waiting start , end time
            waiting_time.append([start, end])
        waiting_time.sort(key=lambda x: x[0])
        print("waiting time", waiting_time)
        start = waiting_time[0][0]
        end = waiting_time[0][1]
        waiting_min = 0
        ## if rush hour happen in waiting time, logic will be more complicated
        for i in range(1, len(waiting_time)):
            if waiting_time[i][0] > end:  # which means we dont have overlap
                waiting_min += end - start
                start = waiting_time[i][0]
                end = waiting_time[i][1]
            else:  # we have overlap
                end = waiting_time[i][1]
        waiting_min += end - start
        waiting_income = waiting_min * 0.3
        print("waiting income", waiting_income)

        return income + waiting_income

if __name__ == '__main__':
    start_time = "6:00"
    end_time = "12:00"
    orderActivity3 = orderActivity(6,0,"waiting",1)
    orderActivity4 = orderActivity(6,3,"endwaiting",1)
    orderActivity7 = orderActivity(6,2,"waiting",2)
    orderActivity8 = orderActivity(6,15,"endwaiting",2)
    orderActivity1 = orderActivity(6,5,"accept",1)
    orderActivity2 = orderActivity(6, 16, "accept", 2)

    orderActivity5 = orderActivity(6,30,"fullfilled",1)
    orderActivity6 = orderActivity(6,40,"fullfilled",2)
    order_list = [orderActivity1, orderActivity2,  orderActivity5, orderActivity6]
    order_list2 = [orderActivity1,orderActivity2,orderActivity3,orderActivity4,orderActivity5,orderActivity6,orderActivity7,orderActivity8]
    sol = solution()
    # print(sol.getTotalIncome(start_time,end_time, order_list))
    print(sol.getTotalIncomeWithWaiting(start_time,end_time,order_list2))
