from firstRount.Tree.TreeBasic.TreeNode import TreeNode


class Solution:
    def __init__(self):
        self.balanced = True
    def isBalanced(self, root: TreeNode) -> bool:

        self.getHeight(root)

        return self.balanced

    def getHeight(self,node:TreeNode):
        if not node:
            return 0
        left_height = self.getHeight(node.left)
        right_height = self.getHeight(node.right)
        if abs(left_height - right_height) > 1:
            self.balanced = False
        return max(left_height, right_height) + 1