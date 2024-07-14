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

https://algo.itcharge.cn/01.Array/03.Array-Binary-Search/02.Array-Binary-Search-02/#_4-2-%E6%8E%92%E9%99%A4%E6%B3%95
'''
import collections
import math


class city:
    def __init__(self,name,x,y):
        self.name = name
        self.x = x
        self.y = y

class solution:
    ## form city name : city dict
    ## form x : list[city] dict
    ## form y : list[city] dict

    # time--> m * n*n  m --> query size n means city list
    def findNearCity(self,cities,list_x,list_y,queries):
        # santity check
        if not cities or not list_x or not list_y or not queries:
            return []
        if len(cities) != len(list_x) or len(cities) != len(list_y):
            return []

        n = len(cities)
        cityname_city_dict = dict()
        x_city_dict = collections.defaultdict(list)
        y_city_dict = collections.defaultdict(list)
        for i in range(n):
            city_name = cities[i]
            city_x = list_x[i]
            city_y = list_y[i]
            cur_city = city(city_name,city_x,city_y)
            cityname_city_dict[city_name] = cur_city
            x_city_dict[city_x].append(cur_city)
            y_city_dict[city_y].append(cur_city)
        ## after we have all list, we handling query
        ## we try to locate query's x , y
        ## find which city has same x , or same y
        ## put them into a candidate list
        ## comparing them with target city one by one , get the closed
        ## if distance even, order by lexorder

        res = []
        for query in queries:
            ## forget to add this , bug
            if query not in cityname_city_dict:
               res.append("NONE")
            else:
                candidate_list = []
                target_city = cityname_city_dict[query]
                target_city_x = target_city.x
                target_city_x_candidate_list = x_city_dict[target_city_x]
                target_city_y = target_city.y
                target_city_y_candidate_list = y_city_dict[target_city_y]

                for candidate_city in target_city_x_candidate_list:
                    if candidate_city.name != target_city.name:
                        candidate_list.append(candidate_city)

                for candidate_city in target_city_y_candidate_list:
                    if candidate_city.name != target_city.name:
                        candidate_list.append(candidate_city)

                final_city = self.getClosedCity(candidate_list,target_city)
                res.append(final_city)

        return res

    def getClosedCity(self,candidate_list,target_city):
        final_city_name = ""
        distance = math.inf
        for candidate in candidate_list:
            cur_dis = abs(candidate.x - target_city.x) + abs(candidate.y - target_city.y)
            if cur_dis < distance:
                distance = cur_dis
                final_city_name = candidate.name
            if cur_dis == distance:
                final_city_name = candidate.name if candidate.name < final_city_name else final_city_name
        return final_city_name

    ## m * nlogn / n *n *logn -->
    def findNearCityBSway(self,cities,list_x,list_y,queries):
        # santity check
        if not cities or not list_x or not list_y or not queries:
            return []
        if len(cities) != len(list_x) or len(cities) != len(list_y):
            return []

        n = len(cities)
        cityname_city_dict = dict()
        x_city_dict = collections.defaultdict(list)
        y_city_dict = collections.defaultdict(list)
        for i in range(n):
            city_name = cities[i]
            city_x = list_x[i]
            city_y = list_y[i]
            cur_city = city(city_name,city_x,city_y)
            cityname_city_dict[city_name] = cur_city
            x_city_dict[city_x].append(cur_city)
            y_city_dict[city_y].append(cur_city)

        ## bug, sort value() !!
        for item in x_city_dict.values():
            # sorted(item,key = lambda x:x.y) ## sort by y's value
            item.sort(key= lambda x:x.y)
        for item in y_city_dict.values():
            item.sort(key= lambda x: x.x) ## sort by x's value

        res = []
        for query in queries:
            ## forget to add this , bug
            if query not in cityname_city_dict:
                res.append("NONE")
            else:
                candidate_list = []
                target_city = cityname_city_dict[query]
                target_city_x = target_city.x
                target_city_y = target_city.y
                if target_city_x in x_city_dict:
                    lower,higher = self.binarySearchY(x_city_dict[target_city_x],target_city)
                    if lower:
                        candidate_list.append(lower)
                    if higher:
                        candidate_list.append(higher)
                if target_city_y in y_city_dict:
                    lower,higher = self.binarySearchX(y_city_dict[target_city_y],target_city)
                    if lower:
                        candidate_list.append(lower)
                    if higher:
                        candidate_list.append(higher)
                final_city = self.getClosedCity(candidate_list, target_city)
                res.append(final_city)

        return res

    def binarySearchX(self,city_list,target_city):
        left = 0
        right = len(city_list) - 1
        target = 0
        lower = None
        higher = None
        while left < right:
            mid = left + (right - left + 1) // 2
            if city_list[mid].name == target_city.name:
                target = mid ## 利用一个target 来保存目标位
                break
            elif city_list[mid].x > target_city.x:
                right = mid - 1
            else:
                left = mid ## 因为我们要靠左， 所以尽量left 不要减 1 所以让right 逼近
            # elif city_list[mid].x < target_city.x:# 换一种写法
            #     left = mid
            # else:
            #     right = mid - 1 ## 因为我们要靠左， 所以尽量left 不要减 1 所以让right 逼近
        if target - 1 >= 0:
            lower = city_list[target - 1]

        if target + 1 < len(city_list):
            higher = city_list[target + 1]

        return lower,higher


    def binarySearchY(self,city_list,target_city):
        left = 0
        right = len(city_list) - 1
        target = 0
        lower = None
        higher = None
        while left < right:
            mid = left + (right - left + 1) // 2
            if city_list[mid].name == target_city.name:
                target = mid ## 利用一个target 来保存目标位
                break
            elif target_city.y < city_list[mid].y:
                right = mid - 1
            else:
                left = mid ## 因为我们要靠左， 所以尽量left 不要减 1 所以让right 逼近

        if target - 1 >= 0:
            lower = city_list[target - 1]

        if target + 1 < len(city_list):
            higher = city_list[target + 1]

        return lower,higher

if __name__ == '__main__':
    cities = ['axx', 'axy', 'az', 'axd', 'aa', 'abc', 'abs','add']
    xs = [0, 1, 2, 4, 5, 0, 1, 0]
    ys = [1, 2, 5, 3, 4, 2, 0, 0]
    query_cities = ['axx', 'axy', 'abs','add']
    solution = solution()
    print(solution.findNearCity(cities,xs, ys, query_cities))
    # ['abc', 'abc', 'add', 'abs']
    print(solution.findNearCityBSway(cities,xs, ys,  query_cities))





















