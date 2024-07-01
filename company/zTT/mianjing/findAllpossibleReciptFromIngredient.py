# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/solutions/1646605/python3-topological-sort-kahn-s-algo/
## leetcode 2115
## topo + bfs 应用题
from collections import defaultdict, deque
from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indeg = defaultdict(int) ## 某个r 需要多少个indegdeint
        graph = defaultdict(list)
        for r, ing in zip(recipes, ingredients):
            indeg[r] = len(ing) ## 表示某个recreipt需要几个indegree来完成， 类似topo排序
            for i in ing:
                graph[i].append(r) ## ingredients---》receipt 的图

        ans = []
        ## supply 可以理解为 一个一个的我们查找这些ingredients， 我们查找这些ingredients 是否能满足让indegree = 0，
        ## 同时当我们完成一个元素 也要把它加入到queue之中，因为它可能是某个recpt的成分。 until queue为空
        queue = deque(supplies)
        recipes = set(recipes)
        while queue:
            item = queue.popleft()
            if item in recipes: ans.append(item)
            for receipt in graph[item]: ##recipt we can make from this item
                indeg[receipt] -= 1 ## if we can make that item(no more item needs)
                if indeg[receipt] == 0: queue.append(receipt)  ## put in to product queue
        return ans