from typing import List
import collections
import math


## https://leetcode.com/problems/count-nodes-with-the-highest-score/solutions/1537511/python3-post-order-dfs
class Solution:
    ## o(n) travel the tree
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        parent_children_graph = collections.defaultdict(list)
        ## You are given a 0-indexed integer array parents representing the tree,
        # where parents[i] is the parent of node i. Since node 0 is the root, parents[0] == -1
        for k,v in enumerate(parents):
            ## value 是父亲节点 k 是index
            parent_children_graph[v].append(k) ## build parent to child's index graph

        freq = collections.defaultdict(int)
        size = len(parents)
        '''
        # Idea is when we visit a node, we split it into, three parts,
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
