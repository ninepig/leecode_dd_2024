'''
经典题目
似乎最新的面经有改版.但是不确定 先做经典版
假设空地里有customer，求离最多数量customer最近的dashmart，会有tie的情况
如果是这样, 应该是location 会增加一个customer 数量
然后根据数量做一个判断.
bfs计算出到每个点的距离的核心算法应该是不变的
变化的就是location上面有数量
按照数量/距离做一个比较. 不会很难


DashMart is a warehouse run by DoorDash that houses items found in convenience stores, grocery stores, and restaurants. We have a city with open roads, blocked-off roads, and DashMarts.

City planners want you to identify how far a location is from its closest DashMart.

You can only travel over open roads (up, down, left, right). Locations are given in `[row, col]` format.

Example 1:

Given a grid where:
- 'O' represents an open road that you can travel over in any direction (up, down, left, or right).
- 'X' represents a blocked road that you cannot travel through.
- 'D' represents a DashMart.

The grid is provided as a 2D array, and a list of locations is provided where each location is a pair `[row, col]`.
[
  ['X', 'O', 'O', 'D', 'O', 'O', 'X', 'O', 'X'], #0
  ['X', 'O', 'X', 'X', 'X', 'O', 'X', 'O', 'X'], #1
  ['O', 'O', 'O', 'D', 'X', 'X', 'O', 'X', 'O'], #2
  ['O', 'O', 'D', 'O', 'D', 'O', 'O', 'O', 'X'], #3
  ['O', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'X'], #4
  ['X', 'O', 'X', 'O', 'O', 'O', 'O', 'X', 'X'], #5
]

List of pairs `[row, col]` for locations:
[
  [200, 200],
  [1, 4],
  [0, 3],
  [5, 8],
  [1, 8],
  [5, 5],
]

Your task is to return the distance for each location from the closest DashMart.

Provided:

- `city: char[][]`
- `locations: int[][]`

**Return:**

- `answer: int[]`
'''
import collections
from typing import List


class Solution:
    '''bfs from 'D' postion , update a dict with {(x,y):distance} ,key is x, y tumple, value is distance '''
    def get_mart_distance(self,city:List[List[str]],location:List[List[int]]):
        queue = collections.deque([])
        distance_dict = dict()
        # find 'D' in map and put into queue,
        rows = len(city)
        cols = len(city[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for i in range(rows):
            for j in range(cols):
                if city[i][j] == 'D': # we found a dashmart
                    queue.append((i,j,0))
                    distance_dict[(i,j)] = 0
        print(queue)
        while queue:
            print(len(queue))
            cur_pos = queue.popleft()
            for dir in directions:
                x,y,value = cur_pos[0],cur_pos[1],cur_pos[2]
                new_x  = x + dir[0]
                new_y  = y + dir[1]
                ## treat distance_dict as a visited dict
                if 0 <= new_x < rows and 0 <= new_y < cols and city[new_x][new_y] == ' ' and (new_x,new_y) not in distance_dict:
                    print(new_x,new_y,rows,cols)
                    queue.append((new_x,new_y,value + 1))
                    distance_dict[(new_x,new_y)] = value + 1

        res = []
        for city in location:
            if (city[0],city[1]) in distance_dict:
                res.append(distance_dict[(city[0],city[1])])

        return res

test =Solution()

city = [
    ['X', ' ', ' ', 'D', ' ', ' ', 'X', ' ', 'X'],
    ['X', ' ', 'X', 'X', ' ', ' ', ' ', ' ', 'X'],
    [' ', ' ', ' ', 'D', 'X', 'X', ' ', 'X', ' '],
    [' ', ' ', ' ', 'D', ' ', 'X', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X'],
    [' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X', 'X']
]

locations = [
    [2, 2],
    [4, 0],
    [0, 4],
    [2, 6],
]


print(test.get_mart_distance(city, locations))
