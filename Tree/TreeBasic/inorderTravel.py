class TreeNode:
    def __init__(self,value : int = 0):
        self.val = value
        self.left = TreeNode()
        self.right = TreeNode()


class solution:

    def inOrderTravel(self, root : TreeNode)-> list[int]:
        res = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)

        dfs(root)
        return res

    def inOrderTravelStack(self, root : TreeNode)-> list[int]:
        if not root:
            return []
        res = []
        stack = []

        while root or stack:  # 根节点或栈不为空
            while root:
                stack.append(root)  # 将当前树的根节点入栈
                root = root.left  # 找到最左侧节点

            node = stack.pop()  # 遍历到最左侧，当前节点无左子树时，将最左侧节点弹出
            res.append(node.val)  # 访问该节点
            root = node.right  # 尝试访问该节点的右子树

        return res