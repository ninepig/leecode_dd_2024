from typing import Optional

from firstRount.Tree.TreeBasic.TreeNode import TreeNode

'''
dfs
For each node during pre-order traversal of s, 
use a recursive function isSame to validate if sub-tree started with this node is the same with t
'''
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if self.isSameTree(root,subRoot):
            return True
        # 递归下去看看有没有任何一边等于subroot
        return self.isSameTree(root.left,subRoot) or self.isSameTree(root.right,subRoot)

    def isSameTree(self,left: Optional[TreeNode], right: Optional[TreeNode])->bool:
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return self.isSameTree(left.left,right.left) and self.isSameTree(left.right,right.right)