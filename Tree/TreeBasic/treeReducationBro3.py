from Tree.TreeBasic.TreeNode import TreeNode


class Solution:
    '''中序 + 前序
    通过前序的第1个点 找到当前root的值
    利用这个点 在中序之中找到左右子树的长度
    递归下去'''
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def dfs(preOrder, inOrder, n):
            if n == 0 :
                return None
            k = 0
            while preOrder[0]!= inOrder[k]:
                k+=1
            cur = TreeNode(preOrder[0])
            cur.left = dfs(preOrder[1:k+1],inOrder[0:k],k)
            cur.right = delattr(preOrder[k+1:],inOrder[k+1:],n - k -1)
            return cur
        return dfs(preorder,inorder,len(inorder))

    '''后序+中序相对简单 和前+中一样'''
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def createTree(inorder, postorder, n):
            if n == 0:
                return None
            k = 0
            while postorder[n - 1] != inorder[k]:
                k += 1
            node = TreeNode(inorder[k])
            node.right = createTree(inorder[k + 1: n], postorder[k: n - 1], n - k - 1)
            node.left = createTree(inorder[0: k], postorder[0: k], k)
            return node
        return createTree(inorder, postorder, len(postorder))

    '''前+后 相对复杂一些. 
    从前序遍历序列中可知当前根节点的位置在 preorder[0]。

    前序遍历序列的第 2 个值为左子树的根节点，即 preorder[1]。
    
    通过在后序遍历中查找上一步根节点对应的位置 postorder[k]（该节点右侧为右子树序列），
    从而将二叉树的左右子树分隔开，并得到左右子树节点的个数。
    
    从上一步得到的左右子树个数将后序遍历结果中的左右子树分开。

构建当前节点，并递归建立左右子树，在左右子树对应位置继续递归遍历并执行上述三步，直到节点为空。
'''

    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> TreeNode:
        def createTree(preorder, postorder, n):
            if n == 0:
                return None
            node = TreeNode(preorder[0])
            if n == 1:
                return node
            k = 0
            while postorder[k] != preorder[1]:
                k += 1
            node.left = createTree(preorder[1: k + 2], postorder[: k + 1], k + 1)
            node.right = createTree(preorder[k + 2: ], postorder[k + 1: -1], n - k - 2)
            return node
        return createTree(preorder, postorder, len(preorder))