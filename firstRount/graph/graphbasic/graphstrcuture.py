class Graph:  # 基本图类，采用邻接矩阵表示
    # 图的初始化操作，ver_count 为顶点个数
    def __init__(self, ver_count):
        self.ver_count = ver_count  # 顶点个数
        self.adj_matrix = [[None for _ in range(ver_count)] for _ in range(ver_count)]  # 邻接矩阵

    # 判断顶点 v 是否有效
    def __valid(self, v):
        return 0 <= v <= self.ver_count

    # 图的创建操作，edges 为边信息
    def creatGraph(self, edges=[]):
        for vi, vj, val in edges:
            self.add_edge(vi, vj, val)

    # 向图的邻接矩阵中添加边：vi - vj，权值为 val
    def add_edge(self, vi, vj, val):
        if not self.__valid(vi) or not self.__valid(vj):
            raise ValueError(str(vi) + ' or ' + str(vj) + " is not a valid vertex.")

        self.adj_matrix[vi][vj] = val

    # 获取 vi - vj 边的权值
    def get_edge(self, vi, vj):
        if not self.__valid(vi) or not self.__valid(vj):
            raise ValueError(str(vi) + ' or ' + str(vj) + " is not a valid vertex.")

        return self.adj_matrix[vi][vj]

    # 根据邻接矩阵打印图的边
    def printGraph(self):
        for vi in range(self.ver_count):
            for vj in range(self.ver_count):
                val = self.get_edge(vi, vj)
                if val:
                    print(str(vi) + ' - ' + str(vj) + ' : ' + str(val))


graph = Graph(5)
edges = [[1, 2, 5], [2, 1, 5], [1, 3, 30], [3, 1, 30], [2, 3, 14], [3, 2, 14], [2, 4, 26], [4, 2, 26]]
graph.creatGraph(edges)
print(graph.get_edge(3, 4))
graph.printGraph()


class VertexNode:  # 顶点信息类
    def __init__(self, vi):
        self.vi = vi  # 顶点
        self.adj_edges = dict()  # 顶点的邻接边


class Graph:
    def __init__(self):
        self.vertices = dict()  # 顶点

    # 图的创建操作，edges 为边信息
    def creatGraph(self, edges=[]):
        for vi, vj, val in edges:
            self.add_edge(vi, vj, val)

    # 向图中添加节点
    def add_vertex(self, vi):
        vertex = VertexNode(vi)
        self.vertices[vi] = vertex

    # 向图的邻接表中添加边：vi - vj，权值为 val
    def add_edge(self, vi, vj, val):
        if vi not in self.vertices:
            self.add_vertex(vi)
        if vj not in self.vertices:
            self.add_vertex(vj)

        self.vertices[vi].adj_edges[vj] = val

    # 获取 vi - vj 边的权值
    def get_edge(self, vi, vj):
        if vi in self.vertices and vj in self.vertices[vi].adj_edges:
            return self.vertices[vi].adj_edges[vj]
        return None

    # 根据邻接表打印图的边
    def printGraph(self):
        for vi in self.vertices:
            for vj in self.vertices[vi].adj_edges:
                print(str(vi) + ' - ' + str(vj) + ' : ' + str(self.vertices[vi].adj_edges[vj]))


graph = Graph()
edges = [[1, 2, 5], [1, 5, 6], [2, 4, 7], [4, 3, 9], [3, 1, 2], [5, 6, 8], [6, 4, 3]]
graph.creatGraph(edges)
print(graph.get_edge(3, 4))
graph.printGraph()