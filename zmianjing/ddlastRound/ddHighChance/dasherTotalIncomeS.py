'''
https://www.1point3acres.com/bbs/thread-919902-1-1.html
https://www.1point3acres.com/bbs/thread-1021472-1-1.html
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


class OrderActivity:
    def __init__(self,hour,min,status,orderId,dasherId):
        self.hour = hour
        self.min = min
        self.status = status
        self.orderId = orderId
        self.dasherId = dasherId

##wenjing
## we need to clearify input time is sorted , if not , we need sorted first
## order's order should be valid

## Using a stack to calculate previous order. if we see any new order, we update income
## 1 if that is a pickup, we update order count + 1
## 2 if that is dropoff, we update order count -1
class Solution:
    def dasherIncome(self,orders : list[OrderActivity],basePay:float):
        if not orders or len(orders) == 0 or not basePay:
            raise Exception("Wrong input")
        stack = []
        totalIncome = 0
        stack.append(orders[0])
        orderInHand = 1
        for i in range(1,len(orders)):
            top_item = stack[-1]
            current_item = orders[i]
            min_difference = self.getMin(top_item, current_item)
            current_income =  min_difference * orderInHand * basePay
            totalIncome += current_income
            if current_item.status == "p":
                orderInHand += 1
            elif current_item.status == "d":
                orderInHand -= 1
            stack.append(current_item) ## 记录上一单的时间，无论是p 还是 d 因为我们每次都会计算，所以要避免重复计算
        return totalIncome

    def getMin(self, top_item, current_item):
        return 60*(current_item.hour - top_item.hour) + current_item.min - top_item.min

    ## 不用栈 就利用一个 变量来做 就行。 我觉得她会问 如果用map ，怎么优化到o1 space
    ## Follow up constraint: try solve it in O(1) space complexity
    def dasherIncomeConstantSpace(self, orders: list[OrderActivity], basePay: float):
        if not orders or len(orders) == 0 or not basePay:
            raise Exception("Wrong input")
        totalIncome = 0
        top_order = orders[0]
        orderInHand = 1
        for i in range(1, len(orders)):
            current_item = orders[i]
            min_difference = self.getMin(top_order, current_item)
            totalIncome += min_difference * orderInHand * basePay
            if current_item.status == "p":
                orderInHand += 1
            elif current_item.status == "d":
                orderInHand -= 1
            top_order = current_item
        return totalIncome



    '''
Follow up question: OrderStatus contain 2 more type as Arrived, picked
    waiting time 
For example, the basePay is 0.3/minute
at 6:15, dasher accepted the order A// from 15-30, 1 order is open, pay = 15 minutes * 0.3
at 6:30, dasher accepted the order B// from 30-35, 2 order is open, pay = 5 minutes * 0.3 * 2
at 6:35, dasher arrived at restaurant A //from 35-40, dasher wait for order A and only count for 1 order pay. pay = 5 * 0.3 * 1
at 6:40, dasher picked up at restaurant A // from 40-45, 2 orders are open
at 6:45, dasher arrived at restaurant B //from 45-48, dasher wait for orderB and count for 1 order pay. pay = 3 * 0.3 * 1
at 6:48, dasher picked up at restaurant B //from 48-50, 2 order are open
at 6:50, dasher fulfilled the order A// from 35-40, 1 order is open, pay = 5 minutes * 0.3
at 6:55, dasher fulfilled the order B// total pay = add all above together'''
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

            ## we count wait/get
            if current_item.status == "a" : ## arrived
                if top_waitingOrder:
                    raise Exception("Wrong order")
                top_waitingOrder = current_item
                continue
            elif current_item.status == "g":
                if not top_waitingOrder:
                    raise Exception("Wrong order")
                min_difference = self.getMin(top_waitingOrder,current_item)
                totalIncome += min_difference * basePay ## waiting pay
                top_waitingOrder = None ## no pending wait order
                continue

            ## we count pick/delivered
            min_difference = self.getMin(top_order, current_item)
            totalIncome += min_difference * orderInHand * basePay
            if current_item.status == "p":
                orderInHand += 1
                top_order = current_item
            elif current_item.status == "d":
                orderInHand -= 1
                top_order = current_item
            # waiting does not care how many order we have

        return totalIncome

    def dasherIncomeWithWaitingBetter(self, orders: list[OrderActivity], basePay: float):
        if not orders or len(orders) == 0 or not basePay:
            raise Exception("Wrong input")
        totalIncome = 0
        top_order = orders[0]
        orderInHand = 1
        top_waitingOrder = None

        for i in range(1, len(orders)):
            ## if we have waiting list, it could duplicated here, so we can not cal here
            current_item = orders[i]
            if current_item.status == "a":  ## arrived
                if top_waitingOrder:
                    raise Exception("Wrong order")
                top_waitingOrder = current_item
            elif current_item.status == "g":
                if not top_waitingOrder:
                    raise Exception("Wrong order")
                min_difference = self.getMin(top_waitingOrder, current_item)
                totalIncome += min_difference * basePay  ## waiting pay
                top_waitingOrder = None  ## no pending wait order
            elif current_item.status == "p":
                min_difference = self.getMin(top_order, current_item)
                totalIncome += min_difference * orderInHand * basePay
                orderInHand += 1
                top_order = current_item
            elif current_item.status == "d":
                min_difference = self.getMin(top_order, current_item)
                totalIncome += min_difference * orderInHand * basePay
                orderInHand -= 1
                top_order = current_item


        return totalIncome

##todo follow up 2：input又多了一个2d string array，每一行‍‍是一个peak time的开始和结束，这期间dasher的收入翻倍
    def dasherIncomeWithWaitingBetter(self, orders: list[OrderActivity], basePay: float,peakHour:list[list[int]]):
        if not orders or len(orders) == 0 or not basePay:
            raise Exception("Wrong input")
        totalIncome = 0
        top_order = orders[0]
        orderInHand = 1
        top_waitingOrder = None

        for i in range(1, len(orders)):
            ## if we have waiting list, it could duplicated here, so we can not cal here
            current_item = orders[i]
            if current_item.status == "a":  ## arrived
                if top_waitingOrder:
                    raise Exception("Wrong order")
                top_waitingOrder = current_item
            elif current_item.status == "g":
                if not top_waitingOrder:
                    raise Exception("Wrong order")
                min_difference = self.getMinWithPeak(top_waitingOrder, current_item,peakHour)
                totalIncome += min_difference * basePay  ## waiting pay
                top_waitingOrder = None  ## no pending wait order
            elif current_item.status == "p":
                min_difference = self.getMinWithPeak(top_order, current_item,peakHour)
                totalIncome += min_difference * orderInHand * basePay
                orderInHand += 1
                top_order = current_item
            elif current_item.status == "d":
                min_difference = self.getMinWithPeak(top_order, current_item)
                totalIncome += min_difference * orderInHand * basePay
                orderInHand -= 1
                top_order = current_item


        return totalIncome


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

test = OrderActivity(6,15,"p",1,1)
test2 = OrderActivity(6,30,"p",2,1)
test3 = OrderActivity(6,35,"d",1,1)
test4 = OrderActivity(6,40,"d",2,1)

testArray = [test,test2,test3,test4]
sol = Solution()
print(sol.dasherIncome(testArray,0.3))
print(sol.dasherIncomeConstantSpace(testArray,0.3))

test = OrderActivity(6,15,"p",1,1)
test2 = OrderActivity(6,30,"p",2,1)
test7 = OrderActivity(6,50,"d",1,1)
test8 = OrderActivity(6,55,"d",2,1)

testArray3 = [test,test2,test7,test8]
print(sol.dasherIncomeConstantSpace(testArray3,0.3))

test = OrderActivity(6,15,"p",1,1)
test2 = OrderActivity(6,30,"p",2,1)
test3 = OrderActivity(6,35,"a",1,1)
test4 = OrderActivity(6,40,"g",1,1)
test5 = OrderActivity(6,45,"a",2,1)
test6 = OrderActivity(6,48,"g",2,1)
test7 = OrderActivity(6,50,"d",1,1)
test8 = OrderActivity(6,55,"d",2,1)
testArray2 = [test,test2,test3,test4,test5,test6,test7,test8]
# testArray3 = [test,test2,test7,test8]
print(sol.dasherIncomeWithWaiting(testArray2,0.3))
print(sol.dasherIncomeWithWaitingBetter(testArray2,0.3))

##todo 测试 peak hour






















