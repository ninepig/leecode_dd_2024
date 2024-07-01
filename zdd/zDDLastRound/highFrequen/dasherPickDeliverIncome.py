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
            min_differece = self.getMin(current_order,top_order)
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



    def dasherIncomeWithWaiting(self, orders: list[OrderActivity], basePay: float,peakHour:list[list[int]]):
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
                min_difference = self.getMin(top_waitingOrder, current_item,peakHour)
                totalIncome += min_difference * basePay  ## waiting pay
                top_waitingOrder = None  ## no pending wait order
            elif current_item.status == "accepted":
                min_difference = self.getMin(top_order, current_item,peakHour)
                totalIncome += min_difference * orderInHand * basePay
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
        for item in peakHour:
            ## 取决于给我们的peakhour的input ---> hour:min ... 最基本的
            peak_start_min = item[0].hour * 60 + item[1].min  ## transs or other way to make hour:min
            peak_end_min = item[1].hour * 60 + item[1].min  ##
            if peak_start_min < start_by_mins:
                if peak_end_min > end_by_mins:
                    peak_min += end_by_mins - start_by_mins
                else:
                    peak_min += peak_end_min - peak_start_min
            else:
                if peak_end_min > end_by_mins:
                    peak_min += (end_by_mins - peak_start_min)
                else:
                    peak_min += (peak_end_min - peak_start_min)

        return base_min + peak_min