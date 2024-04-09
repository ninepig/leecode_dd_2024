'''
https://leetcode.com/discuss/interview-question/1920251/doordash-phone-claim-scheduled-deliveries
https://www.1point3acres.com/bbs/thread-1044923-1-1.html
https://www.1point3acres.com/bbs/thread-917986-1-1.html
part 1:

At DoorDash, many deliveries are scheduled well in advance. To improve our assignment rate, we want to enable dashers
to claim these scheduled deliveries early. However, we noticed that certain dashers perform better,
and want to reward them with a better selection. As a simple solution, we will introduce open windows for
when deliveries will appear for a particular dasher. Below are the following requirements.

1deliveries scheduled two days or further into the future should never be available
2high tier dashers can see all of next day deliveries if the current time is 18:00 or later
3all dashers can see all of next day deliveries if the current time is 19:00 or later
4all dashers can see same day deliveries anytime
Example:
deliveries = [
{ “id”: “one”, “pickupTime”: “2021/01/15 10:00”, “storeId”: “store_1” },
{ “id”: “two”, “pickupTime”: “2021/01/16 6:00”, “storeId”: “store_1” }
];

dasher = { “id”: “dasher_1”, “tier”: “low” };

getAvailableDeliveries(dasher, deliveries, 2021/01/15 18:00) -> [“one”]


We realized, some dashers work really well for some stores, but not as much for others. Therefore we want to allow stores the ability to prefer dashers, so that they can see and claim their deliveries first. Below, is the new requirement we want to introduce.
stores who prefer dashers will have their next day deliveries show up at 17:00 for those preferred dashers only

Consider this new class and new method signature:
class StorePreference {
string id;
string storeId;
string dasherId;
}

Example:
List getAvailableDeliveries(Dasher dasher, List Delivery, DateTime currentTime, List storePreferences)
deliveries = [{ one, 2021/01/15 10:00, store_1 }, { two, 2021/01/16 6:00, store_1 }]
dasher = { dasher_1, low }
preferences = [{ one, store_1, dasher_1 }]

getAvailableDeliveries(dasher, deliveries, 2021/01/15 18:00, preferences) should return both deliveries

part1是dasher分high tier和low tier，所有dasher都能看见当日订单并且看不见明天以后的订单，
对于明天的订单，high tier dasher 下午18点能看到，
而low tier dasher需要19点才能看到，
给你一个delivery list和一个specific dash以及当前的时间datetime类型，问你哪些delivery是availabile的

part2是给delivery加了pickup store的属性，每个store有自己的prefer dasher list，
对于在list中的dasher，次日的订单17点就能看见，修改part1的code

part3
part3是给dasher加了一个属性，骑车或者是开车，给订单加了一个属性，一个订单可以只允许骑车配送，只允许开车或者都允许，
dasher只能看见自己能运的订单，并且对于次日订单，骑车的dasher下午16点就可以看到次日的bike订单，
而开车的dasher19点才能看到那些同时允许开车和骑车的订单，修改part2的code
'''
import collections
from datetime import datetime


class dasher:
    def __init__(self):
        self.id = None
        self.tier = None

class order:
    def __init__(self):
        self.id = None
        self.pick_time = datetime

class Solution:
    ## 如果是datetime type 寫測試變量的時候就要注意了
    def getAvailableOrder(self,order_list:list[order],current_dasher:dasher,currentTime:datetime):

        if not order_list : return []
        if not current_dasher : return []

        res = []
        for item in order_list:
           if self.canSeen(item,current_dasher,currentTime):
               res.append(item)

        return res

    def canSeen(self,item,current_dasher,currentTime):
        current_days = currentTime.day
        current_hours = currentTime.hour
        item_pick_days = item.pick_time.day
        if item_pick_days - current_days == 0 :
            return True
        if item_pick_days - current_days == 1:
            if current_hours >= 19:
                return True
            if current_hours >= 18:
                return current_dasher.tier == 'high'

        return False


    def strToDateTime(self,current_time):
        date_format = '%Y/%m/%d %H:%M'
        return datetime.strptime(current_time,date_format)


##part2
class dasher:
    def __init__(self):
        self.id = None
        self.tier = None

class order:
    def __init__(self):
        self.id = None
        self.pick_time = datetime
        self.pick_store = None

class storePrefer:
    def __init__(self):
        self.id = None
        self.storeId= None
        self.preferDasherList = []


class Solution:
    ## 如果是datetime type 寫測試變量的時候就要注意了
    # 是给delivery加了pickup store的属性，每个store有自己的prefer dasher list，
    # ##对于在list中的dasher，次日的订单17点就能看見
    def getAvailableOrder(self,order_list:list[order],current_dasher:dasher,currentTime:datetime, prefer_list:list[storePrefer]):

        if not order_list  or not current_dasher : return []


        ## get store --> dasher map , check order's store id, if dasher in that dasher map, can be seen after 15
        store_dasher = collections.defaultdict(list)
        for item in prefer_list:
            for dasher_id in item.preferDasherList:
                store_dasher[item.storeId].append(dasher_id)


        res = []
        for item in order_list:
           if self.canSeen(item,current_dasher,currentTime,store_dasher):
               res.append(item)

        return res


    def canSeen(self,item,current_dasher,currentTime,store_dasher):
        current_days = currentTime.day
        current_hours = currentTime.hour
        item_pick_days = item.pick_time.day
        if item_pick_days - current_days == 0 :
            return True
        if item_pick_days - current_days == 1:
            if current_hours >= 19:
                return True
            if current_hours >= 18:
                return current_dasher.tier == 'high'
            if current_hours >= 17:
                if item.pick_store in store_dasher:
                    if current_dasher.id in store_dasher[item.pick_store]:
                        return True

        return False

## part3
'''
part3是给dasher加了一个属性，骑车或者是开车，给订单加了一个属性，一个订单可以只允许骑车配送，只允许开车或者都允许，
dasher只能看见自己能运的订单，并且对于次日订单，骑车的dasher下午16点就可以看到次日的bike订单，
而开车的dasher19点才能看到那些同时允许开车和骑车的订单，修改part2的code
'''
class dasher:
    def __init__(self):
        self.id = None
        self.tier = None
        self.deliver_way = None

class order:
    def __init__(self):
        self.id = None
        self.pick_time = datetime
        self.pick_store = None
        self.deliver_prefer = None

class storePrefer:
    def __init__(self):
        self.id = None
        self.storeId= None
        self.preferDasherList = []

class Solution:
     def getAvailableOrder(self,order_list:list[order],current_dasher:dasher,currentTime:datetime, prefer_list:list[storePrefer]):

            if not order_list  or not current_dasher : return []
            ## get store --> dasher map , check order's store id, if dasher in that dasher map, can be seen after 15
            store_dasher = collections.defaultdict(list)
            for item in prefer_list:
                for dasher_id in item.preferDasherList:
                    store_dasher[item.storeId].append(dasher_id)

            res = []
            for item in order_list:
               if self.canSeen(item,current_dasher,currentTime,store_dasher):
                   res.append(item)

            return res

     def canSeen(self,item,current_dasher,currentTime,store_dasher):
            current_days = currentTime.day
            current_hours = currentTime.hour
            item_pick_days = item.pick_time.day
            if item_pick_days - current_days == 0 :
                return True
            if item_pick_days - current_days == 1:
                if current_hours >= 19:
                    ## need validate with inteviewer, previous case matter or not?
                    if item.deliver_prefer == "both" and current_dasher.deliver_way == "car":
                        return True
                if current_hours >= 18:
                    return current_dasher.tier == 'high'
                if current_hours >= 17:
                    if item.pick_store in store_dasher:
                        if current_dasher.id in store_dasher[item.pick_store]:
                            return True
                if current_hours >= 16:
                    if item.deliver_prefer == "bike" and current_dasher.deliver_way == "bike":
                        return True

            return False