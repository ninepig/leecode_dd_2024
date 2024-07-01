import collections
import math


## https://leetcode.com/problems/count-nodes-with-the-highest-score/solutions/1537511/python3-post-order-dfs
class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        parent_children_graph = collections.defaultdict(list)
        ## You are given a 0-indexed integer array parents representing the tree,
        # where parents[i] is the parent of node i. Since node 0 is the root, parents[0] == -1
        for k,v in enumerate(parents):
            parent_children_graph[v].append(k) ## build parent to child's index graph

        freq = collections.defaultdict(int)
        size = len(parents)

        '''
        后续的dfs ，对于树的dfs 无外乎前中后 ， bfs是层
        # Idea is when we remove a node, we split it into, three parts,
        # 1. The left subtree(left) 
        # 2. The right subtree (right) 
        # 3. All other nodes connected to it's parent (up)
        '''
        def dfs(node):
            left, right = 0
            if parent_children_graph[node]:## count left sub tree, it is binary tree , so we can idx can be 0 or 1
                left = dfs(parent_children_graph[node][0])

            if len(parent_children_graph[node]) > 1:# count right sub tree
                right = dfs(parent_children_graph[node][1])

            up = size - left - right - 1 # count nodes connect to parent

            score = (left or 1) * (right or 1) *(up or 1)
            freq[score] += 1

            return 1 + left + right

        dfs(0)
        ## 最大的freq 出现的个数
        return freq[max(freq)]

    def countHighestScoreNodesPrac(self, parents: List[int]) -> int:
        if not parents or len(parents) == 0: return 0
        size = len(parents)
        parent_node_graph = collections.defaultdict(list)
        for k,v in enumerate(parents):
            parent_node_graph[v].append(k)

        fre_map = collections.defaultdict(int)
        max_fre = -math.inf
        def dfs(node):
            nonlocal  max_fre
            left,right = 0,0
            if parent_node_graph[node]: ## exist subtree
                left = dfs(parent_node_graph[node][0]) ## check left tree's size
            if len(parent_node_graph[node]) > 1 : ## exist right subtree
                right = dfs(parent_node_graph[node][1])

            up = size - left - right - 1 #size is fixed, get 'up' value
            value =  (left or 1) * (right or 1) * (up or 1)
            fre_map[value] += 1
            max_fre = max(max_fre,value)

            return 1 + left + right ## post order , return value of subtree size

        dfs(0)
        return fre_map[max_fre]
