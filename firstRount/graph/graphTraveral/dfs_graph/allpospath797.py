'''
基本的travel dfs 题
给定一个有 n 个节点的有向无环图（DAG），用二维数组 graph 表示。

要求：找出所有从节点 0 到节点 n - 1 的路径并输出（不要求按特定顺序）。

二维数组 graph 的第 i 个数组 graph[i] 中的单元都表示有向图中 i 号节点所能到达的下一个节点，如果为空就是没有下一个结点了。
'''
from firstRount.LinkedList import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path = [0]
        res = []
        self.dfs(graph,res,path,0,len(graph) - 1)
        return res

    # 非常标准的回溯法
    def dfs(self,graph, res, path, start, target):
        if start == target:
            res.append(path[:])
        for end in graph[start]:
            path.append(end)
            self.dfs(graph,res,path,end,target)
            path.remove(end)