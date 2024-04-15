class OrderActivity:
    def __init__(self, hour, mins, status, order_id, dasherId):
        self.hour = hour
        self.mins = mins
        self.status = status
        self.order_id = order_id
        self.dasher_id = dasherId


class Solution:
    def getTotallyIncome(self, orderList, basePay):
        ## sanity check
        if not orderList or len(orderList) == 0:
            print("wrong input")
            return 0
        '''
        we use a stack and counter to record last order, we cal when we see a new order
        if that is a pickup order, we raise counter number , so we can times counternumber to get profit
        '''
        if orderList[0].status != "P":  ## first order is not pick up order, is not valid
            print("Wrongin put")
            return 0  ## 缩进出bug了！
        ## use a vairable to repalce stack.
        top_order = orderList[0]
        res = 0
        pickup_counter = 1
        # print(len(orderList))
        # print(pickup_counter)
        for i in range(1, len(orderList)):
            order = orderList[i]
            time_difference = 60 * (order.hour - top_order.hour) + (order.mins - top_order.mins)
            res += time_difference * pickup_counter * basePay
            print(time_difference, res)
            if order.status == 'P':
                pickup_counter += 1
                top_order = order
            elif order.status == 'D':
                pickup_counter -= 1
                top_order = order

        return res

    def getTotallyIncomeWithWaiting(self, orderList, basePay):
        ## sanity check
        if not orderList or len(orderList) == 0:
            print("wrong input")
            return 0
        '''
        we use a stack and counter to record last order, we cal when we see a new order
        if that is a pickup order, we raise counter number , so we can times counternumber to get profit
        '''
        if orderList[0].status != "P":  ## first order is not pick up order, is not valid
            print("Wrongin put")
            return 0  ## 缩进出bug了！
        ## use a vairable to repalce stack.
        top_order = orderList[0]
        top_waiting_order = None
        res = 0
        pickup_counter = 1
        # print(len(orderList))
        # print(pickup_counter)
        for i in range(1, len(orderList)):
            order = orderList[i]

            # print(time_difference,res)
            if order.status == 'P':
                time_difference = 60 * (order.hour - top_order.hour) + (order.mins - top_order.mins)
                res += time_difference * pickup_counter * basePay
                pickup_counter += 1
                top_order = order
            elif order.status == 'D':
                time_difference = 60 * (order.hour - top_order.hour) + (order.mins - top_order.mins)
                res += time_difference * pickup_counter * basePay
                pickup_counter -= 1
                top_order = order
            elif order.status == "A":  ## arrived, we dont count res,
                if top_waiting_order is not None:
                    print("Wrongin put, we already have a waiting order")
                    return 0  #
                top_waiting_order = order
            elif order.status == "G":
                if top_waiting_order is None:
                    print("Wrongin put, we don't a waiting order")
                    return 0  #
                time_difference = 60 * (order.hour - top_waiting_order.hour) + (order.mins - top_waiting_order.mins)
                res += time_difference * basePay
                top_waiting_order = None

        return res

    def getTotallyIncomeWithWaitingWithPeak(self, orderList, basePay, peakTime):
        ## sanity check
        if not orderList or len(orderList) == 0:
            print("wrong input")
            return 0
        '''
        we use a stack and counter to record last order, we cal when we see a new order
        if that is a pickup order, we raise counter number , so we can times counternumber to get profit
        '''
        if orderList[0].status != "P":  ## first order is not pick up order, is not valid
            print("Wrongin put")
            return 0  ## 缩进出bug了！
        ## use a vairable to repalce stack.
        top_order = orderList[0]
        top_waiting_order = None
        res = 0
        pickup_counter = 1
        # print(len(orderList))
        # print(pickup_counter)
        for i in range(1, len(orderList)):
            order = orderList[i]

            # print(time_difference,res)
            if order.status == 'P':
                time_difference = self.getTime(top_order, order, peakTime)
                res += time_difference * pickup_counter * basePay
                pickup_counter += 1
                top_order = order
            elif order.status == 'D':
                time_difference = self.getTime(top_order, order, peakTime)
                res += time_difference * pickup_counter * basePay
                pickup_counter -= 1
                top_order = order
            elif order.status == "A":  ## arrived, we dont count res,
                if top_waiting_order is not None:
                    print("Wrongin put, we already have a waiting order")
                    return 0  #
                top_waiting_order = order
            elif order.status == "G":
                if top_waiting_order is None:
                    print("Wrongin put, we don't a waiting order")
                    return 0  #
                time_difference = self.getTime(top_waiting_order, order, peakTime)
                res += time_difference * basePay
                top_waiting_order = None

        return res

        ## we assume we only have one peak time

    def getTime(self, top_order, current_order, peakTime):
        ## ttime = base time + peaktime(if live in peakTime)
        baseTime = 60 * (current_order.hour - top_order.hour) + (current_order.mins - top_order.mins)
        peak_mins = 0
        peak_start = peakTime[0][0] * 60 + peakTime[0][1]
        peak_end = peakTime[1][0] * 60 + peakTime[1][1]
        start_time_mins = 60 * top_order.hour + top_order.mins
        end_time_mins = 60 * current_order.hour + current_order.mins

        ## 还需要向下逻辑 todo
        if end_time_mins <= peak_end:
            peak_mins = 0
        elif start_time_mins >= peak_end:
            peak_mins = 0
        elif start_time_mins <= peak_start:
            if end_time_mins >= peak_end:
                peak_mins = peak_end - peak_start
            else:
                peak_mins = end_time_mins - peak_start
        elif end_time_mins <= peak_end:
            if start_time_mins >= peak_start:
                peak_mins = baseTime
            else:
                peak_mins = end_time_mins - peak_start

        return baseTime + peak_mins

        ## we need check if


test = OrderActivity(6, 15, "P", 1, 1)
test2 = OrderActivity(6, 30, "P", 2, 1)
test3 = OrderActivity(6, 35, "A", 1, 1)
test4 = OrderActivity(6, 40, "G", 1, 1)
test5 = OrderActivity(6, 45, "A", 2, 1)
test6 = OrderActivity(6, 48, "G", 2, 1)
test7 = OrderActivity(6, 50, "D", 1, 1)
test8 = OrderActivity(6, 55, "D", 2, 1)
testArray2 = [test, test2, test3, test4, test5, test6, test7, test8]
peakhour = [[6, 14], [6, 16]]
sol = Solution()
print(sol.getTotallyIncomeWithWaiting(testArray2, 0.3))
print(sol.getTotallyIncomeWithWaitingWithPeak(testArray2, 0.3, peakhour))
