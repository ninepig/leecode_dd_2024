class Solution:
    '''经典 sametree + dfs题'''
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        return self.isSameTree(root,subRoot) or self.isSubtree(root.left,root) or self.isSubtree(root.right,root)


    def isSameTree(self,rootA,rootB):
        if not rootA and not rootB:
            return True
        if not rootA :
            return False
        if not rootB:
            return False
        if rootA.val != rootB.val:
            return False

        return self.isSameTree(rootA.left,rootB.left) and self.isSameTree(rootA.right,rootB.right)
