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

"""
o(m*n) time 

https://www.1point3acres.com/bbs/thread-796359-1-1.html ## 详细的题在这里

因为location的数量远大于 d的数量， 所以从 d出发 ，这样节省空间
https://www.1point3acres.com/bbs/thread-1052637-1-1.html

TODO 有可能location out of grid， 这点要考虑  

"""
class solution:
    def getClosedMart(self,locations:list[list[int]],grid:list[list[str]]) -> list[int]:
        '''
        for this question
        using bfs--> because it is bfs, so visited in map means it will has shorter distance
        we can start travel from 'D' , record distance each pos in grid ,and store in to a dict.
        dict can be a memorize table to trim travel and also can be used to store distance

        after searching
        we check each location, can the map, we can find the distance from each target location

        '''
        if not locations or not grid:
            return []

        queue = []
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        distance_map = dict() ## distance map and visited map

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'D':
                    queue.append((i,j,0)) ## put distance as 0 in to queue for easier calc

        ## bfs to travel all grid
        while queue:
            cur = queue.pop()
            cur_x,cur_y,cur_distance = cur[0],cur[1],cur[2]
            for dx,dy in dirs:
                new_x = cur_x + dx
                new_y = cur_y + dy
                ## key not in / key in map to check exist
                if 0<= new_x < rows and 0 <= new_y < cols and (new_x,new_y) not in distance_map:
                    if grid[new_x][new_y] == ' ': ## means we can pass, we need store the distance and put back to queue
                        distance_map[(new_x,new_y)] = cur_distance + 1
                        queue.append((new_x,new_y,cur_distance + 1))
                    if grid[new_x][new_y] == 'X': ## means wall, we can not pass, but we need store the location of that
                        distance_map[(new_x,new_y)] = cur_distance + 1

        ## check the distance from target to store location
        res = []
        for location in locations:
            if (location[0],location[1]) in distance_map:
                res.append(distance_map[location[0],location[1]])

        return res
        '''
        using bfs from any customer.
        find closed store from that customer
        use a dict to store how many customer goto this store

        loop to output customer count of each store
        '''

    def getMostCustomerCount(self, locations: list[list[int]], grid: list[list[str]]):

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
        for key in store_customer_dict.keys():
            if store_customer_dict[key] == max_value:
                res.append(key)

        return res


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




sol = solution()
city = [
    ['X', ' ', ' ', 'D', ' ', ' ', 'X', ' ', 'X'],
    ['X', ' ', 'X', 'X', ' ', ' ', ' ', ' ', 'X'],
    [' ', ' ', ' ', 'D', 'X', 'X', ' ', 'X', ' '],
    [' ', ' ', ' ', 'D', ' ', 'X', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X'],
    [' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X', 'X']
]

customer_city = [
    ['X', 'C', 'C', 'D', 'C', ' ', 'X', ' ', 'X'],
    ['X', ' ', 'X', 'X', ' ', ' ', ' ', ' ', 'X'],
    [' ', ' ', 'C', 'D', 'X', 'X', ' ', 'X', ' '],
    [' ', ' ', 'C', 'D', 'C', 'X', ' ', ' ', ' '],
    [' ', ' ', ' ', 'C', ' ', 'X', ' ', ' ', 'X'],
    [' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X', 'X']
]

locations = [
    [2, 2],
    [4, 0],
    [0, 4],
    [2, 6],
]
print(sol.getClosedMart(locations, city))
print(sol.getMostCustomerCount(locations,customer_city))
print(sol.getClosedMartMaxCustomer(locations,customer_city))