class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        size = len(graph)
        colors = [0 for _ in range(size)]

        for i in range(size):
            if colors[i] == 0 and not self.dfs(graph,colors,i,1):
                return False
        return True

    def dfs(self, graph, colors, i, color):
        colors[i] = color
        for j in graph[i]:
            if colors[j] == color[i]:
                return False #neighbor color is same as current
            ## dfs 染色下去 并且判断邻居节点
            if colors[j] == 0 and not self.dfs(graph,colors,j,-1):
                return False
        return True


