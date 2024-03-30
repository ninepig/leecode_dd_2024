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

'''

https://www.1point3acres.com/bbs/thread-1050540-1-1.html
https://www.1point3acres.com/bbs/thread-1045459-1-1.html
这道题就是纯手速 已经熟练度

'''
class city:
    def __init__(self,x:int,y:int,name:str):
        self.x = x
        self.y = y
        self.name = name # city name

    def __str__(self):
        return str(self.x) + " " + str(self.y) + " " + self.name
class solution:
    ## only return one city
    def queryCities(self,x_list:list[int],y_list:list[int],cities:list[str],query_cities:list[str])->list[str]:
        if not x_list or not y_list or not cities or not query_cities:
            return ""
        city_x_list = collections.defaultdict(list)
        city_y_list = collections.defaultdict(list)
        city_city_list = dict()

        ## preprocessing
        ## form  x-city, y-city, city_name-city dicts for better searching
        for i in range(len(x_list)):
            city_x_pos, city_y_pos,city_name = x_list[i],y_list[i],cities[i]
            cur_city = city(city_x_pos,city_y_pos,city_name)
            city_x_list[city_x_pos].append(cur_city)
            city_y_list[city_y_pos].append(cur_city)
            city_city_list[city_name] = cur_city

        # print(city_y_list)
        # print(city_city_list)
        # print(city_x_list)
        ## query process
        '''
        1 try to locate that in x or y list
          1.1 if not existed --> return none
        2 find closed one in candidate 
        '''
        res = []
        for query_city in query_cities:
            if query_city not in city_city_list : ## check if existed
               res.append("NONE")
            else:
                target_city = city_city_list[query_city]
                target_x,target_y = target_city.x,target_city.y
                candidate_list = []
                ## using a judge here ? i dont think so..
                for candidate_x_city in city_x_list[target_x]:
                    if candidate_x_city.name != target_city.name:
                        candidate_list.append(candidate_x_city)
                for candidate_y_city in city_y_list[target_y]:
                    if candidate_y_city.name != target_city.name:
                        candidate_list.append(candidate_y_city)

                for item in candidate_list:
                    print(item)

                closed_candidate = self.findClosedCandidate(target_city,candidate_list)
                res.append(closed_candidate)

        return res

    def findClosedCandidate(self, target_city, matching_city):
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

    def queryCitiesBinarySearchWay(self,x_list:list[int],y_list:list[int],cities:list[str],query_cities:list[str])->list[str]:
        # edge case
        if not x_list or not y_list or not cities or not query_cities:
            return []
        ## ignore length different , length = 0

        ## preprocessing
        x_city_list_dict = collections.defaultdict(list)
        y_city_list_dict = collections.defaultdict(list)
        city_name_city_dict = dict()

        ## form list
        for i in range(len(x_list)):
            cur_city_x,cur_city_y,cur_city_name = x_list[i],y_list[i],cities[i]
            cur_city = city(cur_city_x,cur_city_y,cur_city_name)
            x_city_list_dict[cur_city_x].append(cur_city)
            y_city_list_dict[cur_city_y].append(cur_city)
            city_name_city_dict[cur_city_name] = cur_city

        # preprocessing  for binary search
        ## for x pos city dict, we binary search by y pos
        for x_city_list in x_city_list_dict.values():
            x_city_list.sort(key=lambda city:city.y)
        ## for y pos city dict, we binary search by x pos
        for y_city_list in y_city_list_dict.values():
            y_city_list.sort(key= lambda city:city.x)

        res = []
        ## query
        for query_city in query_cities:
            print(query_city)
            if query_city not in city_name_city_dict:
               res.append("NONE")
            else:
                candidate_list = []
                target_city = city_name_city_dict[query_city]
                target_city_x, target_city_y = target_city.x, target_city.y
                if target_city_x in x_city_list_dict:
                    lower,higher = self.binarySearchYpos(x_city_list_dict[target_city_x],target_city)
                    if lower:
                        candidate_list.append(lower)
                    if higher:
                        candidate_list.append(higher)
                if target_city_y in y_city_list_dict:
                    lower,higher = self.binarySearchXpos(y_city_list_dict[target_city_y],target_city)
                    if lower:
                        candidate_list.append(lower)
                    if higher:
                        candidate_list.append(higher)
                final = self.findClosedCandidateSec(candidate_list,target_city)
                res.append(final)

        return res



    ##逻辑写错了 minDiff
    # def findClosedCandidate(self, target_city, candidate_list):
    #     res = ""
    #     minDiff = 0 ## 这里应该是 math.inf 无穷大！！ 因为是比小值。。
    #     for candidate in candidate_list:
    #         cur_diff = abs(target_city.x - candidate.x) + abs(target_city.y - candidate.y)
    #         if cur_diff < minDiff:
    #             res = candidate.name
    #             minDiff = cur_diff
    #         if minDiff == cur_diff: ## same distance , order by lexi
    #             res = res if res < candidate.name else candidate.name
    #             # final_city_name = city.name if city.name < final_city_name else final_city_name
    #
    #     return res


    def binarySearchYpos(self, target_x_list, target_city):
        left = 0
        right = len(target_x_list)
        lower = None
        higher = None
        target = 0
        while left < right:
            mid = left + (right - left) // 2
            if target_x_list[mid].name == target_city.name:
                target = mid
                break
            elif target_x_list[mid].y > target_city.y:
                right = mid - 1
            else:
                left = mid
        if target - 1 >= 0:
            lower = target_x_list[target - 1]
        if target + 1 < len(target_x_list):
            higher = target_x_list[target + 1]

        return lower,higher

    def binarySearchXpos(self, target_y_list, target_city):
        left = 0
        right = len(target_y_list)
        lower = None
        higher = None
        target = 0
        while left < right:
            mid = left + (right - left) // 2
            if target_y_list[mid].name == target_city.name:
                target = mid
                break
            elif target_y_list[mid].x > target_city.x:
                right = mid - 1
            else:
                left = mid
        if target - 1 >= 0:
            lower = target_y_list[target - 1]
        if target + 1 < len(target_y_list):
            higher = target_y_list[target + 1]

        return lower,higher

    def findClosedCandidateSec(self, candidate_list, target_city):
        final_name = ""
        min_diff = math.inf
        for candidate in candidate_list:
            cur_diff = abs(target_city.x - candidate.x) + abs(target_city.y - candidate.y)
            if cur_diff < min_diff:
                min_diff = cur_diff
                final_name = candidate.name
            if cur_diff == min_diff:
                final_name = final_name if final_name < candidate.name else candidate.name
        return final_name

if __name__ == '__main__':
    cities = ['axx', 'axy', 'az', 'axd', 'aa', 'abc', 'abs','add']
    xs = [0, 1, 2, 4, 5, 0, 1, 0]
    ys = [1, 2, 5, 3, 4, 2, 0, 0]
    query_cities = ['axx', 'axy', 'abs','add']
    solution = solution()
    # print(solution.queryCities(xs, ys, cities, query_cities))
    # ['abc', 'abc', 'add', 'abs']
    print(solution.queryCitiesBinarySearchWay(xs, ys, cities, query_cities))