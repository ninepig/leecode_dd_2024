import collections
import math


class City:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def __str__(self):
        return "name " + self.name + " x " + str(self.x) + " y " + str(self.y)


class Solution:
    def getNearCity(self, city_name_list, city_x_list, city_y_list, queries):
        ## santity check
        if not city_name_list or not city_x_list or not city_y_list or not queries:
            raise Exception("wrong input")

        city_dict = dict()
        x_city_dict = collections.defaultdict(list)
        y_city_dict = collections.defaultdict(list)

        for i in range(len(city_name_list)):
            cur_city = City(city_name_list[i], city_x_list[i], city_y_list[i])
            city_dict[city_name_list[i]] = cur_city
            x_city_dict[city_x_list[i]].append(cur_city)
            y_city_dict[city_y_list[i]].append(cur_city)

            ## we sorting x_city_dict by y's value  same as y city by x value for binarysearch

        for item in x_city_dict.values():
            item.sort(key=lambda x: x.y)

        for item in y_city_dict.values():
            item.sort(key=lambda x: x.x)

        res = []

        ## starting query
        ## for each query, we try to located higher/lower city with x/y value in list, then located final one
        for query in queries:
            if query not in city_dict:
                res.append("NONE")
            else:
                target_city = city_dict[query]
                target_x = target_city.x
                target_y = target_city.y
                candidate_list = []
                if target_x in x_city_dict:
                    lower, higher = self.binarySearchXbased(x_city_dict[target_x], target_city)
                    if lower:
                        candidate_list.append(lower)
                    if higher:
                        candidate_list.append(higher)
                if target_y in y_city_dict:
                    lower, higher = self.binarySearchYbased(y_city_dict[target_y], target_city)
                    if lower:
                        candidate_list.append(lower)
                    if higher:
                        candidate_list.append(higher)

                # print(candidate_list)
                for item in candidate_list:
                    print(item)
                final_string = self.compareDifference(candidate_list, target_city)

                res.append(final_string)

        return res

    def compareDifference(self, target_list, target_city):
        distance = math.inf
        final_name = ""
        for candidate in target_list:
            cur_distance = abs(candidate.x - target_city.x) + abs(candidate.y - target_city.y)
            if cur_distance < distance:
                ## forget to set name here  bug !
                distance = cur_distance
                final_name = candidate.name
            if cur_distance == distance:
                final_name = final_name if final_name < candidate.name else candidate.name

        return final_name

    def binarySearchXbased(self, target_list, target_city):
        ## x based means we need sort by y
        left, right = 0, len(target_list)
        start = 0
        lower = None
        higher = None
        while left < right:
            mid = left + (right - left) // 2
            if target_list[mid].name == target_city.name:
                start = mid
                break
            elif target_list[mid].y < target_city.y:
                left = mid
            else:
                right = mid - 1

        if start - 1 >= 0:
            lower = target_list[start - 1]
        if start + 1 < len(target_list):
            higher = target_list[start + 1]

        return lower, higher

    def binarySearchYbased(self, target_list, target_city):
        ## xy based means we need sort by x
        left, right = 0, len(target_list)
        start = 0
        lower = None
        higher = None
        while left < right:
            mid = left + (right - left) // 2
            if target_list[mid].name == target_city.name:
                start = mid
                break
            elif target_list[mid].x < target_city.x:
                left = mid
            else:
                right = mid - 1

        if start - 1 >= 0:
            lower = target_list[start - 1]

        if start + 1 < len(target_list):
            higher = target_list[start + 1]

        return lower, higher


cities = ['axx', 'axy', 'az', 'axd', 'aa', 'abc', 'abs', 'add', 'ddd']
xs = [0, 1, 2, 4, 5, 0, 1, 0, 1]
ys = [1, 2, 5, 3, 4, 2, 0, 0, 9]
query_cities = ['axx', 'axy', 'abs', 'add']

sol = Solution()
print(sol.getNearCity(cities, xs, ys, query_cities))
