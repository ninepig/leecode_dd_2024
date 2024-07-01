class unionfind:
    def __init__(self, size):
        self.fa = [i for i in range(size)]
        self.size = [1 for _ in range(size)]

    def find(self, x):
        if self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        self.fa[x_root] = y_root
        self.size[y_root] += self.size[x_root]


class solution:
    def largestIsland(self, grid):
        ## santity check
        if not grid or len(grid) == 0:
            raise Exception("Wrong input")
        rows = len(grid)
        cols = len(grid[0])
        uf = unionfind(rows * cols + 1)
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    for d in dirs:
                        new_row = i + d[0]
                        new_col = i + d[1]
                        if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1:
                            uf.union(i * rows + j, new_row * rows + new_col)  ## union island

        ## we already union all island
        ## if point is 0 , try to flip and to see if we can update largest

        largest = max(uf.size)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    continue
                count = set()
                for dx, dy in dirs:
                    new_row = i + dx
                    new_col = j + dy
                    if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1:
                        count.add(uf.find(new_row * rows + new_col))
                largest = max(largest, sum(uf.size[z] for z in count) + 1)

        return largest

    def getMakringIslandHashMap(self, grid):
        if not grid or len(grid) == 0:
            raise Exception("Wrong input")
        rows = len(grid)
        cols = len(grid[0])
        idx = 2  ## starting idx is 2
        idx_size_dict = dict()
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        ## get size of orignal grid and coloring grid with island idx
        def getSize(row, col, idx):
            if grid[row][col] == 0:
                return 0  ## water
            elif grid[row][col] != 1:  # vistied
                return 0
            grid[row][col] = idx
            size = 1
            for dx, dy in dirs:
                x = row + dx
                y = col + dy
                if 0 <= x < rows and 0 <= y < cols:
                    size += getSize(x, y, idx)

            return size

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    ## idx missed
                    size = getSize(i, j, idx)
                    idx_size_dict[idx] = size
                    idx += 1

        # flip 0 to 1
        max_size = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 0:
                    max_size = max(max_size, idx_size_dict[grid[i][j]])
                elif grid[i][j] == 0:
                    curSize = 1
                    neigh_dict = dict()
                    for dx, dy in dirs:
                        x = i + dx
                        y = j + dy
                        if 0 <= x < rows and 0 <= y < cols:
                            neigh_idx = grid[x][y]
                            neigh_area = 0
                            if neigh_idx in idx_size_dict:
                                neigh_area = idx_size_dict[neigh_idx]

                            if neigh_idx not in neigh_dict:
                                neigh_dict[neigh_idx] = neigh_area
                    ## bug 1  () missed
                    curSize += sum(neigh_dict.values())
                    max_size = max(max_size, curSize)

        return max_size


input = [[1, 0], [0, 1]]
sol = solution()
print(sol.largestIsland(input))
