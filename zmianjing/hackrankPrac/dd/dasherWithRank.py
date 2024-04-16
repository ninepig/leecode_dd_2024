'''

Example:
deliveries = [
{ “id”: “one”, “pickupTime”: “2021/01/15 10:00”, “storeId”: “store_1” },
{ “id”: “two”, “pickupTime”: “2021/01/16 6:00”, “storeId”: “store_1” }
];

dasher = { “id”: “dasher_1”, “tier”: “low” };

getAvailableDeliveries(dasher, deliveries, 2021/01/15 18:00) -> [“one”]
'''

from datetime import datetime
import collections


class dasher:
    def __init__(self, dash_id, tier):
        self.dash_id = dash_id
        self.tier = tier


class delivery:
    def __init__(self, delivery_id, pickTime, store_id):
        self.delivery_id = delivery_id
        self.pickTime = pickTime
        self.store_id = store_id


class storePreference:
    def __init__(self, per_id, store_id, dasher_id):
        self.per_id = per_id
        self.store_id = store_id
        self.dasher_id = dasher_id


class Solution:
    def getAvailableDeliveries(self, dasher, deliveries, cur_time):
        if not deliveries:
            raise Exception("wrong input")
        res = []

        for item in deliveries:
            if self.canSeen(dasher, item, cur_time):
                ## 要加入 delivery id
                res.append(item.delivery_id)

        return res

    # both item's pickTime str, cur_time use datetime type
    def canSeen(self, dasher, item, cur_time):

        itemTime = self.parseTimeFromString(item.pickTime)
        if itemTime.day - cur_time.day >= 2:
            return False
        if itemTime.day - cur_time.day == 1:  ## next day
            if cur_time.hour >= 19:
                return True
            elif cur_time.hour >= 18:
                ## 注意判断的细节
                if dasher.tier == "High":
                    return True
                elif dasher.tier == "Low":
                    return False
        if itemTime.day == cur_time.day:
            return True

        return False

    ##2021/01/15 10:00
    def parseTimeFromString(self, time_string):
        strformat = "%Y/%m/%d %H:%M"
        return datetime.strptime(time_string, strformat)

    def getAvailableDeliveriesWithPrefence(self, dasher, deliveries, cur_time, perference_list):
        if not deliveries:
            raise Exception("wrong input")

        store_dasher_dict = collections.defaultdict(list)

        for preference in perference_list:
            store_dasher_dict[preference.store_id].append(preference.dasher_id)

        res = []
        for item in deliveries:
            if self.canSeenWithPrefence(dasher, item, cur_time, store_dasher_dict):
                ## 要加入 delivery id
                res.append(item.delivery_id)

        return res

    def canSeenWithPrefence(self, dasher, item, cur_time, store_dasher_dict):

        itemTime = self.parseTimeFromString(item.pickTime)
        if itemTime.day - cur_time.day >= 2:
            return False
        if itemTime.day - cur_time.day == 1:  ## next day
            if cur_time.hour >= 19:
                return True
            elif cur_time.hour >= 18:
                ## 注意判断的细节
                if dasher.tier == "High":
                    return True
                elif dasher.tier == "Low":
                    return False
            elif cur_time.hour >= 17:
                ## when dasher id in store's preference dasher
                if dasher.dash_id in store_dasher_dict[item.store_id]:
                    return True
        if itemTime.day == cur_time.day:
            return True

        return False

    ## 没跑， 但是需要问面试官， 车/骑车 具体的情况
    def canSeenType(self, dasher, item, currentTime, store_dashers_prefer):
        pick_uptime = self.getPickUpTime(item.picktime)  ## trans to datetime type
        prefer_dasher = []
        if item.store in store_dashers_prefer:
            if len(store_dashers_prefer[item.store]) > 0:
                prefer_dasher = store_dashers_prefer[item.store]
        # print(prefer_dasher)
        # print(dasher)
        # print(item.id)
        # print(pick_uptime.day, pick_uptime.hour)
        # print(currentTime.day , currentTime.hour)
        if pick_uptime.day - currentTime.day >= 2:  # rule 1
            return False
        if pick_uptime.day == currentTime.day:  # rule 4
            return True
        if (pick_uptime.day - currentTime.day) == 1:  ##next day
            ## 开车的dasher19点才能看到那些同时允许开车和骑车的订单 这个要明确 ，是否order type 一样才能接 还是没声明就都能接
            ## 开车的只能接 both car 骑车的只能接 骑车 both  only car  所以要先判断type？
            ## 要看之前的这些条件 怎么适用。
            if (item.type == "Car" or item.type == "Both") and (dasher.type == "Car" or dasher.type == "Both"):
                if currentTime.hour >= 19:
                    return True
                if currentTime.hour >= 18:
                    # todo bug!! check level
                    if dasher.level == "high":
                        return True
                if currentTime.hour >= 17:
                    if dasher.id in prefer_dasher:
                        return True
            elif (item.type == "Bike" or item.type == "Both") and (dasher.type == "Bike" or dasher.type == "Both"):
                if currentTime.hour >= 19:
                    return True
                if currentTime.hour >= 18:
                    if dasher.level == "high":
                        return True
                if currentTime.hour >= 17:
                    if dasher.id in prefer_dasher:
                        return True
                if currentTime >= 16:
                    if dasher.type == 'Bike' and item.type == 'Bike':
                        return True
        return False


dasher1 = dasher(3, 'High')
dasher2 = dasher(2, 'Low')
deliveries = [
    delivery(1, "2024/3/24 15:00", 1),
    delivery(2, "2024/3/24 19:00", 2),
    delivery(3, "2024/3/23 15:00", 3),
    delivery(4, "2024/3/24 15:00", 4)
]
preference1 = storePreference(1, 2, 2)
preference2 = storePreference(2, 4, 2)
prefence_list = [preference1, preference2]
sol = Solution()
time_object = sol.parseTimeFromString("2024/3/23 17:00")
# print(sol.getAvailableDeliveries(dasher2,deliveries,time_object))
print(sol.getAvailableDeliveriesWithPrefence(dasher2, deliveries, time_object, prefence_list))

