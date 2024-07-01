'''
1 并查集
--》 遍历grid， 把岛合并在一起， 然后记录下size
--》 第二遍grid --》 如果grid xx = 1 不需要做任何事情， 因为无法改成岛
---》对于 海水， 计算四周岛屿size ， 全部累加， 计算最大
uf 的方法
https://leetcode.cn/problems/making-a-large-island/solutions/1830996/by-ac_oier-1kmp

'''
from typing import List


class UnionFind:
    def __init__(self,n):
        # init forest
        self.fa = [i for i in range(n)]
        ## 增加了这个就能算出 uf之中count数
        # self.count = n
        self.size = [1 for _ in range(n)] # need a size map

    def find(self,x):
        while self.fa[x] != x:
            ## path compression, point to fa'fa in one loop, to reduce tree height
            self.fa[x] = self.fa[self.fa[x]]
            x = self.fa[x]
        return x

    def union(self,x,y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_y == root_x:
            return False # they belong same union
        if self.size[x] < self.size[y]:
            self.union(y,x)
        # connect
        self.fa[root_x] = root_y
        self.size[x] += self.size[y]
        # self.count -= 1
        return True

    # def is_connect(self,x,y):
        # return self.find(x) == self.find(y)



class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        ans = 0
        uf = UnionFind(rows * cols + 10)
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0 :
                    continue
                for dir in dirs:
                    new_i = i + dir[0]
                    new_j = j + dir[1]
                    if 0 <= new_i < rows and 0 <= new_j < cols and grid[new_i][new_j] == 1:
                        ## uf to get all island connect and count the size
                        uf.union(i*rows + j + 1, new_i * rows + new_j + 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1: ## dont need to flip
                    ans = max(ans, uf.size[uf.find(i*rows +j + 1)]) # uf 找到这个点的在uf之中cluster的面积
                if grid[i][j] == 0:
                    cur = 1
                    visited = set()
                    for dir in dirs:
                        new_i = i + dir[0]
                        new_j = j + dir[1]
                        if 0 <= new_i < rows and 0 <= new_j < cols and grid[new_i][new_j] == 1:
                            root = uf.find(new_i * rows + new_j + 1)
                            if root in visited:
                                continue
                            cur += uf.size[root]
                            visited.add(root)
                    ans = max(ans,cur)

        return ans


'''
dfs 版本
1 同样 先计算每个小岛的面积 （dfs） ， 记录
2 对于 海水区域， 计算四周小岛的面积
3 计算最大面积
这个做法太复杂了 要写得简化一点
## 计算四周的面积， 中间利用到最早的那个dict， 得到 idx: size， 看看四周是不是属于1个岛 自己写下 

https://leetcode.cn/problems/making-a-large-island/solutions/790816/827zui-da-ren-gong-dao-python3-shi-yong-wwkd5
'''
class Solution2:
    def largestIsland(self, grid: List[List[int]]) -> int:
        ## First, compute the area size of each island
        m, n = len(grid), len(grid[0])
        idxIsland = 2  # Index the Islands from 2
        markIsland = dict()

        def inArea(i, j):
            return 0 <= i < m and 0 <= j < n

        def areaSize(idxIsland, i, j):
            if not inArea(i, j):
                return 0
            if grid[i][j] != 1:
                return 0
            grid[i][j] = idxIsland
            return 1 + areaSize(idxIsland, i - 1, j) + areaSize(idxIsland, i + 1, j) + areaSize(idxIsland, i,
                                                                                                j - 1) + areaSize(
                idxIsland, i, j + 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    size = areaSize(idxIsland, i, j)
                    markIsland[idxIsland] = size
                    idxIsland += 1

        if len(markIsland) == 0:
            return 1

        if max(markIsland.values()) == m * n:
            return m * n

        ## Second, check each sea pixel and its neighbor islands' size
        def area_idx(i, j):
            if inArea(i, j):
                idx = grid[i][j]
                if idx == 0:
                    return 0, 0
                size = markIsland[idx]
                return idx, size
            return 0, 0

        # compute the total size of neihgbor Islands

        def neighbor_areas(i, j):
            areas_dict = dict()
            moves = {(0, 1), (0, -1), (-1, 0), (1, 0)}
            for move in moves:
                r = i + move[0]
                c = j + move[1]
                idx, size = area_idx(r, c)
                # save the area size of the neighbor islands
                if idx not in areas_dict:
                    areas_dict.update({idx: size})
            return sum(areas_dict.values())

        # compute the max area size with the extra sea connection
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    size = 1 + neighbor_areas(i, j)
                    res = max(res, size)
        return res



    def largestIslandWenjing(self, grid: List[List[int]]) -> int:
        ## cal all island area and store it
        rows = len(grid)
        cols = len(grid[0])
        idx_area_map = dict()
        idx = 2 ## starting index, we will use this as flag for visited or not, 1 means island, 0 means water
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        def getArea(row,col,idx):
            if not( 0<= row < rows or 0 <= col < cols):
                return 0
            if grid[row][col] != 1 : # not island
                return 0
            grid[row][col] = idx # dfs过程之中染色 外加计算面积
            cur_area = 1
            for dir in dirs:
                new_x = dir[0] + row
                new_y = dir[1] + col
                cur_area += getArea(new_x,new_y,idx)
            return cur_area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = getArea(i,j,idx)
                    idx_area_map[idx] = area
                    idx += 1

        # after we have all island area size, we try to flip

        if max(idx_area_map) == 0:
            return 1 # no island
        if max(idx_area_map) == rows * cols:
            return rows * cols ## only 1 island, no need to go further

        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    ans = max(ans,idx_area_map[grid[i][j]]) #
                else:
                    ## cal 4 surruranding island
                    cur = 1
                    neighbourisland_dict = dict()
                    for dir in dirs:
                        new_x = dir[0] + i
                        new_y = dir[1] + j
                        if 0 <= new_x < rows and 0 <= new_y < cols:
                            new_idx = grid[new_x][new_y]
                            neighbour_area = 0
                            if new_idx in idx_area_map:
                                neighbour_area = idx_area_map[new_idx]
                            if new_idx not in neighbourisland_dict:
                                neighbourisland_dict[new_idx] = neighbour_area
                    cur += sum(neighbourisland_dict.values())
                    ans = max(ans,cur)

        return ans