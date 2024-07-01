'''
https://leetcode.com/discuss/interview-question/1920251/doordash-phone-claim-scheduled-deliveries
https://www.1point3acres.com/bbs/thread-1044923-1-1.html
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
'''

'''
这道题关键是
datetime 类的使用 和一定的ood

'''

from datetime import datetime


class Dasher:
    def __init__(self,id,tier):
        self.id = id
        self.tier = tier

class Delivery:
    def __init__(self,id,picktime,store_id):
        self.id = id
        self.picktime = picktime
        self.store = store_id

class Preference:
    def __init__(self,id,store_id,dasher):
        self.id = id
        self.store_id = store_id
        self.dasher = dasher

class Solution:
    def getAvailableDeliveries(self,dash:Dasher,deliveries:list[Delivery],current_time:str):
        if not deliveries :
            return []
        res = []
        for delivery in deliveries:
            if self.canSeen(dash,delivery,current_time):
                res.append(delivery.id)

        return res

    def parse_time(self, current_time:str)-> datetime:
        data_format = '%Y/%m/%d %H:%M' ## can be store in self for future change
        return datetime.strptime(current_time,data_format)

    def canSeen(self, dash, delivery, current_time):
        current_time_date = self.parse_time(current_time)
        delivery_time_date = self.parse_time(delivery.picktime)
        # print(current_time_date)
        # print(delivery_time_date)
        # print((delivery_time_date.day),(current_time_date.day))
        # print((delivery_time_date.day - current_time_date.day))
        '''
        judge logic 
        1deliveries scheduled two days or further into the future should never be available
        2high tier dashers can see all of next day deliveries if the current time is 18:00 or later
        3all dashers can see all of next day deliveries if the current time is 19:00 or later
        4all dashers can see same day deliveries anytime
        '''
        if (delivery_time_date.day - current_time_date.day) >= 2 :
            return False
        elif (delivery_time_date.day - current_time_date.day) == 1:
            # print("current hour",current_time_date.hp)
            if 18 <= current_time_date.hour and dash.tier == 'high':
                return True
            elif 19 <= current_time_date.hour:
                return True
        elif delivery_time_date.day == current_time_date.day:
            return True ## can seen any same day
        else:
            return False ## need ask, if we can see pass order

    def getAvailableDeliveriesWithPreference(self, dash: Dasher, deliveries: list[Delivery],perferences:list[Preference], current_time: str):
        if not deliveries :
            return []
        prefer_map = dict()

        ## store --> dasher set
        for item in perferences:
            store_id, dasher_id = item.store_id,item.dasher
            if store_id not in prefer_map:
                prefer_map[store_id] = set()
                prefer_map[store_id].add(dasher_id)

        res = []

        for item in deliveries:
            if self.canSeenWithPrefer(item,current_time,prefer_map,dash):
                res.append(item.id)

        return res

    def canSeenWithPrefer(self, delivery, current_time, prefer_map,dash):
        current_time_date = self.parse_time(current_time)
        delivery_time_date = self.parse_time(delivery.picktime)

        # print(current_time_date.hour)
        # print(delivery_time_date.day - current_time_date.day)
        # print(prefer_map)
        # print("dash id ",dash.id)
        # print("deliver store",delivery.store)
        '''
        We realized, some dashers work really well for some stores, but not as much for others. 
        Therefore we want to allow stores the ability to prefer dashers, so that they can see and claim their deliveries first. 
        Below, is the new requirement we want to introduce.
        stores who prefer dashers will have their next day deliveries show up at 17:00 for those preferred dashers only
        '''
        if delivery.store in prefer_map:
            if dash.id in prefer_map[delivery.store]: ## dasher in store's prefer list
                if delivery_time_date.day - current_time_date.day == 1: ## next day and current time is 15
                    if current_time_date.hour >= 17:
                        return True

        '''
        judge logic 
        1deliveries scheduled two days or further into the future should never be available
        2high tier dashers can see all of next day deliveries if the current time is 18:00 or later
        3all dashers can see all of next day deliveries if the current time is 19:00 or later
        4all dashers can see same day deliveries anytime
        '''
        if (delivery_time_date.day - current_time_date.day) >= 2 :
            return False
        elif (delivery_time_date.day - current_time_date.day) == 1:
            # print("current hour",current_time_date.hp)
            if 18 <= current_time_date.hour and dash.tier == 'high':
                return True
            elif 19 <= current_time_date.hour:
                return True
        elif delivery_time_date.day == current_time_date.day:
            return True ## can seen any same day
        else:
            return False ## need ask, if we can see pass order



# current_time = "2021/01/15 18:00"
# data_format = '%Y/%m/%d %H:%M'
# datetime =datetime.strptime(current_time,data_format)
# data_current_time  = datetime.now()
#
# print(data_current_time - datetime)
# print((data_current_time - datetime).days)
## 如果是时间戳直接相减 那就是他们相差时间戳。 可以转换成days。 但是如果只要看day 那就是用days相减

dasher = Dasher(3,'high')
dasher2 = Dasher(2,'low')
deliveries = [
    Delivery(1,"2024/3/24 15:00",1),
    Delivery(2,"2024/3/24 19:00",2),
    Delivery(3,"2024/3/23 15:00",3),
    Delivery(4,"2024/3/24 15:00",2)
]

preferences = [
    Preference(1,2,3)
]

solu = Solution()
print(solu.getAvailableDeliveries(dasher2,deliveries,"2024/3/23 18:20"))
print(solu.getAvailableDeliveriesWithPreference(dasher2,deliveries,preferences,"2024/3/23 19:20",))