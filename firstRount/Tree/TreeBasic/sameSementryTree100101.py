
class TreeNode:
    def __init__(self,value : int = 0):
        self.val = value
        self.left = TreeNode()
        self.right = TreeNode()

'''同一类
遍历树
dfs'''
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

    '''
    我们可以通过递归方式，
    检查其左子树与右子树外侧节点和内测节点是否相等。
    即递归检查左子树的左子节点值与右子树的右子节点值是否相等（外侧节点值是否相等），
    递归检查左子树的右子节点值与右子树的左子节点值是否相等（内测节点值是否相等）'''

    def isSemeteryTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        return  self.checkSemetery(root.left,root.right)


    def checkSemetery(self,left:TreeNode,right:TreeNode):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return  self.checkSemetery(left.left,right.right) and self.checkSemetery(left.right,right.left)