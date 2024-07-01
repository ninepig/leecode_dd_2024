class Solution:
    def __init__(self):
        self.boolean = True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        self.dfs(root)

        return self.boolean

    def dfs(self, root):
        if not root:
            return

        if root.left and root.left.val > root.val:
            self.boolean = False

        if root.right and root.right.val < root.val:
            self.boolean = False

        self.dfs(root.left)
        self.dfs(root.right)

    ##答案, 不需要global value , 更简单.把 效率更好,本质一样 都是preorder
    def isValidBSTAns(self, root: TreeNode) -> bool:
        def preorderTraversal(root, min_v, max_v):
            if root == None:
                return True
            if root.val >= max_v or root.val <= min_v:
                return False
            return preorderTraversal(root.left, min_v, root.val) and preorderTraversal(root.right, root.val, max_v)

        return preorderTraversal(root, float('-inf'), float('inf'))
