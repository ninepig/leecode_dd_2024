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
import math


class City:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y


class solution:
    def queryNearestCity(self, cities: list[str], list_x: list[int], list_y: list[int], querys: list[str]) -> list[str]:
        ## santity check
        if not cities or len(cities) == 0:
            return []

        cityname_city_dict = dict()
        x_city_list = collections.defaultdict(list)
        y_city_list = collections.defaultdict(list)

        ## building dict for better query
        for idx, name in enumerate(cities):
            cur_city = City(name, list_x[idx], list_y[idx])
            cityname_city_dict[name] = cur_city
            x_city_list[list_x[idx]].append(cur_city)
            y_city_list[list_y[idx]].append(cur_city)

            ## using liner search , going through all candidate if we have x or y matched
        ## option 1
        ## using binaery search to decreasing liner time to lgn
        ## option 2

        ## bug, sort value() !!
        for item in x_city_list.values():
            # sorted(item,key = lambda x:x.y) ## sort by y's value
            item.sort(key= lambda x:x.y)
        for item in y_city_list.values():
            item.sort(key= lambda x: x.x) ## sort by x's value

        res = []

        for query in querys:
            if query not in cityname_city_dict:  ## no candidate
                res.append(query)
            else:
                ## found candidate city in x list and y list
                candidate_list = []
                target_city = cityname_city_dict[query]
                target_city_x = target_city.x
                target_city_y = target_city.y
                if target_city_x in x_city_list:
                    lower,higher = self.binarySearchY(x_city_list[target_city_x],target_city)
                    if lower:
                        candidate_list.append(lower)
                    if higher:
                        candidate_list.append(higher)
                if target_city_y in y_city_list:
                    lower,higher = self.binarySearchX(y_city_list[target_city_y],target_city)
                    if lower:
                        candidate_list.append(lower)
                    if higher:
                        candidate_list.append(higher)
                final_city = self.compareDistance(target_city,candidate_list)
                res.append(final_city)

        return res

    def compareDistance(self, target_city: City, candidate_list: list[City]):
        min_distance = math.inf
        final_name = ""

        for city in candidate_list:
            distance = abs(city.x - target_city.x) + abs(city.y - target_city.y)
            if distance < min_distance:
                min_distance = distance
                final_name = city.name
            elif distance == min_distance:
                final_name = city.name if city.name < final_name else final_name

        return final_name

    # def binarySearchXlist(self, target_city: City, city_list: list[City]):
    #     left = 0
    #     right = len(city_list)
    #     target = 0
    #     lower = None
    #     higher = None
    #     print("x search start")
    #     while left < right:
    #         mid = left + (right - left) // 2
    #         if city_list[mid].name == target_city.name:
    #             target = mid  ## 利用一个target 来保存目标位
    #             break
    #         elif city_list[mid].x > target_city.x:
    #             right = mid - 1
    #         else:
    #             left = mid  ## 因为我们要靠左， 所以尽量left 不要减 1 所以让right 逼近
    #         # elif city_list[mid].x < target_city.x:# 换一种写法
    #         #     left = mid
    #         # else:
    #         #     right = mid - 1 ## 因为我们要靠左， 所以尽量left 不要减 1 所以让right 逼近
    #     if target - 1 >= 0:
    #         lower = city_list[target - 1]
    #
    #     if target + 1 < len(city_list):
    #         higher = city_list[target + 1]
    #
    #     print("x search end")
    #
    #     return lower, higher
    #
    # def binarySearchYlist(self, target_city: City, city_list: list[City]):
    #     left = 0
    #     right = len(city_list)
    #     target = 0
    #     lower = None
    #     higher = None
    #
    #     print("y search start")
    #
    #     while left < right:
    #         mid = left + (right - left) // 2
    #         if city_list[mid].name == target_city.name:
    #             target = mid  ## 利用一个target 来保存目标位
    #             break
    #         elif target_city.y < city_list[mid].y:
    #             right = mid - 1
    #         else:
    #             left = mid  ## 因为我们要靠左， 所以尽量left 不要减 1 所以让right 逼近
    #         print(str(left) + "xx" + str(right) + "xx")
    #
    #     if target - 1 >= 0:
    #         lower = city_list[target - 1]
    #
    #     if target + 1 < len(city_list):
    #         higher = city_list[target + 1]
    #
    #     print("y search end")
    #
    #     return lower, higher
    def binarySearchX(self,city_list,target_city):
        left = 0
        right = len(city_list)
        target = 0
        lower = None
        higher = None
        while left < right:
            mid = left + (right - left) // 2
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
        right = len(city_list)
        target = 0
        lower = None
        higher = None
        while left < right:
            mid = left + (right - left) // 2
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
    cities = ['axx', 'axy', 'az', 'axd', 'aa', 'abc', 'abs', 'add']
    xs = [0, 1, 2, 4, 5, 0, 1, 0]
    ys = [1, 2, 5, 3, 4, 2, 0, 0]
    query_cities = ['axx', 'axy', 'abs', 'add']
    solution = solution()
    print(solution.queryNearestCity(cities, xs, ys, query_cities))


