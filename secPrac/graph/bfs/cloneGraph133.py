import collections
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        visited = dict()
        queue = collections.Deque([])

        clone_node = Node(node.val,[])

        queue.append(node)
        visited[node] = clone_node
        while queue:
            node_u = queue.popleft()
            for neighbour in node_u.neighbours:
                if neighbour not in visited:
                    visited[neighbour] = Node(neighbour.val,[])
                    queue.append(neighbour)
                # clone的node的neighbour 拿出来， 加上新clone的neighbour
                visited[node_u].neighbors.append(visited[neighbour])

        return clone_node

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        visited = dict()
        queue = collections.deque([])
        clone_node = Node(node.val,[])
        queue.append(node)
        visited[node] = clone_node

        while queue:
            cur_node = queue.popleft()
            for neighbour in cur_node.neighbours:
                if neighbour not in visited:
                    visited[neighbour] = Node(neighbour.val,[])# 不存在就 复制邻居 ,并且加入queue
                    queue.append(neighbour)
                visited[cur_node].neighbors.append(visited[neighbour]) #给当前点的邻居复制

        return visited[node]

