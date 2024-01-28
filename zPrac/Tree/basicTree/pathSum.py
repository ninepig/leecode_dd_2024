class Solution:
    def __init__(self):
        self.exist = False
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        ## 这里dfs的意义就是前序遍历
        def dfs(node,sum):
            if not node:
                return
            # missing one step, need to be leaf node
            if node.left is None and node.right is None and targetSum - node.val == 0:
                self.exist = True
            if node.left :
                dfs(node.left , targetSum - node.val)
            if node.right :
                dfs(node.right, targetSum - node.val)
            return

        dfs(root,targetSum)
        return self.exist

    ## 答案显得清晰很多。。
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        return self.sum(root, targetSum, 0)

    def sum(self, root: TreeNode, targetSum: int, curSum: int) -> bool:
        if root == None:
            return False
        curSum += root.val
        if root.left == None and root.right == None:
            return curSum == targetSum
        else:
            return self.sum(root.left, targetSum, curSum) or self.sum(root.right, targetSum, curSum)

## 找出所有路径
# backtrack
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        path = []
        ans = []
        self.pathHelper(path,ans,root,targetSum)

    def pathHelper(self, path, ans, root, targetSum):
        if not root:
            return
        #backtracking process,对于当前层我们要做什么，怎么处理
        path.append(root.val)
        if root.left is None and root.right is None and root.val == targetSum:
            ans.append(path[:])
        self.pathHelper(path,ans,root.left,targetSum-root.val)
        self.pathHelper(path,ans,root.right,targetSum-root.val)
        path.pop()






