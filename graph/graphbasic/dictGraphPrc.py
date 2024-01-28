class VertexNode:
    def __init__(self,vi):
        self.edges = dict() # edges
        self.vi = vi # self node

class Graph:
    def __init__(self):
        self.vertices = dict() # vertical dict

    def creatGraph(self, edges = []):
        for vi, vj , val in edges:
            self.add_edge(vi,vj,val)

    def add_vertex(self,vi):
        vertex = VertexNode(vi)
        self.vertices[vi] = vertex

    def add_edge(self,vi,vj,val):
        if vi not in self.vertices:
            self.add_vertex(self,vi)
        if vj not in self.vertices:
            self.add_vertex(self,vj)

        self.vertices[vi].edges[vj] = val

    def get_edge(self,vi,vj):
        if vi in self.vertices and vj in self.vertices[vi].edges:
            return self.vertices[vi].edges[vj]
        return None

