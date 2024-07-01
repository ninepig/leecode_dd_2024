import collections


class solution:
    ## starting from each dashmart , record each pos if can be reach or not, if can, we record distance
    ## check target location's distance
    ## santicy check
    '''

    这道题是个多源的bfs 不断更新最短路径。
    因为对于每个源头，每次都是1个step
    我们利用把step放在queue之中，所以不需要层序的做法
    '''
    def getClosedMart(self,locations:list[list[int]],grid:list[list[str]]) -> list[int]:
        queue = collections.deque()
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        distance_dict = dict() ## 要用dict， 这样 key 可以是tuble
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 'D':
                    queue.append((row,col,0)) ## we store x,y, distance in to queue

        while queue:
            cur_row,cur_col,cur_dis = queue.popleft()
            for dir in dirs:
                new_row = cur_row + dir[0]
                new_col = cur_col + dir[1]
                if 0 <= new_row < rows and 0 <= new_col < cols and (new_row,new_col) not in distance_dict:
                    if grid[new_row][new_col] == 'X': ## if that is a X, we can not go through, but we record
                        distance_dict[(new_row,new_col)] = cur_dis + 1
                    elif grid[new_row][new_col] == ' ':
                        queue.append((new_row,new_col,cur_dis + 1))
                        distance_dict[(new_row,new_col)] = cur_dis + 1

        res = []
        for location in locations:
            if (location[0],location[1]) in distance_dict:
                res.append(distance_dict[location[0],location[1]])

        return res


    '''
    follow up是单源的做法 每次都从一个c 出发
    '''
    def getMartWithMostCustomer(self,locations:list[list[int]],grid:list[list[str]]) -> list[int]:
        ## santity check
        store_customer_dict = collections.defaultdict(int)
        visited = set()
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 'C':
                    queue = collections.deque()
                    visited.clear()
                    queue.append((row,col))
                    visited.add((row,col))
                    found_store = False
                    while queue:
                        cur_row,cur_col = queue.popleft()
                        for dir in dirs:
                            new_row = dir[0] + cur_row
                            new_col = dir[1] + cur_col
                            if 0 <= new_row < rows and 0<= new_col < cols and (new_row,new_col) not in visited and not found_store:
                                if grid[new_row][new_col] == 'D':
                                    ## we found a store
                                    store_customer_dict[(new_row,new_col)] += 1 ##  customer + 1
                                    found_store = True
                                    break
                                elif grid[new_row][new_col] == ' ' or grid[new_row][new_col] == 'C':
                                    visited.add((new_row,new_col))
                                    queue.append((new_row,new_col))

        max_value = max(store_customer_dict.values())
        res = []
        for key in store_customer_dict.keys():
            if store_customer_dict[key] == max_value:
                res.append(key)

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
print(sol.getMartWithMostCustomer(locations,customer_city))

