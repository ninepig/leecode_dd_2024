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
import heapq


class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Dasher:
    def __init__(self, id, location, rating):
        self.id = id
        self.location = location
        self.rating = rating


class pqObject:
    def __init__(self, id, distance, rating):
        self.id = id
        self.distance = distance
        self.rating = rating

    def __lt__(self, other):
        if self.distance == other.distance:  ## if distance tie
            return self.rating < other.rating  ## we want pop out smaller rating
        return self.distance > other.distance  ## we want to maintain a maxheap, since we want 3 smallsest distance


class Solution:
    def getNearDasher(self, cur_location, dashers, k):
        ## santity chceck
        if not cur_location or not dashers:
            raise Exception("wrong input")
        queue = []

        for dasher in dashers:
            distance = (dasher.location.x - cur_location.x) ** 2 + (dasher.location.y - cur_location.y) ** 2
            heapq.heappush(queue, pqObject(dasher.id, distance, dasher.rating))
            ## 不断push 满了 pop out
            if len(queue) > k:
                heapq.heappop(queue)
        # res = [(item.id,item.rating) for item in queue]
        res = [(item.id, item.rating) for item in queue]

        return list(reversed(res))


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

sol = Solution()
print(sol.getNearDasher(Location(0, 0), dashers, 2))