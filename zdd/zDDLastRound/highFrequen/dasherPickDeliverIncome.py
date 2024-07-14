'''
https://www.1point3acres.com/bbs/thread-919902-1-1.html
https://www.1point3acres.com/bbs/thread-1021472-1-1.html
Given list of OrderActivity and basePay/minute for one Dasher,
calculate the total pay of the dasher. Consider this is for one dasher,
and all activities happened within single day
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
class OrderActivity:
    def __init__(self,hour,min,status,orderId,dasherId):
        self.hour = hour
        self.min = min
        self.status = status
        self.orderId = orderId
        self.dasherId = dasherId


class solution:
    def dasherIncome(self,orders : list[OrderActivity],basePay:float):
        if not orders or len(orders) == 0 or basePay == 0:
            return 0
        top_order = orders[0]
        if top_order.status == "F":
            return 0 ## invaild
        order_in_hands = 1
        income = 0
        for idx in range(1,len(orders)):
            current_order = orders[idx]
            min_differece = self.getMin(top_order,current_order)
            current_income = min_differece * order_in_hands * basePay ## order in hands means how many picked order, 2 picking order diff has base pay
            income += current_income
            if current_order.status == "P":
                order_in_hands += 1
            else:
                order_in_hands -= 1
            top_order = current_order ## we update toporder with current order , we only cal the time diff between two adjancent order

        return income


    def getMin(self, top_item, current_item):
        return 60*(current_item.hour - top_item.hour) + current_item.min - top_item.min



    def dasherIncomeWithWaiting(self, orders: list[OrderActivity], basePay: float):
        if not orders or len(orders) == 0 or not basePay:
            raise Exception("Wrong input")
        totalIncome = 0
        top_order = orders[0]
        orderInHand = 1
        top_waitingOrder = None

        for i in range(1, len(orders)):
            ## if we have waiting list, it could duplicated here, so we can not cal here
            current_item = orders[i]
            if current_item.status == "arrived":  ## arrived
                if top_waitingOrder:
                    raise Exception("Wrong order")
                top_waitingOrder = current_item
            elif current_item.status == "picked":
                if not top_waitingOrder:
                    raise Exception("Wrong order")
                min_difference = self.getMin(top_waitingOrder, current_item)
                totalIncome += min_difference * basePay  ## waiting pay
                top_waitingOrder = None  ## no pending wait order
            elif current_item.status == "accepted":
                min_differece = self.getMin(top_order, current_item)
                totalIncome += min_differece * orderInHand * basePay
                orderInHand += 1
                top_order = current_item
            elif current_item.status == "delivered":
                min_difference = self.getMin(top_order, current_item)
                totalIncome += min_difference * orderInHand * basePay
                orderInHand -= 1
                top_order = current_item


        return totalIncome

## waiting time,
    ## waiting 和 deliver的钱单独算。 这样就很优雅
    def dasherIncomeWithWaitingPeak(self, orders: list[OrderActivity], basePay: float,peakHour:list[list[int]]):
        if not orders or len(orders) == 0 or not basePay:
            raise Exception("Wrong input")
        totalIncome = 0
        top_order = orders[0]
        orderInHand = 1
        top_waitingOrder = None

        for i in range(1, len(orders)):
            ## if we have waiting list, it could duplicated here, so we can not cal here
            current_item = orders[i]
            if current_item.status == "arived":  ## arrived
                if top_waitingOrder:
                    raise Exception("Wrong order")
                top_waitingOrder = current_item
            elif current_item.status == "picked":
                if not top_waitingOrder:
                    raise Exception("Wrong order")
                min_difference = self.getMinWithPeak(top_waitingOrder, current_item,peakHour)
                totalIncome += min_difference * basePay  ## waiting pay
                top_waitingOrder = None  ## no pending wait order
            elif current_item.status == "accepted":
                min_difference = self.getMinWithPeak(top_order, current_item,peakHour)
                totalIncome += min_difference * orderInHand * basePay
                orderInHand += 1
                top_order = current_item
            elif current_item.status == "delivered":
                min_difference = self.getMinWithPeak(top_order, current_item)
                totalIncome += min_difference * orderInHand * basePay
                orderInHand -= 1
                top_order = current_item


        return totalIncome


    # peak hour
    def getMinWithPeak(self, top_item, current_item,peakHour):
        # return 60*(current_item.hour - top_item.hour) + current_item.min - top_item.min
        start_by_mins = top_item.hour * 60 + top_item.min
        end_by_mins = current_item.hour * 60 + current_item.min
        base_min = end_by_mins - start_by_mins
        ## get peak time
        peak_min = 0

        ## how many peak hour we have and what is format . TODO need confirm with interviewer
        for item in peakHour:
            peak_start_min = item[0] * 60 + item[1]
            peak_end_min = item[2]*60 + item[3]
            ## check if our current start - end time interval has overlap with peak hour
            ## 一定要画图做
            if peak_end_min < start_by_mins:
                peak_min+=0
            elif peak_start_min > end_by_mins:
                peak_min += 0
            elif peak_start_min < start_by_mins and peak_end_min < end_by_mins:
                peak_min += peak_end_min - start_by_mins
            elif peak_start_min > start_by_mins and peak_end_min < end_by_mins:
                peak_min += peak_end_min + peak_start_min
            elif peak_start_min < end_by_mins and peak_end_min > end_by_mins:
                peak_min += end_by_mins - peak_end_min

        return peak_min + base_min




        return base_min + peak_min

## for pick full 2 type only

test = OrderActivity(6,15,"P",1,1)
test2 = OrderActivity(6,30,"P",2,1)
test3 = OrderActivity(6,35,"F",1,1)
test4 = OrderActivity(6,40,"F",2,1)

testArray = [test,test2,test3,test4]
sol = solution()
print(sol.dasherIncome(testArray,0.3))
# print(sol.dasherIncomeConstantSpace(testArray,0.3))


test = OrderActivity(6,15,"accepted",1,1)
test2 = OrderActivity(6,30,"accepted",2,1)
test3 = OrderActivity(6,35,"arrived",1,1)
test4 = OrderActivity(6,40,"picked",1,1)
test5 = OrderActivity(6,45,"arrived",2,1)
test6 = OrderActivity(6,48,"picked",2,1)
test7 = OrderActivity(6,50,"delivered",1,1)
test8 = OrderActivity(6,55,"delivered",2,1)
testArray2 = [test,test2,test3,test4,test5,test6,test7,test8]
# testArray3 = [test,test2,test7,test8]
print(sol.dasherIncomeWithWaiting(testArray2,0.3))


## peak hour 没有测试 但是大概就这个意思 取决于input的格式
