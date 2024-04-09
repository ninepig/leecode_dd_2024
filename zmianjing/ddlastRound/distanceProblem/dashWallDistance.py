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
'''
不出意外 题目里应该会说 location 数组 会很大。 所以从d出发是最合适的
'''

class solution:

    def getClosedMart(self, locations: list[list[int]], grid: list[list[str]]) :
        ## santity check
        ## location could overrange
        if not locations or not grid:
            return []

        ## record  distance from each D , which starting from D
        distance_dict = dict()
        queue = []
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'D':
                    ## we store distance with x, y for easier handling
                    queue.append((i,j,0))
                    distance_dict[(i,j)] = 0 ## put dashmart's pos in map also

        while queue:
            cur_pos = queue.pop()
            cur_x , cur_y, cur_dis = cur_pos[0],cur_pos[1],cur_pos[2]
            for dir in dirs:
                new_x = cur_x + dir[0]
                new_y = cur_y + dir[1]
                if 0 <= new_x < rows and 0 <= new_y < cols and (new_x,new_y) not in distance_dict:
                    if grid[new_x][new_y] == ' ': ## can pass
                        queue.append((new_x,new_y,cur_dis + 1))
                        distance_dict[(new_x,new_y)] = cur_dis + 1
                    if grid[new_x][new_y] == 'x': ## can not paas, but we also need record that pos
                        distance_dict[(new_x,new_y)] = cur_dis + 1

        res = []
        for location in locations:
            if (location[0],location[1]) in distance_dict:
                res.append(distance_dict[(location[0],location[1])])

        return res

    ## we have c in grid now, find which dashmart has most c
    def getClosedMartMaxCustomer(self, locations: list[list[int]], grid: list[list[str]]) :
        ## location could overrange
        if not locations or not grid:
            return []

        ## record  distance from each D , which starting from D
        store_customer_dict = dict()
        queue = []
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        for i in range(rows):
            for j in range(cols):
                ## starting from c
                if grid[i][j] == 'C':
                    queue.clear()
                    visited.clear()
                    ## store found then need break
                    store_found = False
                    queue.append((i,j))
                    while queue:
                        current_pos = queue.pop()
                        current_x , current_y = current_pos[0],current_pos[1]
                        for dir in dirs:
                            new_x = current_x + dir[0]
                            new_y = current_y + dir[1]
                            if 0<= new_x < rows and 0 <= new_y < cols and (new_x,new_y) not in visited and not store_found:
                                if grid[new_x][new_y] == 'D' : # we found a store
                                    if (new_x,new_y) not in store_customer_dict:
                                        store_customer_dict[(new_x,new_y)] = 1
                                    else:
                                        store_customer_dict[(new_x,new_y)] += 1
                                    store_found = True
                                if grid[new_x][new_y] == ' ' or grid[new_x][new_y] == 'C':
                                    visited.add((new_x,new_y))
                                    queue.append((new_x,new_y)) ## free road or customer , we can pass
        print(store_customer_dict)
        max_value = max(store_customer_dict.values())
        res = []
        for item,value in store_customer_dict.items():
            if value == max_value:
                res.append(item)

        return res



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

customer_city = [
    ['X', 'C', 'C', 'D', 'C', ' ', 'X', ' ', 'X'],
    ['X', ' ', 'X', 'X', ' ', ' ', ' ', ' ', 'X'],
    [' ', ' ', 'C', 'D', 'X', 'X', ' ', 'X', ' '],
    [' ', ' ', 'C', 'D', 'C', 'X', ' ', ' ', ' '],
    [' ', ' ', ' ', 'C', ' ', 'X', ' ', ' ', 'X'],
    [' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X', 'X']
]


sol = solution()

print(sol.getClosedMart(locations, city))
print(sol.getClosedMartMaxCustomer(locations,customer_city))









