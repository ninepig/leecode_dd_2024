# Definition for a binary tree node.
##https://leetcode.cn/problems/most-frequent-subtree-sum/solutions/1610634/pythonjavatypescriptgo-di-gui-by-himymbe-9tds
from collections import defaultdict
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
子树sum 一般都是后序来做
配合dict来做

'''
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        tree_sum = defaultdict(int)
        max_count = 0
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            cur_val = left + right + root.val
            tree_sum[cur_val] += 1 # 这里可以写成 tree_sum[cur_val := left + right + root.val]
            nonlocal max_count
            max_count = max(max_count, tree_sum[cur_val])
            return cur_val
        dfs(root)
        ans = []
        for i,v in tree_sum.items():
            if v == max_count:
                ans.append(i)
        return ans