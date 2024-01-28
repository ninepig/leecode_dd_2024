class Solution:
    '''比数组的方法优雅很多'''
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(root, min, max):
            if root == None:
                return True
            if root.val > max or root.val < min:
                return False
            return  dfs(root.left , min, root.val) and dfs(root.right, root.val, max)

        return  dfs(root,float('-inf'),float('inf'))



    def isValidBst(self, root: TreeNode) -> bool:
        def dfs(root, min , max):
            if not root :
                return True
            if root.val > max or root.val < min:
                return False
            return dfs(root.left, min, root.val) or dfs(root.right, root.val,max)

        return dfs(root,float("-inf"),float("inf"))