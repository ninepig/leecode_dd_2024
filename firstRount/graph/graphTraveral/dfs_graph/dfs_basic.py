class Solution:
    def dfs_recursive(self, graph, u, visited):
        print(u)  # 访问节点
        visited.add(u)  # 节点 u 标记其已访问

        for v in graph[u]:
            if v not in visited:  # 节点 v 未访问过
                # 深度优先搜索遍历节点
                self.dfs_recursive(graph, v, visited)


graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D", "G"],
    "G": []
}

# 基于递归实现的深度优先搜索
visited = set()
Solution().dfs_recursive(graph, "A", visited)
