class Solution:
    '''简单 自己的复杂'''
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root or val == root.val:
            return root
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

    def __init__(self):
        self.target = None

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.dfs(root, val)

        return self.target

    def dfs(self, node: TreeNode, val: int):
        if not node:
            return
        if node.val == val:
            self.target = node
            return
        if node.val < val:
            self.dfs(node.right, val)
        if node.val > val:
            self.dfs(node.left, val)
