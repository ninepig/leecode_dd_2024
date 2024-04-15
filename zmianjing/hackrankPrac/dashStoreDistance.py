import collections


class Solution:
    def getClosedStore(self, grid, locations):
        ## santity check
        if not grid or len(grid) == 0:
            return []
        if not locations or len(locations) == 0:
            return []

        '''
        we starting from each D , record all pos with closed distance to a dashStore
        '''
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = collections.deque()
        ## need a dict to works as vistied and store distance
        point_store_dict = dict()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'D':
                    ## we put (row,col,distance) tuble in queue
                    q.append((i, j, 0))
                    point_store_dict[(i, j)] = 0

        while q:
            cur_row, cur_col, cur_dis = q.popleft()
            for d in dirs:
                new_row = cur_row + d[0]
                new_col = cur_col + d[1]
                if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in point_store_dict:
                    if grid[new_row][new_col] == ' ':  ## SPACE MEANS ROAD
                        q.append((new_row, new_col, cur_dis + 1))
                        point_store_dict[(new_row, new_col)] = cur_dis + 1
                    elif grid[new_row][new_col] == 'X':  ## IF x means we can not pass , but we need record pos
                        point_store_dict[(new_row, new_col)] = cur_dis + 1
        res = []
        for item in locations:
            if (item[0], item[1]) not in point_store_dict:
                res.append(-1)
            else:
                res.append(point_store_dict[(item[0], item[1])])

        return res

        ## bug ,注意输入！！ 输入是带C的那个grid

    def getMostCustomerStore(self, grid):
        ## santity check
        if not grid or len(grid) == 0:
            return []
        if not locations or len(locations) == 0:
            return []

        '''
        we starting from each c, once reach a store, store has a map to record how many customer it has
        '''
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = collections.deque()
        store_customer_dict = dict()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'C':
                    q.clear()
                    vistied = set()
                    q.append((i, j))
                    vistied.add((i, j))
                    found_store = False
                    while q:
                        cur_row, cur_col = q.popleft()
                        for d in dirs:
                            new_row = cur_row + d[0]
                            new_col = cur_col + d[1]
                            if (0 <= new_row < rows and 0 <= new_col < cols and (
                                    new_row, new_col) not in vistied and not found_store):
                                if grid[new_row][new_col] == 'D':  # we found a store
                                    found_store = True
                                    vistied.add((new_row, new_col))
                                    if (new_row, new_col) not in store_customer_dict:
                                        store_customer_dict[(new_row, new_col)] = 1
                                    else:
                                        store_customer_dict[(new_row, new_col)] += 1
                                if grid[new_row][new_col] == 'C' or grid[new_row][
                                    new_col] == ' ':  # can pass or a customer
                                    vistied.add((new_row, new_col))
                                    q.append((new_row, new_col))

        # print(store_customer_dict.values())
        max_value = max(store_customer_dict.values())
        res = []
        for k, v in store_customer_dict.items():
            if v == max_value:
                res.append(k)

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

sol = Solution()
# print(sol.getClosedStore(city,locations))
print(sol.getMostCustomerStore(customer_city))
