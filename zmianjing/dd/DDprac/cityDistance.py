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
import bisect
import collections
import math


class city:
    def __init__(self,x:int,y:int,name:str):
        self.x = x
        self.y = y
        self.name = name # city name

    def __str__(self):
        return str(self.x) + " " + str(self.y) + " " + self.name


class Solution:
    def queryCities(self,x_list:list[int],y_list:list[int],cities:list[str],query_cities:list[str]):
        if not x_list or not y_list or not cities or not query_cities:
            return []
        ## corner case if length different ---> we will return []
        x_city_list = collections.defaultdict(list)
        y_city_list = collections.defaultdict(list)
        city_name_city_list = collections.defaultdict()
        ## form list / dict
        for idx in range(len(x_list)):
            cur_x = x_list[idx]
            cur_y = y_list[idx]
            cur_cityname = cities[idx]
            cur_city = city(cur_x,cur_y,cur_cityname)
            x_city_list[cur_x].append(cur_city)
            y_city_list[cur_y].append(cur_city)
            city_name_city_list[cur_cityname] = cur_city

        res = []
        '''
        output
        1 if query not exists 'None'
        2 if query city does not have any same x or y value with othercity, mean can not reachable --> 'None'
        3 if query city does have any same x or y , we choose the same distance
        4 if same distance, order by city name --> lexi order
'''
        for target in query_cities:
            if target not in city_name_city_list: # we dont have this city here
                res.append("NONE")
                continue
            else:
                target_city = city_name_city_list[target] ## we got target city
                target_x = target_city.x
                target_y = target_city.y
                matching_city = []
                ## finding city with same x or y
                if target_x in x_city_list:
                    target_cities_same_x = x_city_list[target_x]
                    for temp in target_cities_same_x:
                        if temp != target_city:
                            matching_city.append(temp)
                if target_y in y_city_list:
                    target_cities_same_y = y_city_list[target_y]
                    for temp in target_cities_same_y:
                        if temp != target_city:
                            matching_city.append(temp)
                closed_city = self.findClosedCity(target_city,matching_city)
                res.append(closed_city)

        return res

    def findClosedCity(self, target_city, matching_city):
        final_city_name = ""
        minDistance = math.inf
        for city in matching_city:
            cur_distance = abs(city.x - target_city.x) + abs(city.y - target_city.y)
            if cur_distance < minDistance:
                minDistance = cur_distance
                final_city_name = city.name
            if cur_distance == minDistance:
                final_city_name = city.name if city.name < final_city_name else final_city_name

        return final_city_name



    def queryCitiesBSway(self,x_list:list[int],y_list:list[int],cities:list[str],query_cities:list[str]):
        if not x_list or not y_list or not cities or not query_cities:
            return []
        ## corner case if length different ---> we will return []
        x_city_list = collections.defaultdict(list)
        y_city_list = collections.defaultdict(list)
        city_name_city_list = collections.defaultdict()
        ## form list / dict
        for idx in range(len(x_list)):
            cur_x = x_list[idx]
            cur_y = y_list[idx]
            cur_cityname = cities[idx]
            cur_city = city(cur_x,cur_y,cur_cityname)
            x_city_list[cur_x].append(cur_city)
            y_city_list[cur_y].append(cur_city)
            city_name_city_list[cur_cityname] = cur_city

        ## sort in each list, sorting by x and y correndingly
        ## if that is y's list
        for key in x_city_list:
            x_city_list[key].sort(key = lambda city:city.y)

        for key in y_city_list:
            y_city_list[key].sort(key = lambda city:city.x)

        res = []

        # for key in x_city_list:
        #     print(key)
        #     for item in x_city_list[key]:
        #         print(item)


        for target in query_cities:
            if target not in city_name_city_list:
                res.append("NONE")
                continue
            else:
                matching_city = []
                target_city = city_name_city_list[target]
                target_x = target_city.x
                target_y = target_city.y
                if target_x in x_city_list:
                    target_cities = x_city_list[target_x] ## candidates with same x
                    ## we use Binary search to locate upper and lower candidate comparing to target
                    ## BISECT can not be used to locate string , so we have to implement our own bs way
                    # higher_city = bisect.bisect_right(target_cities,tatarget)
                    # lower_city =bisect.bisect_left(target_cities,target)
                    # print(higher_city,lower_city)
                    # todo test python binary search
                    # break
                    lower_city, higher_city = self.binarySearchXcity(target_city,target_cities)
                    if lower_city :
                        matching_city.append(lower_city)
                    if higher_city:
                        matching_city.append(higher_city)

                if target_y in y_city_list:
                    target_cities = y_city_list[target_y]  ## candidates with same y

                    lower_city, higher_city = self.binarySearchycity(target_city, target_cities)
                    if lower_city:
                        matching_city.append(lower_city)
                    if higher_city:
                        matching_city.append(higher_city)

                final_city = self.findClosedCity(target_city,matching_city)
                res.append(final_city)

        return res

    def binarySearchXcity(self, cur_city,target_cities):
        print( cur_city )
        print(len(target_cities))
        left = 0
        right = len(target_cities)
        target = 0
        while left < right:
            mid = left + (right - left) // 2
            print(mid)
            if target_cities[mid].name == cur_city.name:
                target = mid
                break
            else:
                ## cur city 's y is too small
                if target_cities[mid].y > cur_city.y:
                    right = mid - 1
                else:
                    left = mid
        print("end")
        lower = None
        higher = None
        if target - 1 >= 0:
            lower = target_cities[target - 1]
        if target + 1 < len(target_cities):
            higher = target_cities[target + 1]

        return lower, higher

    def binarySearchycity(self, target_city, target_cities):
        left, right = 0, len(target_cities)  ## bug 在这里 二分法 右侧边界
        target_index = 0
        while left < right:
            mid = left + (right - left) // 2
            print(mid)
            if target_cities[mid].name == target_city.name:
                target_index = mid
                break
            else:
                if target_cities[mid].x > target_city.x:
                    ## target city is on left side
                    right = mid - 1
                else:
                    left = mid
        lower = None
        higher = None
        if target_index - 1 >= 0:
            lower = target_cities[target_index - 1]
        if target_index + 1 < len(target_cities):
            higher = target_cities[target_index + 1]

        return lower, higher

    # def binarySearchycity(self, cur_city, target_cities):
    #     left = 0
    #     right = len(target_cities)
    #     target = 0
    #     while left < right:
    #         mid = left + (right - left) // 2
    #         if target_cities[mid].name == cur_city.name:
    #             target = mid
    #             break
    #         else:
    #             ## cur city 's x is too small, binery search result on left side
    #             if target_cities[mid].x > cur_city.x:
    #                 right = mid - 1
    #             else:
    #                 left = mid
    #     lower = None
    #     higher = None
    #     if target - 1 >= 0:
    #         lower = target_cities[target - 1]
    #     if target + 1 < len(target_cities):
    #         higher = target_cities[target + 1]
    #     return lower, higher
if __name__ == '__main__':
    cities = ['axx', 'axy', 'az', 'axd', 'aa', 'abc', 'abs','add']
    xs = [0, 1, 2, 4, 5, 0, 1, 0]
    ys = [1, 2, 5, 3, 4, 2, 0, 0]
    query_cities = ['axx', 'axy', 'abs','add']
    solution = Solution()
    # print(solution.queryCities(xs, ys, cities, query_cities))
    print(solution.queryCitiesBSway(xs, ys, cities, query_cities))