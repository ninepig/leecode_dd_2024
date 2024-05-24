
class TreeNode:
    def __init__(self,value : int = 0):
        self.val = value
        self.left = TreeNode()
        self.right = TreeNode()

'''自己写的好蠢'''
class Solution:
    def __init__(self):
        self.exit = False

    def pathSum(self, root: TreeNode,targetSum: int) -> bool:
        self.dfs(root,targetSum)
        return self.exit

    def dfs(self,node: TreeNode,targetSum: int):
        if not node:
            return 0
        if not node.left and node.right:
            if targetSum == node.val:
                self.exit = True
        if node.left :
            self.dfs(node.left,targetSum - node.val)
        if node.right:
            self.dfs(node.right, targetSum - node.val)


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        return self.sum(root, targetSum, 0)

    def sum(self, root: TreeNode, targetSum: int, curSum:int) -> bool:
        if root == None:
            return False
        # 标准的前序, 先把当前节点做了. 判断. 然后左右
        curSum += root.val
        if root.left == None and root.right == None:
            return curSum == targetSum
        else:
            return self.sum(root.left, targetSum, curSum) or self.sum(root.right, targetSum, curSum)

    # 回溯法, 内建dfs
    # 太优雅了这个写法
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(node,targetSum):
            if not node:
                return
            path.append(node.val)
            targetSum -= node.val
            if not node.left and not node.right and targetSum == 0:
                res.append(path[:])
            dfs(node.left,targetSum)
            dfs(node.right,targetSum)
            path.pop()

        dfs(root,targetSum)
        return res