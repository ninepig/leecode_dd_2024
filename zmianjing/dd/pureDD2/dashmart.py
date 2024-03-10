'''
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


然后还问了follow up，如果char[][]里有'C'
代表customer，customer会选择离他最近的dashmart，求有最多的customers的dashmart

some detail
也就是test case 可以从墙出发
也就是x 是墙  但是也要记录到达的距离 这个是含义
follow up 格子里有c， c选择离他最近的d，求客人最多的店
https://www.1point3acres.com/bbs/thread-1047368-1-1.html
https://www.1point3acres.com/bbs/thread-1043914-1-1.html


'''
import collections
from collections import deque


class Solution:
    def findDistanceNearedDm(self,grids:list[list[int]],location:list[list[int]])-> list[int]:
        point_dm_distance_map = dict()
        rows = len(grids)
        cols = len(grids[0])
        queue = deque()
        dirctions = [(-1,0),(1,0),(0,1),(0,-1)]
        # starting from 'D'
        for i in range(rows):
            for j in range(cols):
                if grids[i][j] == 'D':
                    queue.append((i,j,0)) #把距离也加入，这个方法比较好 ,利用这个三元来做
                    point_dm_distance_map[(i,j)] = 0

        ## count distantce based on queue
        while queue:
            cur_node = queue.popleft()
            for direct in dirctions:
                new_x = cur_node[0] + direct[0]
                new_y = cur_node[1] + direct[1]
                dist = cur_node[2] ## 获得距离
                ## TODO 这里需要改， 也就是 x也需要加distance 同时 空格 入队
                # if (0 <= new_x < rows and 0 <= new_y < cols and grids[new_x][new_y] == ' ' and
                #         (new_x,new_y) not in point_dm_distance_map):
                if (0 <= new_x < rows and 0 <= new_y < cols and (new_x,new_y) not in point_dm_distance_map):
                    if grids[new_x][new_y] == ' ': ## if it can pass , we add that to queue
                        queue.append((new_x,new_y,dist + 1))
                        point_dm_distance_map[(new_x,new_y)] = dist + 1
                    elif grids[new_x][new_y] == 'X': ## if that is block, we still need add that to map
                        point_dm_distance_map[(new_x,new_y)] = dist + 1
        res = []

        for loc in location:
            x,y = loc[0],loc[1]
            if (x,y) in point_dm_distance_map:
                res.append(point_dm_distance_map[(x,y)])
            else:
                res.append("-1")

        return res

    '''
    然后还问了follow up，如果char[][]里有'C'
    代表customer，customer会选择离他最近的dashmart，求有最多的customers的dashmart
    '''
    def findMaxCustomerDm(self,grids:list[list[int]],location:list[list[int]])-> list[int]:
        # point_dm_distance_map = dict()
        rows = len(grids)
        cols = len(grids[0])
        queue = deque()
        dirctions = [(-1,0),(1,0),(0,1),(0,-1)]
        visited = set() # we should not use this
        dm_customercount_map = dict()
        # starting from ' C'
        for i in range(rows):
            for j in range(cols):
                if grids[i][j] == 'C':
                    visited.clear()
                    find_store = False
                    queue.append((i,j))
                    #有一个客户就加入一个点， 遇到第一个dashmart 就可以把他消化 ,那这个题目就应该是针对每一个customer 开始进行 ，这个时候就是单源了 不能是多源同时进行了
                    # 找到第一个dashmart ，然后dashmart + 1
                    visited.add((i,j))
                    while queue:
                        cur = queue.popleft()
                        for direct in dirctions:
                            new_x = cur[0] + direct[0]
                            new_y = cur[1] + direct[1]
                            if 0 <= new_x < rows and 0 <= new_y < cols and (new_x,new_y) not in visited and not find_store:
                                if grids[new_x][new_y] == ' ' or grids[new_x][new_y] == 'C' : # can pass 还有一种可能 就是这个位置也是人的情况 自己debug出来的！！牛逼了
                                   queue.append((new_x, new_y))
                                   visited.add((new_x, new_y))
                                if grids[new_x][new_y] == 'D' :# we found a store, we choose this as this is closed
                                   if(new_x,new_y) not in dm_customercount_map:
                                       dm_customercount_map[(new_x,new_y)] = 1
                                   else:
                                       dm_customercount_map[(new_x,new_y)] += 1
                                   find_store = True
        print(dm_customercount_map)
        return max(dm_customercount_map.values())




sol = Solution()
# city = [
#     ['X', 'C', 'C', 'D', 'C', ' ', 'X', ' ', 'X'],
#     ['X', ' ', 'X', 'X', ' ', ' ', ' ', ' ', 'X'],
#     [' ', ' ', 'C', 'D', 'X', 'X', ' ', 'X', ' '],
#     [' ', ' ', ' ', 'D', ' ', 'X', ' ', ' ', ' '],
#     [' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X'],
#     [' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X', 'X']
# ]

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

print(sol.findDistanceNearedDm(city, locations))