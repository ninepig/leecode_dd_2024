
class TreeNode:
    def __init__(self,value : int = 0):
        self.val = value
        self.left = TreeNode()
        self.right = TreeNode()

class Solution:
    def maxDeep(self, root: TreeNode) -> int:

        if not root : return 0

        return max(self.maxDeep(root.right), self.maxDeep(root.left)) + 1

    def minDeep(self, root: TreeNode) -> int:

        if not root: return 0

        # 确定叶子节点
        if not root.left and not root.right:
            return 1

        # 当前节点的左右子树的最小叶子节点深度
        min_res = 0xffffff
        if root.left :
            min_res = min(min_res,self.minDeep(root.left))
        if root.right:
            min_res = min(min_res,self.minDeep(root.right))

        # 当前节点的最小叶子节点深度
        return min_res + 1