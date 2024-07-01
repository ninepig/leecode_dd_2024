'''
https://zhuanlan.zhihu.com/p/423471030?utm_id=0
reference


'''
class Solution:
    '''1 号题 岛屿数量 最经典
    dfs 搜索问题。
    结束条件
    1 边界到达
    2 不是小岛
    3 已经访问过了
    一般会利用一个visited dict 来保存
    但是可以利用 原来的数组 把值设为0 （淹没小岛） 来达到已经访问过的效果

    对于每个数组中的1 进行一次搜索。 已经访问过的会被置为0。
    '''
    def islandCount200(self, grid:list[list[int]])-> int:
        count = 0
        rows = len(grid)
        cols = len(grid[0])


        def dfs(row,col):
            if row < 0 or col <0 or col >= cols or row >= rows:
                return
            if grid[row][col] == 0 : return  # have vistied or not island
            grid[row][col] = 0 ## make island disappear
            dfs(row + 1, col)
            dfs(row - 1 ,col)
            dfs(row,col+1)
            dfs(row,col-1)


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    count += 1
                    dfs(i,j)

        return count

'''
这个是200的 纯纯follow up 
封闭岛屿的意思 就是连着四周的都不算封闭岛屿
必须是在中心部分。 
所以需要做预处理
也就是把连接四周的小岛都沉没 变成水域 。然后再找还存在的

这道题 1是水
'''
def closedIslandCount(self, grid:list[list[int]])->int:
    count = 0
    rows = len(grid)
    cols = len(grid[0])

    def dfs(row, col):
        if row < 0 or col < 0 or col >= cols or row >= rows:
            return
        if grid[row][col] == 1: return  # have vistied or not island
        grid[row][col] = 1  ## make island disappear
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

    for i in range(rows):
        # dont need consider if that is 0 or 1 just go
        dfs(i,0)
        dfs(i,cols - 1)

    for i in range(cols):
        dfs(0,i)
        dfs(rows-1,i)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                count += 1
                dfs(i,j)

    return count


'''
这个题是搜索返回的时候赋值
同样的搜索框架
'''
def maxIsland(self, grid:list[list[int]])->int:
    ans = 0
    rows = len(grid)
    cols = len(grid[0])
    if rows == cols == 1:
        return grid[0][0] == 1

    def dfs(row,col):
        if not(0 <= row < col and 0 <= col < cols):
            return 0
        if not grid[row][col]:
            return 0
        area = 1
        grid[row][col] = 0 #
        area += dfs(row + 1, col)
        area += dfs(row - 1, col)
        area += dfs(row, col + 1)
        area += dfs(row, col - 1)

        return area

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                ans = max(ans,dfs(i,j))

    return ans


'''
这道题其实也算是200的后续
只不过思考起来有点复杂
需要一个预处理
如果在grid1是海 grid2是陆地 相连的所有岛屿 需要先沉没
因为这个肯定不是子岛 预处理完了以后再做 
'''
def subIslandCount(self, grid:list[list[int]],grid2:list[list[int]])->int:
    count = 0
    rows = len(grid)
    cols = len(grid[0])

    def dfs(row, col):
        if row < 0 or col < 0 or col >= cols or row >= rows:
            return
        if grid2[row][col] == 0: return  # have vistied or not island
        grid2[row][col] = 0  ## make island disappear
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

    for i in range(rows):
        for j in range(cols):
            if not grid[i][j]  and grid2[i][j]: #
                dfs(i,j) # only disappear island in grid2 , that can not be subisland of grid1

    for i in  range(rows):
        for j in range(cols):
            if grid2[i][j] == 1:
                count += 1
                dfs(i,j)

    return count


'''
边长也是dfs， 逻辑是什么？
如果某个岛 有一个边是0 或者出界，他那可以提供的边长就是1
所以搜索的条件就出来了 
利用2代表访问过。 在遇到2 就直接返回0， 不返回0 '''
def islandPerimeter(self, grid:list[list[int]])-> int:
    ans = 0
    rows = len(grid)
    cols = len(grid[0])

    def dfs(row,col):
        if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
            return 1 # 边界或者水域，所以边长是1
        if grid[row][col] == 2:
            return 0 # 已经访问过了
        grid[row][col] = 2 # 设置访问过

        return dfs(row + 1, col) + dfs(row-1,col) + dfs(row,col + 1) + dfs(row,col -1 )

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                ans = max(ans,dfs(i,j))
                # break;  #如果只有一个岛的话 第一次就可以break了 ，要不然就是取最大的
    return ans



'''
形状一样 就是行走的方向一样
因为dfs的顺序是一致的 如果能组成岛 
同时顺序的sequ一样， 那么岛的形状肯定一样
'''
def sameShapeIsland(self,grid:list[list[int]])->int:
    rows = len(grid)
    direction = [(-1,0),(1,0),(0,1),(0,-1)]
    cols = len(grid[0])
    def dfs(row:int, col:int, direct:tuple,seq:list[tuple]):
        if not( 0 <= row <rows or 0 <= col < cols):
            return seq
        if grid[row][col] == 0:
            return seq
        seq.append(direct)
        for direct in direction:
            new_row = direct[0] + row
            new_col = direct[1] + col
            seq = dfs(new_row,new_col,direct,seq)
        return seq

    shape = set()
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                islandShape = dfs(i,j,(0,0),[])
                shape.add(islandShape)

    return len(shape)


## todo shape 2 好像很麻烦。。
## largest human island
# https://leetcode.cn/problems/making-a-large-island/solutions/1830996/by-ac_oier-1kmp
