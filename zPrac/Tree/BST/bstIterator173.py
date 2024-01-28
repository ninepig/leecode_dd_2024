class BSTIterator:
    '''
    表示一个按中序遍历二叉搜索树
    注意，指针初始化为一个不存在于 BST 中的数字，所以对 next() 的首次调用将返回 BST 中的最小元素。
    '''
    def __init__(self, root: Optional[TreeNode]):
        self.nodeArray = []
        self.dfs(root)
        self.index = 0

    def next(self) -> int:
        ans = self.nodeArray[self.index]
        self.index += 1
        return ans

    def hasNext(self) -> bool:
        return self.index == len(self.nodeArray)

    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        self.nodeArray.append(root.val)
        self.dfs(root.right)

##下面的答案是基于stack的 更简单一点
 def __init__(self, root: TreeNode):
        self.stack = []
        self.in_order(root)

    def in_order(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        if node.right:
            self.in_order(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) != 0