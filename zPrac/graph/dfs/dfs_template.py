class Solution:
    def dfs_recursive(self,graph,u,visited):
        print(u) # 打印当前节点
        visited.add(u) # 已经访问过了
        for v in graph[u]:
            if v not in visited:
                self.dfs_recursive(graph,v,visited)


graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D", "G"],
    "G": []
}
'''
1 邻接表的定义
2 visit 辅助数组
3 从某一个结点开始
4 根据题意 处理未被访问的点
5 加入 vistied之中
6 根据当前点的灵界节点开始访问

'''
# 基于递归实现的深度优先搜索
visited = set()
Solution().dfs_recursive(graph, "A", visited)