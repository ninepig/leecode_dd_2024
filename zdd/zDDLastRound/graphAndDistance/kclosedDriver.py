'''

k closed distance + rating as extra tie breaker

use heap , and heap lt to do this . rewrite dasher 's class function LT or create a new class heapobject to handle this


# Question
# Given a restaurant geolocation ( longitude / latitude), find 3 closest Dashers (drivers) near the restaurant who can be assigned for delivery, ordered by their distance from the restaurant.
# In case 2 Dashers are equidistant from the restraunt, use Dasher rating as tie breaker.
#
# Each Dasher has 3 properties:
#
# Dasher ID
# Last known location [x,y]
# Rating (0 - 100). Higher the better
# Assume you have a method GetDashers() which returns a list of all Dashers.

'''
import heapq
import math


class Location:
    def __init__(self,longtitue,latitude):
        self.longtitue = longtitue
        self.latitude = latitude

class Dasher:
    def __init__(self,id,location,rating):
        self.location = location
        self.id = id
        self.rating = rating

class HeapObject:

    def __init__(self,id,rating,distance):
        self.distance = distance
        self.id = id
        self.rating = rating

    ## rewrtie lt for handling tiebreak logic
    ## we want 1 closed driver, 2 higher rating
    ## we want a maxHeap to pop larger distance first.(then we can reverse result to get closed driver)
    ## for tie breaking, we want a minHeap, to pop lower rating first
    def __lt__(self, other):
        if self.distance == other.distance:
            return self.rating < other.rating
        return self.distance > other.distance

class Solution:
    def getKClosedDriver(self,k:int, drivers:list[Dasher],rest_location:Location):
        if not rest_location or not drivers or len(drivers) == 0 :
            return []
        heaq_queue = []
        for driver in drivers:
            cur_distance = self.getDistance(driver.location,rest_location)
            heapq.heappush(heaq_queue,HeapObject(driver.id,driver.rating,cur_distance))
            if len(heaq_queue) > k:
                heapq.heappop(heaq_queue)
        return list(reversed([(item.id,item.rating) for item in heaq_queue])) ## output driver id with rating tumple

    def getDistance(self, location, rest_location):
        return math.sqrt((rest_location.latitude - location.latitude)**2 + (rest_location.longtitue - location.longtitue)**2)


def generateDashers(num):
    dashers = []


    dashers.append(Dasher(1, Location(5, 5), 5))
    dashers.append(Dasher(2, Location(5, 5), 4))
    dashers.append(Dasher(3, Location(5, 5), 3))
    dashers.append(Dasher(4, Location(2, 4), 3))
    return dashers

if __name__ == "__main__":
    ##  k closed 所以要用大根堆 ， 自定义这个lt函数 如果distance 相同，我们让rating高的排在前面。 要自己写 尝试下
    dashers = generateDashers(5)
    sol = Solution()
    obj = sol.getKClosedDriver(3,dashers, Location(0, 0))
    print(obj)