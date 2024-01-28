class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
'''
使用一个哈希表存储所有已被访问和克隆的节点。哈希表中的 key 是原始图中的节点，value 是克隆图中的对应节点。

从给定节点开始遍历图。如果某个节点已经被访问过，则返回其克隆图中的对应节点。

如下图，我们给定无向边边 A - B，表示 A 能连接到 B，且 B 能连接到 A。如果不对访问过的节点做标记，则会陷入死循环中。



如果当前访问的节点不在哈希表中，则创建它的克隆节点并存储在哈希表中。注意：在进入递归之前，必须先创建克隆节点并保存在哈希表中。如果不保证这种顺序，可能会在递归中再次遇到同一个节点，再次遍历该节点时，陷入死循环。


递归调用每个节点的邻接点。每个节点递归调用的次数等于邻接点的数量，每一次调用返回其对应邻接点的克隆节点，最终返回这些克隆邻接点的列表，将其放入对应克隆节点的邻接表中。这样就可以克隆给定的节点和其邻接点。

作者：力扣官方题解
链接：https://leetcode.cn/problems/clone-graph/solutions/370663/ke-long-tu-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

非常非常标准的dfs 题
利用visit 来判断是否被访问过
对于当前一个点,先判断是否有visit过
没有就创建, 同时对他的neighbour进行访问
'''



class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return node

        visit = dict()

        def dfs(node:Node) ->Node:
            if node in visit:
                return node
            clone_node = Node(node.val,[])
            visit[node] = clone_node
            for neighbour in node.neighbors:
                clone_node.neighbors.append(dfs(neighbour))
            return clone_node

        return dfs(node)


    def cloneGraphP(self,node: Node) -> Node:
        visited = dict()
        def dfs(node:Node):
            if node in visited:
                return node
            # 当前dfs层处理
            cloned_node = Node(node.val,[])
            visited[node] = cloned_node
            for node_v in node:
                #很核心的一步, 对于邻居,让他dfs下去处理
                cloned_node.neighbors.append(dfs(node_v))

            return cloned_node

        return dfs(node)

