class Solution:
    ## print all path ---> backtracking problem
    ## DAG, so we dont need care about cycle problem
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path = [0]
        res = []
        self.dfs(graph,0,len(graph) - 1 , path, res)
        return res

    def dfs(self, graph, start, target, path, ans):
        if start == target:
            ans.append(path[:])
            return
        for end in graph[start]:
            path.append(end)
            self.dfs(graph, end, target, path, ans)
            path.remove(end)


   '''
   非常标准的 dfs + backtracking题 
   '''