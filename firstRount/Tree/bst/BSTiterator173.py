class BSTIterator:
    '''
    stack的方法
    其实数组的方法也挺好
    复杂度不一样
    '''
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
        return len(self.stack)!=0