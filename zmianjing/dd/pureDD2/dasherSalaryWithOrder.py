'''
input两个string，代表一个dasher上班时间和下班时间，还有一个2d string array，
每一行有order status(接单或者送达)，order id，和一个时间，
假设dasher收入是每单每分钟0.3，ta当天收入是多少？时间string的format都是00:00，注意最后收入结果是小数
有意思

follow up 1
order status多了等待和结束等待，代表dasher到了餐厅但是还没pick up food，这期间dasher的收入是0.3每分钟不管手里有多少单

follow up 2
input又多了一个2d string array，每一行是一个peak time的开始和结束，这期间dasher的收入翻倍

'''

class Order:
    def __init__(self,id:int,status:str,timeStamp:str):
        self.id = id
        self.status = status
        self.timeStamp = timeStamp
class solution:
    '''
    # invalid order ,need discuss with interviewer
    ## if info come with pick -> deliver order?
    ## all valid?
    '''
    def calcSalary(self,startTime:str, endTime:str, orders:list[Order]):
        income = 0.0
        order_dict = dict()
        for order in orders:
            if startTime < order.timeStamp < endTime:
                if order.status == 'pick':
                    order_dict[order.id] = startTime ## store stat time

                elif order.status == 'deliver':
                    ## if not in order, we need  add some logic here, store deliver time , we can store negetive time
                    if order.id not in order_dict:
                        continue
                    else:
                        min = self.calcMin(order.timeStamp , order_dict[order.id])
                        income += min * 0.3 # rate
        return income

    '''
    time_formate
    00：00 ---》 need parse that to mins 
    '''
    def calcMin(self, de_time, pi_time):
        pick_time = pi_time.split(":")
        delivier_time  = de_time.split(":")
        pick_hour, pick_min = int(pick_time[0]) , int(pick_time[1])
        d_hour, d_min = int(delivier_time[0]) , int(delivier_time[1])
        return pick_hour*60 + pick_min - d_hour*60 - d_min

