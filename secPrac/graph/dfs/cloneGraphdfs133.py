
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []



class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        visited = dict()
        def dfs(node):
            if node in visited:
                return visited[node]
            cloneNode = Node(node.val,[])
            visited[node] = cloneNode
            for neigh in node.neighbours:
                # 关键点 对于当前node 他的邻居需要被重新clone,根据他的node 的neighbour 来clone
                cloneNode.neighbours.append(dfs(neigh))

            return cloneNode
        return dfs(node)

    def cloneGraphDFS(self, node: 'Node') -> 'Node':
        if not node:
            return node
        visited = dict()

        def dfs(node):
            if node in visited:
                return visited[node]
            ## 核心逻辑， 如果不存在，就创造一个新的，放入dict之中
            clone_node = Node(node.val, [])
            visited[node] = clone_node
            # clone neighbour of node
            for neighbour in node.neighbors:
                ## 不需要这里 因为逻辑已经在之前做过了 对于dfs层
                # if neighbour not in visited:
                #     clone_neighbour = Node(neighbour.val, [])
                #     visited[neighbour] = clone_neighbour
                clone_node.neighbors.append(dfs(neighbour))

            return clone_node

        return dfs(node)


    def cloneGraphDFS(self, node: 'Node') -> 'Node':
        if not node:
            return node
        visited = dict()
        def dfs(node):
            if node in visited:
                return visited[node]
            # copy cur node
            clone_node = Node(node.val,[])
            visited[node] = clone_node
            # copy neighbour
            for neigh  in node.neighbours:
                visited[node].neighbours.append(dfs(neigh))

            return clone_node
        return dfs(node)