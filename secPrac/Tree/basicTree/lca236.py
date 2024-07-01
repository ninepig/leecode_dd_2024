class Solution:
    '''
如果当前节点 node 等于 p 或者 q，那么 node 就是 p、q 的最近公共祖先，直接返回 node。
如果当前节点 node 不为 None，则递归遍历左子树、右子树，并判断左右子树结果。
如果左右子树都不为空，则说明 p、q 在当前根节点的两侧，当前根节点就是他们的最近公共祖先。
如果左子树为空，则返回右子树。
如果右子树为空，则返回左子树。
如果左右子树都为空，则返回 None。
如果当前节点 node 为 None，则说明 p、q 不在 node 的子树中，不可能为公共祖先，直接返回 None
    '''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or root == q:
            return root
        if root:
            node_left = self.lowestCommonAncestor(root.left, p , q )
            node_right = self.lowestCommonAncestor(root.right, p , q)

            if node_right and node_left:
                return root
            if node_right and node_left is None:
                return node_right
            if node_left and node_right is None:
                return node_left

        return None