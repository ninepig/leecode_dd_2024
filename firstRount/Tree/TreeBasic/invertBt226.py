from typing import Optional

from firstRount.Tree.TreeBasic.TreeNode import TreeNode


class Solution:
    '''classic 其实就是个后序题'''
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        left_tree = self.invertTree(root.left)
        right_tree = self.invertTree(root.right)
        root.left = right_tree
        root.right = left_tree

        return  root