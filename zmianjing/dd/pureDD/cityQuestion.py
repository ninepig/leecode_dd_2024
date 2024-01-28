from collections import defaultdict
import random
from collections import namedtuple

from LinkedList import List

'''
Nearest Neighbour City

A number of cities are arranged on a graph that has been divided up like an ordinary Cartesian plane.
Each city is located at an integral (x, y) coordinate intersection.
City names and locations are given in the form of three arrays: c, x, and y,
which are aligned by the index to provide the city name (c[i]), and its coordinates, (x[i], y[i]). 
Determine the name of the nearest city that shares either an x or a y coordinate with the queried city. 
If no other cities share an x or y coordinate, return 'NONE'. If two cities have the same distance to the queried city, q[i],
consider the one with an alphabetically shorter name (i.e. 'ab' < 'aba' < 'abb') as the closest choice.
The distance is the Manhattan distance, the absolute difference in x plus the absolute difference in y.


The time complexity for my solution is O(NlogK) for processing input + O(QlogK) for returning the result for all the given queries,
where N is the number of cities, K is the max number of cities with same x or y coordinate and Q is the number of queries.
'''
City = namedtuple('City', ['x', 'y', 'name'])

# class Solution:
#     def solution(self, nums1: List[int], nums2: List[int]) -> float:
#
#         #          0,1    1,2    2,5.  4,3   5,4.  0,2.   1,0.  0,2
#         cities = ['axx', 'axy', 'az', 'axd', 'aa', 'abc', 'abs', 'p']
#         xs = [0, 1, 2, 4, 5, 0, 1, 0]
#         ys = [1, 2, 5, 3, 4, 2, 0, 2]
#
#         query_cities = ['axx', 'axy', 'abs', "zmm"]
#
#         nearest_cities = self.find_nearest_cities(xs, ys, cities, query_cities)
#         print(query_cities)
#         print(nearest_cities)
#
#     def find_nearest_cities(self, x_list, y_list, cities, query_cities):
#         xCitiesMap = defaultdict(list)
#         yCitiesMap = defaultdict(list)
#         cityMap = dict()
#
#         for idx in range(len(cities)):
#             city = City(x_list[idx], y_list[idx], cities[idx])
#             xCitiesMap[x_list[idx]].append(city)
#             yCitiesMap[y_list[idx]].append(city)
#             cityMap[cities[idx]] = city
#
#         result = []
#         # k * N
#         for query_city in query_cities:
#             if query_city == None or query_city not in cityMap:
#                 result.append(None)
#                 continue
#             city = cityMap[query_city]
#             res = self.find_nearest_neighbour(city, xCitiesMap[city.x] + yCitiesMap[city.y])
#             result.append(res)
#
#         return result
#
#     def find_nearest_neighbour(self, city, neighbours):
#         result = None
#         minDist = float("inf")
#
#         for neighbour in neighbours:
#             if neighbour.name == city.name:
#                 continue
#             tmpDist = abs(city.x - neighbour.x) + abs(city.y - neighbour.y)
#
#             if minDist > tmpDist:
#                 minDist = tmpDist
#                 result = neighbour.name
#             elif minDist == tmpDist:
#                 if len(result) > len(neighbour.name):
#                     result = neighbour.name
#
#         return result

''' binary search'''

#
# def find_nearest_cities_3(x_cord, y_cord, city, query_cities):
#     def distance(x_y1, x_y2):
#         x1, y1 = x_y1
#         x2, y2 = x_y2
#         return abs(x2 - x1) + abs(y2 - y1)
#
#     def b_search_smallest(coord_city_list, target_coord, target_city):
#         start, end = 0, len(coord_city_list) - 1
#         while (start < end):
#             mid = start + (end - start) // 2
#             if coord_city_list[mid][0] >= target_coord:
#                 end = mid
#             else:
#                 start = mid + 1
#         returning_city = coord_city_list[start][1]
#         if returning_city == query_city:
#             dis_around_query = float('inf')
#             if start > 0:
#                 dis_around_query = coord_city_list[start - 1][0]
#                 returning_city = coord_city_list[start - 1][1]
#             if start < len(coord_city_list) - 1 and coord_city_list[start + 1][0] <= dis_around_query:
#                 dis_around_query = coord_city_list[start + 1][0]
#                 returning_city = coord_city_list[start + 1][1]
#         return returning_city
#
#     x_map, y_map, c_map = defaultdict(list), defaultdict(list), defaultdict()
#     for c, x, y in zip(city, x_cord, y_cord):
#         x_map[x].append((y, c))
#         y_map[y].append((x, c))
#         c_map[c] = (x, y)
#
#     for k in x_map.keys():
#         x_map[k].sort()
#         y_map[k].sort()
#
#     # print(x_map)
#     # print(y_map)
#     # print(c_map)
#     res = []
#     for query_city in query_cities:
#         if query_city not in c_map:
#             res.append(None)
#         else:
#             query_x, query_y = c_map[query_city]
#             city_near_x = b_search_smallest(x_map[query_x], query_y, query_city)
#             city_near_y = b_search_smallest(y_map[query_y], query_x, query_city)
#             if city_near_x == query_city and city_near_y == query_city:
#                 res.append(None)
#             elif city_near_x == query_city:
#                 res.append(city_near_y)
#             elif city_near_y == query_city:
#                 res.append(city_near_x)
#             else:
#                 dist1, dist2 = distance(c_map[query_city], c_map[city_near_x]), distance(c_map[query_city],
#                                                                                          c_map[city_near_y])
#                 if dist1 < dist2:
#                     res.append(city_near_x)
#                 else:
#                     res.append(city_near_y)
#     return res
#
#
# if __name__ == '__main__':
#     cities = ['axx', 'axy', 'az', 'axd', 'aa', 'abc', 'abs']
#     xs = [0, 1, 2, 4, 5, 0, 1]
#     ys = [1, 2, 5, 3, 4, 2, 0]
#
#     query_cities = ['axx', 'axy', 'abs']
#     print(find_nearest_cities_3(xs, ys, cities, query_cities))
#
# ''''native '''
#
#
# class City():
#     def __init__(self, name, x, y):
#         self.name = name
#         self.x = x
#         self.y = y
#
#
# class Solution():
#     def __init__(self, cities, xCo, yCo):
#         self.cityList = {}
#         self.query = ['abs', 'axx', 'axy', "zmm"]
#         for i in range(len(cities)):
#             self.cityList[cities[i]] = City(cities[i], xCo[i], yCo[i])
#
#     def getNearestCity(self):
#         res = []
#         for q in self.query:
#             minDist = float('inf')
#             curClosestCity = ""
#
#             if q in self.cityList:
#                 qx, qy = self.cityList[q].x, self.cityList[q].y
#                 for key, val in self.cityList.items():
#                     if key != self.cityList[q].name:
#                         if val.x == qx or val.y == qy:
#                             manhattanDist = abs(val.x - qx) + abs(val.y - qy)
#                             if manhattanDist < minDist:
#                                 minDist = manhattanDist
#                                 curClosestCity = val.name
#                             elif manhattanDist == minDist:
#                                 if curClosestCity > val.name:
#                                     curClosestCity = val.name
#
#             res.append(curClosestCity)
#         res.sort()
#         return res
#
#
# cities = ['axx', 'axy', 'az', 'axd', 'aa', 'abc', 'abs', 'p']
# xs = [0, 1, 2, 4, 5, 0, 1, 0]
# ys = [1, 2, 5, 3, 4, 2, 0, 2]
# s = Solution(cities, xs, ys)
# print(s.getNearestCity())