class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def getCount(self,root:TreeNode):
        if not root:
            return 0
        def dfs(node):
            nonlocal count
            if not node:
                return 0
            count = 1
            if node.left:
                count += dfs(node.left)
            if node.right :
                count += dfs(node.right)
            return count

        return dfs(root)