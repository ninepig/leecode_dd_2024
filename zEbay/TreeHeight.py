class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def getHeightOfTree(self,root:TreeNode):
        if not root:
            return 0

        left = self.getHeightOfTree(root.left)
        right = self.getHeightOfTree(root.right)

        return max(left,right) + 1

    def getMinOfTree(self,root:TreeNode):
        if not root:
            return 0
        if not root.left:
            return self.getMinOfTree(root.right) + 1
        if not root.right:
            return self.getMinOfTree(root.left) + 1

        return min(self.getMinOfTree(root.right),self.getMinOfTree(root.left)) + 1