class Solution:
    def __init__(self):
        self.answer = 0
    # 对于树的dfs 就是他到叶子节点了,返回高度为0.dfs的结束条件
    def dfs(self, node):
        if not node:
            return 0
        left_height =  self.dfs(node.left)
        right_height = self.dfs(node.right)
        self.answer = max(self.answer,left_height+right_height)
        return max(left_height,right_height) + 1 # 类似最大深度

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root :
            return 0
        self.dfs(root)
        return self.answer