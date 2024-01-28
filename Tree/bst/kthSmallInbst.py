from Tree.TreeBasic.TreeNode import TreeNode


class Solution:
    '''
    inorder的实践
    '''
    def kthSmallest(self, root: TreeNode , k : int) -> TreeNode:
        stack = []
        count = 0
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            count += 1
            node = stack.pop()
            if count == k:
                return node.val
            node = node.right
        return -1
