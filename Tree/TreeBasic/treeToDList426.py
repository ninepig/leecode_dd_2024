'''
很好的题目,
中序 转换 双向循环链表
'''
class Node:
    def __init__(self):
        self.left = Node()
        self.right = Node()
        self.tail = Node()
        self.head = Node()
class Solution:

    def treeToDoublyList(self, root: 'Node') -> 'Node':

        def dfs(node:Node):
            if not node:
                return
            dfs(node.left)
            # 中序链接
            if self.tail:
                self.tail.right = node
                node.left = self.tail
            else:
                self.head = node
            self.tail = node
            dfs(node.right)

        if not root:
            return None

        self.head , self.tail = None, None
        dfs(root)
        # 循环链表
        self.head.left = self.tail
        self.tail.right = self.head
        return self.head