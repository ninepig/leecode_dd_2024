from firstRount.Tree.TreeBasic.TreeNode import TreeNode


class Solution:
    def preorderTraversalRec(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(root):
            if not root:
                return
            ans.append(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return  ans

    def preorderTraversalStack(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = [root]
        while stack:
            cur = stack.pop() # pre order--> we visit root first
            ans.append(cur.val)
            if cur.right :
                stack.append(cur.right) # right first so, left will be pop first
            if cur.left:
                stack.append(cur.left)

        return ans

    def orderTraversalRec(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            ans.append(root.val)

            dfs(root.right)

        dfs(root)
        return  ans

    def orderTraversalStack(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []
        while stack or root: ## inorder go left first
            while root:
                stack.append(root)
                root = root.left
            cur = stack.pop()
            ans.append(cur.val)
            root = cur.right # 直接给邮编就行 不需要判断

        return ans

    ## 比较难 抄答案就行了..
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        prev = None  # 保存前一个访问的节点，用于确定当前节点的右子树是否访问完毕

        while root or stack:  # 根节点或栈不为空
            while root:
                stack.append(root)  # 将当前树的根节点入栈
                root = root.left  # 继续访问左子树，找到最左侧节点

            node = stack.pop()  # 遍历到最左侧，当前节点无左子树时，将最左侧节点弹出

            # 如果当前节点无右子树或者右子树访问完毕
            if not node.right or node.right == prev:
                res.append(node.val)  # 访问该节点
                prev = node  # 记录前一节点
                root = None  # 将当前根节点标记为空
            else:
                stack.append(node)  # 右子树尚未访问完毕，将当前节点重新压回栈中
                root = node.right  # 继续访问右子树

        return res