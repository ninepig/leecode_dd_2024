from typing import List


class Solution:
    ## print all path ---> backtracking problem
    ## DAG, so we dont need care about cycle problem，so we dont need add visited or not array
    # def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    #     res = []
    #     # 在开始的时候加入 root点， 避免dfs之中错过
    #     path = [0]
    #     self.dfs(graph,0,len(graph) - 1 , path, res)
    #     return res

    # def dfs(self, graph, start, target, path, ans):
    #     if start == target:
    #         ans.append(path[:])
    #         return
    #
    #     for end in graph[start]:
    #         path.append(end)
    #         self.dfs(graph, end, target, path, ans)
    #         path.remove(end)

   '''
   非常标准的 dfs + backtracking题 
   '''
    def allPathsSourceTarget2(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph:
            return []
        res = []
        path = [0] # starting from 0
        self.dfs2(graph,res,path,0,len(graph) - 1)
        return res

    def dfs2(self, graph, res, path, cur, target):

        if cur == target:
            res.append(path[:])

        for neigh in graph[cur]:
            path.append(neigh)
            self.dfs2(graph,res,path,neigh,target)
            path.remove(neigh)
        return