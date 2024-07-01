'''
Timestamp(12h) | Action
8:30am | pickup
9:10am | dropoff
10:20am| pickup
12:15pm| pickup
12:45pm| dropoff
2:25pm | dropoff

total time = 2:25pm-8:30am = 355 mins;
idle time = 10:20am-9:10am = 70 mins;
active time = total time-idle time = 355-70 = 285 mins;
'''

from datetime import datetime


class Solution:
    def getActivateTime(self, order_list):
        ## santity check
        if not order_list or len(order_list) == 0:
            raise Exception("wrong input")

        '''
        we maintain a stack to record last pickup order
        we maintain a count  for pick up order number
        if droped order we minis count
        if count == 0  mean we are not working, we cal the working time
        every min will be time from midnight
        '''
        res = 0
        order_stack = []
        pick_count = 0
        for order in order_list:
            order_min, order_type = self.parsingOrderTimeAndType(order)
            print(order_min, order_type)
            if order_type == "pickup":
                if pick_count == 0:
                    order_stack.append(order_min)  ## push order when we dont have order, which is starting working time
                pick_count += 1
            elif order_type == "dropoff":
                pick_count -= 1
                if pick_count == 0:
                    if not order_stack:
                        raise Exception("wrong input order")
                    res += order_min - order_stack.pop()
        print(res)
        return res

    def parsingOrderTimeAndType(self, order):
        order_type = order.split("|")[1]
        order_time = order.split("|")[0]
        time_format_str = "%I:%M %p"
        ##这里很关键 这个datetime 是从datetime包里导入的类， datetime是个大的类，我们要用到其中的小类
        order_time_date_time = datetime.strptime(order_time, time_format_str)
        initial_time = "12:00 am"
        initial_time_type = datetime.strptime(initial_time, time_format_str)

        return 60 * (
                    order_time_date_time.hour - initial_time_type.hour) + order_time_date_time.minute - initial_time_type.minute, order_type


test = ['8:30 am|pickup', '9:10 am|dropoff', '10:20 am|pickup', '12:15 pm|pickup', '12:45 pm|dropoff',
        '2:25 pm|dropoff']
sol = Solution()
sol.getActivateTime(test)

