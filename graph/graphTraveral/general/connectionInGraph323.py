'''
这道题是图里最能体验基础的题
可以用bfs dfs uf来做,包括构建图的技巧

BFS, DFS 都是先构建图 无向图
然后就是利用visited 数组 来记录访问过的节点

'''
import collections

from LinkedList import List


class UF:
    def __init__(self,n):
        self.count  = n
        self.father = [i for i in range(n)]

    def find(self,x):
        while x != self.father[x]:
            self.father[x] = self.father[self.father[x]]
            x = self.father[x]
        return x

    def union(self,x,y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_y == root_x:
            return False
        self.father[root_x] = root_y
        self.count -= 1
        return True

    def is_connect(self,x,y):
        return self.find(x) == self.find(y)

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UF(n)
        for edge in edges:
            uf.union(edge[0],edge[1])

        return uf.count

    def dfs(self,visit,node,graph):
        visit[node] = True
        for j in graph[node]:
            if not visit[j]:
                self.dfs(visit,j,graph)

    def countComponentsDFS(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        visit = [False for i in range(n)]
        graph = [[] for _ in range(n)]
        # dag 无向图
        for x , y in edges:
            graph[x].append(y)
            graph[y].append(x)

        for i in range(n):
            if not visit[i]:
                count +=1
                self.dfs(visit,i,graph)

        return count

    def countComponentsBFS(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        visited = set()
        graph = [[] for _ in range(n)]

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        for i in range(n):
            if i not in visited:
                visited.add(i)
                count += 1
                queue = collections.deque([i])
                while queue:
                    node_u = queue.popleft()
                    for node_v in graph[node_u]:
                        if node_v not in visited:
                            visited.add(node_v)
                            queue.append(node_v)
        return count