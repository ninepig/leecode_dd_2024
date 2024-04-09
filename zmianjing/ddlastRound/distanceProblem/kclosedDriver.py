import heapq
import math
import random

# Question
# Given a restaurant geolocation ( longitude / latitude), find 3 closest Dashers (drivers) near the restaurant who can be assigned for delivery, ordered by their distance from the restaurant. In case 2 Dashers are equidistant from the restraunt, use Dasher rating as tie breaker.
#
# Each Dasher has 3 properties:
#
# Dasher ID
# Last known location [x,y]
# Rating (0 - 100). Higher the better
# Assume you have a method GetDashers() which returns a list of all Dashers.
class Location:
    def __init__(self, longitude, lattitude):
        self.longitude = longitude
        self.lattitude = lattitude


class Dasher:
    def __init__(self, id, last_location, rating):
        self.id = id
        self.lastLocation = last_location
        self.rating = rating


class heapObject:
    def __init__(self,id,distance,rating):
        self.id = id
        self.distance = distance
        self.rating = rating

    def __lt__(self, other):
        if self.distance == other.distance:
            return self.rating < other.rating ## smaller will be pop first
        return self.distance > other.distance ## we reverse , so we want keep samller in the last

class ClosestDriver:
    def __init__(self, dashers, k, restaurant_location):
        self.dashers = dashers
        self.restaurant_location = restaurant_location
        self.k = k

    def distance(self, location):
        return math.sqrt((location.longitude-self.restaurant_location.longitude)**2 + (location.lattitude-self.restaurant_location.lattitude)**2)

    def getClosestDriver(self):
        closest_dashers = []
        for dasher in self.dashers:
            dist = self.distance(dasher.lastLocation)
            heapq.heappush(closest_dashers, heapObject(dasher.id,dist,dasher.rating))
            if len(closest_dashers)>self.k:
                heapq.heappop(closest_dashers)
        return list(reversed([(heapitem.id,heapitem.rating) for heapitem in closest_dashers]))

def generateDashers(num):
    dashers = []
    # for i in range(num):
    #     rating = random.randrange(1, 5)
    #     latt = random.randrange(100, 200)
    #     long = random.randrange(100, 200)
    #     dashers.append(Dasher(i, Location(long, latt), rating))
    dashers.append(Dasher(1, Location(5, 5), 5))
    dashers.append(Dasher(2, Location(5, 5), 4))
    dashers.append(Dasher(3, Location(5, 5), 3))
    dashers.append(Dasher(4, Location(2, 4), 3))
    return dashers


if __name__ == "__main__":
    ##  k closed 所以要用大根堆 ， 自定义这个lt函数 如果distance 相同，我们让rating高的排在前面。 要自己写 尝试下
    dashers = generateDashers(5)
    # latt = random.randrange(100, 200)
    # long = random.randrange(100, 200)
    obj = ClosestDriver(dashers, 3, Location(0, 0))
    print(obj.getClosestDriver())