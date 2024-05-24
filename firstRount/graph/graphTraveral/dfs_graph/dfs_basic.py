class Solution:
    def dfs_graph(self,graph,visited,u):
        print(u) # visit current vertics
        visited.add(u) # flag
        for v in graph[u]: # 题中都是邻接表的实现
            if v not in visited:
                self.dfs_graph(self,graph,visited,v)

