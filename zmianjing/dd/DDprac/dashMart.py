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
'''
import collections


class solution:


    ## time : o(m*n) searching

    def getClosedMart(self,locations:list[list[int]],grid:list[list[str]]) -> list[int]:
        ''' bfs question
        1 we start travel from each 'D'
        2 store closed distance of each point to 'D' ## follow the o x d rule
            2.1 if x is a block, we can not pass, but we still need store ? if location will contain block?  need confirm
        3 check how much distance from map based on location
        '''
        if not locations or len(locations) == 0 : return []
        if not grid or len(grid) == 0 : return []
        distance_map = dict() ## dict not array
        queue = collections.deque()
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        ## inital queue
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'D':
                    queue.append((i,j,0))
                    distance_map[(i,j)] = 0

        ## bfs
        while queue:
            cur = queue.popleft()
            row,col,dis = cur[0],cur[1],cur[2]
            for dir in dirs:
                new_row = row + dir[0]
                new_col = col + dir[1]
                ## dict check method
                # print((new_row,new_col))
                if 0 <= new_row < rows and 0 <= new_col < cols and (new_row,new_col) not in distance_map:
                    if grid[new_row][new_col] == ' ' :
                        # if we can pass this node, we need cacl distance of this node and store that and put that to queue
                        queue.append((new_row,new_col,dis + 1))
                        distance_map[(new_row,new_col)] = dis + 1
                    elif grid[new_row][new_col] == 'X':
                        ## if we can not pass this node, we need storing his distance into map
                        distance_map[(new_row,new_col)] = dis + 1

        ## count res
        res = []
        for location in locations:
            if distance_map[(location[0],location[1])]:
                res.append(distance_map[location[0],location[1]])

        return res

    def getMostCustomerMart(self, locations: list[list[int]], grid: list[list[str]]) -> list[int]:
        if not locations or len(locations) == 0: return []
        if not grid or len(grid) == 0: return []
        mart_customer_count = dict()  ## dict not array
        visited = set()
        queue = collections.deque()
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'C' : # starting from any customer
                    queue.clear()
                    visited.clear()
                    queue.append((i,j))
                    find_store = False # add this flag to avoid loop
                    while queue:
                        cur = queue.popleft()
                        for dir in dirs:
                            new_row = cur[0] + dir[0]
                            new_col = cur[1] + dir[1]
                            if 0 <= new_row < rows and 0 <= new_col < cols and (new_row,new_col) not in visited and not find_store:
                                ## we still need judge if we can access some node , since it could be D we can not reach
                                if grid[new_row][new_col] == ' ' or grid[new_row][new_col] == 'C' : ## we can pass this pos
                                    queue.append((new_row,new_col)) ## add to queue
                                    visited.add((new_row,new_col)) # visited map
                                if grid[new_row][new_col] == 'D': ## we found a store
                                    find_store = True
                                    if (new_row,new_col) not in mart_customer_count:
                                        mart_customer_count[(new_row,new_col)] = 1
                                    else:
                                        mart_customer_count[(new_row,new_col)] += 1
        res = []
        # print(mart_customer_count)
        ## we could have mult store which same customer
        max_customer = max(mart_customer_count.values()) ## 要用max value（）才可以
        # print(max_customer)
        for key in mart_customer_count.keys():
            if mart_customer_count[key] == max_customer:
                res.append(key)

        return res



sol = solution()
# city = [
#     ['X', ' ', ' ', 'D', ' ', ' ', 'X', ' ', 'X'],
#     ['X', ' ', 'X', 'X', ' ', ' ', ' ', ' ', 'X'],
#     [' ', ' ', ' ', 'D', 'X', 'X', ' ', 'X', ' '],
#     [' ', ' ', ' ', 'D', ' ', 'X', ' ', ' ', ' '],
#     [' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X'],
#     [' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X', 'X']
# ]

city = [
    ['X', 'C', 'C', 'D', 'C', ' ', 'X', ' ', 'X'],
    ['X', ' ', 'X', 'X', ' ', ' ', ' ', ' ', 'X'],
    [' ', ' ', 'C', 'D', 'X', 'X', ' ', 'X', ' '],
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

print(sol.getMostCustomerMart(locations, city))

