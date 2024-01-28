##
# does not has weight, directly graph
class node:
    def __init__(self,vi):
        self.vi = vi # self vertics
        self.edges = [] ## point to vertics

class graphWithoutWeight:
    def __init__(self):
        self.nodes = dict() # id : node dict

    ## create graph , edges as input
    ## assume edge looks like 2 element tuble (vi,vj)
    def createGraph(self,edges = []):
        for vi,vj in edges:
            self.add_edges(vi,vj)

    def add_edges(self, vi, vj):
        if vi not in self.nodes:
            self.add_node(vi)
        if vj not in self.nodes:
            self.add_node(vj)
        # append edge from vi
        self.nodes[vi].edges.append(vj)

    def add_node(self, vi):
        cur = node(vi)
        # id is key, node is value
        self.nodes[vi] = cur



class NodeW:
    def __init__(self,vi):
        self.id = vi
        # edge node and his weight
        self.neighbours = dict()

class GraphWithWeight:
    def __init__(self):
        self.nodes = dict()

    def createGraph(self,edges = []):
        for vi, vj , weight in edges:
            self.add_edges(vi,vj,weight)

    def add_edges(self, vi, vj, weight):
        if vi not in self.nodes:
            self.add_node(vi)
        if vj not in self.nodes:
            self.add_node(vj)
        # neighbour dict
        self.nodes[vi].neighbours[vj] = weight

    def add_node(self, vi):
        cur = NodeW(vi)
        self.nodes[vi] = cur

    # 寻找某边的权重
    def get_edge(self,vi,vj):
        if vi in self.nodes and vj in self.nodes:
            return self.nodes[vi].neighbours[vj]
        return None

