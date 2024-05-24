'''
最小生成树
包含所有顶点：生成树中包含了原图的所有顶点。
连通性：生成树是原图的一个连通子图，意味着任意两个顶点之间都存在一条路径。
无环图：生成树一个无环图。
边数最少：在包含所有顶点的情况下，生成树的边数最少，其边数为顶点数减

3.2 Kruskal 算法的实现步骤
将图中所有边按照权重从小到大进行排序。
将每个顶点看做是一个单独集合，即初始时每个顶点自成一个集合。
按照排好序的边顺序，按照权重从小到大，依次遍历每一条边。
对于每条边，检查其连接的两个顶点所属的集合：
如果两个顶点属于同一个集合，则跳过这条边，以免形成环路。
如果两个顶点不属于同一个集合，则将这条边加入到最小生成树中，同时合并这两个顶点所属的集合。
重复第
 步，直到最小生成树中的变数等于所有节点数减
 为止。
'''

class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.count = n

    def find(self,x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self,x,y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_y == root_x:
            return False
        self.parent[x] = y
        self.count -= 1
        return True

    def is_union(self,x,y):
        return self.find(x) == self.find(y)

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # from matric to edge lists
        edges = []
        length = len(heights)
        width = len(heights[0])
        size = length * width

        for row in range(length):
            for col in range(width):
                ## 从n 到n下方节点的edge
                if row < length - 1 :
                    x = row * length + col
                    y = (row + +1 )*length + col
                    h = abs(heights[row][col] - heights[row + 1][col])
                    edges.append((x,y,h))
                ## 从n 到n 右侧节点的edge
                if col < width - 1 :
                    x = row * length + col
                    y = row * length + col + 1
                    h = abs(heights[row][col] - heights[row][col+1])
                    edges.append((x,y,h))

        edges.sort(key = lambda x:x[2])
        uf = UF(size)

        for edge in edges:
            x,y,h = edge[0],edge[1],edge[1]
            uf.union(x,y)
            if uf.is_union(0,size - 1):
                return h

        return 0