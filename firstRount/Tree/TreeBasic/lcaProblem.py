
class TreeNode:
    def __init__(self,value : int = 0):
        self.val = value
        self.left = TreeNode()
        self.right = TreeNode()

'''
lca general
设 lca_node 为节点 p、q 的最近公共祖先。则 lca_node 只能是下面几种情况：

p、q 在 lca_node 的子树中，且分别在 lca_node 的两侧子树中。
p == lca_node，且 q 在 lca_node 的左子树或右子树中。
q == lca_node，且 p 在 lca_node 的左子树或右子树中。
'''

'''
如果当前节点 node 等于 p 或者 q，那么 node 就是 p、q 的最近公共祖先，直接返回 node。
如果当前节点 node 不为 None，则递归遍历左子树、右子树，并判断左右子树结果。
如果左右子树都不为空，则说明 p、q 在当前根节点的两侧，当前根节点就是他们的最近公共祖先。
如果左子树为空，则返回右子树。
如果右子树为空，则返回左子树。
如果左右子树都为空，则返回 None。
如果当前节点 node 为 None，则说明 p、q 不在 node 的子树中，不可能为公共祖先，直接返回 None。
'''
class Solution:
    def lcaOrTwoTreeNode(self, root: TreeNode, p:TreeNode,q:TreeNode) -> TreeNode:
        if p == root or q == root:
            return root
        if root:
            lca_left = self.lcaOrTwoTreeNode(root.left,p,q)
            lca_right = self.lcaOrTwoTreeNode(root.right,p,q)

            if lca_right and lca_left:
                return root
            if lca_right :
                return lca_right
            if lca_left :
                return lca_left

        return None

'''
从根节点 root 开始遍历。
如果当前节点的值大于 p、q 的值，说明 p 和 q 应该在当前节点的左子树，因此将当前节点移动到它的左子节点，继续遍历；
如果当前节点的值小于 p、q 的值，说明 p 和 q 应该在当前节点的右子树，因此将当前节点移动到它的右子节点，继续遍历；
如果当前节点不满足上面两种情况，则说明 p 和 q 分别在当前节点的左右子树上，则当前节点就是分岔点，直接返回该节点即可。
'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestor = root
        while True:
            if ancestor.val > p.val and ancestor.val > q.val:
                ancestor = ancestor.left
            elif ancestor.val < p.val and ancestor.val < q.val:
                ancestor = ancestor.right
            else:
                break
        return ancestor
