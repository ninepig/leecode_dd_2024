class Solution:
    '''经典dfs,把所有path相加, 但是对于当前层要根据上一层进行 *10 + root.val的操作,所以需要一个pre_sum'''
    def dfs(self, root, pre_total):
        if not root:
            return 0
        total = pre_total * 10 + root.val
        if not root.left and not root.right:
            return total
        return self.dfs(root.left, total) + self.dfs(root.right, total)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)