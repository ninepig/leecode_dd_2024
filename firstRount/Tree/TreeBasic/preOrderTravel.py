class TreeNode:
    def __init__(self,value : int = 0):
        self.val = value
        self.left = TreeNode()
        self.right = TreeNode()


class solution:

    def preOrderTravel(self, root : TreeNode)-> list[int]:
        res = []

        def dfs(root):
            if not root:
                return
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return res

    def preOrderTravelStack(self, root : TreeNode)-> list[int]:
        if not root:
            return []
        res = []
        stack = [root]
        # 利用stack的特性，所以要先push 右侧， 再左侧
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res