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

input :
cities
list_x
list_y (integer?)
querys

output
1 if query not exists 'None'
2 if query city does not have any same x or y value with othercity, mean can not reachable --> 'None'
3 if query city does have any same x or y , we choose the same distance
4 if same distance, order by city name --> lexi order

'''
import collections
from bisect import bisect


class City:
    def __init__(self,cityName,cityX,cityY):
        self.name = cityName
        self.x = cityX
        self.y = cityY

    def __str__(self):
        return self.name + " " + str(self.x) + " " + str(self.y)

class solution:
    def find_nearest_citiesNormal(self, x_list, y_list, cities, query_cities):
        # step 1 validte input edge case, ignore here

        # step 2 build cities dict | x value - cityname dict | y value city name list

        x_city_dict = collections.defaultdict(list)
        y_city_dict = collections.defaultdict(list)
        city_name_city_dict = collections.defaultdict()

        for idx in range(len(cities)):
            city = City(cities[idx], x_list[idx], y_list[idx])
            x_city_dict[x_list[idx]].append(city)
            y_city_dict[y_list[idx]].append(city)
            city_name_city_dict[cities[idx]] = city

        # query with city name
        res = []

        for query_city in query_cities:
            # if city not exist , return 'none'
            if query_city not in city_name_city_dict:
                res.append('NONE')
                continue
            else:
                # temp city in dict
                cur_city = city_name_city_dict[query_city]
                # find if there is city has same x or same y
                cur_x = cur_city.x
                cur_y = cur_city.y
                matching_city = []
                ## looping to get target city, potential place to improve
                if cur_x in x_city_dict:
                    # loop to compare all city has same x value
                    target_cities = x_city_dict[cur_x]
                    for target_city in target_cities:
                        if target_city != cur_city:
                            matching_city.append(target_city)
                if cur_y in y_city_dict:
                    target_cities = y_city_dict[cur_y]
                    for target_city in target_cities:
                        if target_city != cur_city:
                            matching_city.append(target_city)
                nearest_city = self.findMinDistance(matching_city,cur_city)
                res.append(nearest_city)

        return res

    def findMinDistance(self, target_cities, cur_city):

        minDistance = float('inf')
        final_target = ""

        for target_city in target_cities:
            curDistance = abs(cur_city.x - target_city.x) + abs(cur_city.y - target_city.y)
            if curDistance < minDistance:
                minDistance = curDistance
                final_target = target_city.name
            if curDistance == minDistance:
                final_target = final_target if final_target < target_city.name else target_city.name

        return final_target


    '''
    python 关键的一点 dict.sort() 直接在原地sort 
    xxx = sorted(xxx,xxx) 这个会赋值
    '''
    def find_nearest_citiesBinarySearcgWay(self, x_list, y_list, cities, query_cities):
        # step 1 validte input edge case, ignore here

        # step 2 build cities dict | x value - cityname dict | y value city name list

        x_city_dict = collections.defaultdict(list)
        y_city_dict = collections.defaultdict(list)
        city_name_city_dict = collections.defaultdict()

        for idx in range(len(cities)):
            city = City(cities[idx], x_list[idx], y_list[idx])
            x_city_dict[x_list[idx]].append(city)
            y_city_dict[y_list[idx]].append(city)
            city_name_city_dict[cities[idx]] = city

        ## sort x_city_dict with y's value
        for key in x_city_dict:
            x_city_dict[key].sort(key = lambda city:city.y)

        ## sort y_city_dict with x's value
        for key in y_city_dict:
            y_city_dict[key].sort(key = lambda city:city.x)

        # print(x_city_dict)
        # print(y_city_dict)

        res = []
        for query_city in query_cities:
            # if city not exist , return 'none'
            if query_city not in city_name_city_dict:
                res.append('NONE')
                continue
            else:
                # temp city in dict
                cur_city = city_name_city_dict[query_city]
                # find if there is city has same x or same y
                cur_x = cur_city.x
                cur_y = cur_city.y
                matching_city = []
                if cur_x in x_city_dict:
                    # improving, only add closed 2 city in match with binary tree, so we dont need loop all
                    target_cities = x_city_dict[cur_x]
                    ## finding lower or higher city with cur city's y value
                    # using cur_y to located two nearest city
                    lower_city,higher_city = self.binarySearchX(target_cities,cur_city)
                    if lower_city:
                        matching_city.append(lower_city)
                    if higher_city:
                        matching_city.append(higher_city)

                if cur_y in y_city_dict:
                    target_cities = y_city_dict[cur_y]
                    ## finding lower or higher city with cur city's y value
                    # using cur_y to located two nearest city
                    lower_city, higher_city = self.binarySearchY(target_cities, cur_city)
                    if lower_city:
                        matching_city.append(lower_city)
                    if higher_city:
                        matching_city.append(higher_city)
                # print("current query city name is ",query_city)
                # print("querycity's matching city is ",matching_city)
                # for city in matching_city:
                #     print(city )

                nearest_city = self.findMinDistance(matching_city, cur_city)

                # print("nearcity is ",nearest_city)
                res.append(nearest_city)
        return res

    ## target_city is already sorted by y or x
    def binarySearchX(self, target_cities, cur_city):
        left = 0
        right = len(target_cities)
        target = 0
        while left < right:
            mid = left + (right - left)//2
            if target_cities[mid].name == cur_city.name:
                target = mid
                break
            else:
                ## cur city 's y is too small
                if target_cities[mid].y > cur_city.y:
                    right = mid - 1
                else:
                    left = mid
        lower = None
        higher = None
        if target - 1 >= 0:
            lower = target_cities[target - 1]
        if target + 1 < len(target_cities):
            higher = target_cities[target + 1]

        return lower,higher


    def binarySearchY(self, target_cities, cur_city):
        left = 0
        right = len(target_cities)
        target = 0
        while left < right:
            mid = left + (right - left)//2
            if target_cities[mid].name == cur_city.name:
                target = mid
                break
            else:
                ## cur city 's x is too small, binery search result on left side
                if target_cities[mid].x > cur_city.x:
                    right = mid - 1
                else:
                    left = mid
        lower = None
        higher = None
        if target - 1 >= 0:
            lower = target_cities[target - 1]
        if target + 1 < len(target_cities):
            higher = target_cities[target + 1]
        return lower,higher


if __name__ == '__main__':
    cities = ['axx', 'axy', 'az', 'axd', 'aa', 'abc', 'abs','add']
    xs = [0, 1, 2, 4, 5, 0, 1, 0]
    ys = [1, 2, 5, 3, 4, 2, 0, 0]

    query_cities = ['axx', 'axy', 'abs','add']
    solution = solution()
    print(solution.find_nearest_citiesNormal(xs, ys, cities, query_cities))
    print(solution.find_nearest_citiesBinarySearcgWay(xs, ys, cities, query_cities))

