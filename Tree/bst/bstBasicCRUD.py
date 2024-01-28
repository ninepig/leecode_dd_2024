class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        if root.val == val:
            return root
        if root.val < val:
            return self.searchBST(root.right,val)
        elif root.val > val:
            return self.searchBST(root.left,val)

    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        return root

    def buildBST(self, nums) -> TreeNode:
        root = TreeNode(val)
        for num in nums:
            self.insertIntoBST(root, num)
        return root
    '''
    在二叉搜索树中删除元素，首先要找到待删除节点，然后执行删除操作。根据待删除节点所在位置的不同，可以分为 
 种情况：

被删除节点的左子树为空。则令其右子树代替被删除节点的位置。
被删除节点的右子树为空。则令其左子树代替被删除节点的位置。
被删除节点的左右子树均不为空，则根据二叉搜索树的中序遍历有序性，删除该节点时，可以使用其直接前驱（或直接后继）代替被删除节点的位置。
直接前驱：在中序遍历中，节点 p 的直接前驱为其左子树的最右侧的叶子节点。
直接后继：在中序遍历中，节点 p 的直接后继为其右子树的最左侧的叶子节点。
二叉搜索树的删除算法步骤如下：

如果当前节点为空，则返回当前节点。
如果当前节点值大于 val，则递归去左子树中搜索并删除，此时 root.left 也要跟着递归更新。
如果当前节点值小于 val，则递归去右子树中搜索并删除，此时 root.right 也要跟着递归更新。
如果当前节点值等于 val，则该节点就是待删除节点。
如果当前节点的左子树为空，则删除该节点之后，则右子树代替当前节点位置，返回右子树。
如果当前节点的右子树为空，则删除该节点之后，则左子树代替当前节点位置，返回左子树。
如果当前节点的左右子树都有，则将左子树转移到右子树最左侧的叶子节点位置上，然后右子树代替当前节点位置。
    '''

    def deleteBst(self, root:TreeNode, val):
        if not root:
            return None
        if root.val > val:
            root.left = self.deleteBst(root.left,val)
            return root
        elif root.val < val:
            root.right = self.deleteBst(root.right,val)
            return root
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                cur = root.right
                while cur.left:
                    cur = cur.left
                # 删除 target,把他的左侧给新的结点
                cur.left = root.left
                return root.right # 新的root节点(删除了老的,成为新的当前节点)
