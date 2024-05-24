import collections


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    # def cloneGraph(self, node: 'Node') -> 'Node':
    #     visited = dict()
    #     queue = collections.deque([])
    #     visited[node] = Node(node.val,[])
    #     queue.append(node)
    #     while queue:
    #         cur = queue.popleft()
    #         for node_v in cur.neighbors:
    #             if node_v not in visited:
    #                 visited[node_v] = Node(node_v.val,[])
    #                 queue.append(node_v)
    #             visited[node_v].neighbors.append(visited[node_v])
    #
    #     return visited[node_v]

    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = dict()
        queue = collections.deque([])
        visited[node] = Node(node.val,[])
        queue.append(node)
        while queue:
            cur = queue.popleft()
            for neighbour in cur.neighbours:
                if neighbour not in visited:
                    #基本的bfs逻辑
                    visited[neighbour] = Node(neighbour.val,[])
                    #没visit过 所以需要加入quque
                    queue.append(neighbour)
                #复制 neighbour节点 每一层的逻辑
                visited[neighbour].neighbors.append(visited[neighbour])

        return visited[node]

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        visited = dict()

        def dfs(node: 'Node') -> 'Node':
            if node in visited:
                return visited[node]

            clone_node = Node(node.val, [])
            visited[node] = clone_node
            for neighbor in node.neighbors:
                clone_node.neighbors.append(dfs(neighbor))
            return clone_node

        return dfs(node)