'''
At DoorDash, many deliveries are scheduled well in advance. To improve our assignment rate, we want to enable dashers to claim these scheduled deliveries early. However, we noticed that certain dashers perform better, and want to reward them with a better selection. As a simple solution, we will introduce open windows for when deliveries will appear for a particular dasher. Below are the following requirements.
deliveries scheduled two days or further into the future should never be available
high tier dashers can see all of next day deliveries if the current time is 18:00 or later
all dashers can see all of next day deliveries if the current time is 19:00 or later
all dashers can see same day deliveries anytime
from datetime import datetime, timedelta

def get_available_deliveries(dasher, deliveries, current_time):
# TODO: implement.
return []

class Delivery(object):
def init(self, idx, pickup_time, store_id):
self.id = idx
self.pickup_time = pickup_time
self.store_id = store_id

class Dasher(object):
def init(self, idx, tier):
self.id = idx
self.tier = tier # 'low', 'high'

Sample test.
today = datetime(2021, 1, 15)
dasher = Dasher('dasher', 'low')
deliveries = [
Delivery('1', today + timedelta(hours=10), 'store_1'),
Delivery('2', today + timedelta(hours=30), 'store_1')
]
available_deliveries = get_available_deliveries(
dasher=dasher,
deliveries=deliveries,
current_time=today + timedelta(hours=18)
)
print([d.id for d in available_deliveries]) # Should include delivery 1.


'''
import datetime


class Delivery:
    def __init__(self, idx:str, pickup_time:datetime, store_id:str):
        self.id = idx
        self.pickup_time = pickup_time
        self.store_id = store_id

class Dasher:
    def __init__(self, idx:str, tier:str):
        self.id = idx
        self.tier = tier # 'low', 'high'

'''
deliveries scheduled two days or further into the future should never be available
high tier dashers can see all of next day deliveries if the current time is 18:00 or later
all dashers can see all of next day deliveries if the current time is 19:00 or later
all dashers can see same day deliveries anytime
'''

def get_available_deliveries(dasher:Dasher,current_time:datetime, deliveries:list[Delivery] ):
    out = []
    for delivery in deliveries:
        if dasher.tier == "high":
            if current_time.hour > 18: # high tier, hour is 18 later ,see all next day deliver
                ## 逻辑就来了 必须是timestamp 在1天之内 timestamp = int(round(now.timestamp())) ,变成timestamp 然后 相差
                ## python 时间戳是秒为单位
                # the next day,  这个很难定义。。不能单纯的用时间戳
                # if int(round(delivery.pickup_time.timestamp())) - int(round(now.timestamp())) <= 24*60*60
                ## 这个挺复杂的
                ## 1 picked date - 1 == current date  next day
                ## judge by month? asking interviewer if we need consider this, or we can use time stamp to judge
                if delivery.pickup_time.day - 1 == current_time.day : ## next day order
                    out.append(delivery)
        if dasher.tier == "low":
            if current_time.hour > 19:  # low tier, hour is 19 later ,see all next day deliver
                if delivery.pickup_time.day - 1 == current_time.day:  ## next day order
                    out.append(delivery)

        if delivery.pickup_time.day  == current_time.day:
            out.append(delivery)
        # see same day order
        ## if we need handle corner case, passed due? will us see that?

    return out


#Sample test.

now = datetime.datetime.now()
dasher = Dasher('dasher', 'high')
deliveries = [
Delivery('1', now + datetime.timedelta(hours=10), 'store_1'),
Delivery('2', now + datetime.timedelta(hours=23), 'store_1'),
Delivery('3', now + datetime.timedelta(hours=40), 'store_1')
]
available_deliveries = get_available_deliveries(
dasher=dasher,
current_time=now,
deliveries=deliveries
)
print([d.id for d in available_deliveries]) # Should include delivery 1.