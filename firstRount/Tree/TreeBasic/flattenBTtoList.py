class Solution:
    '''这道题关键是按照前序来做 那我们可以先转成前序数组,然后再拼接
    直观 易懂 就是需要额外的数组'''
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        preorderList = list()

        def preorderTraversal(root: TreeNode):
            if root:
                preorderList.append(root)
                preorderTraversal(root.left)
                preorderTraversal(root.right)

        preorderTraversal(root)
        size = len(preorderList)
        for i in range(1, size):
            prev, curr = preorderList[i - 1], preorderList[i]
            prev.left = None
            prev.right = curr

    #如果要求没有额外空间 就要用恶心人的比那里方法
    '''
    将左子树插入到右子树的地方
将原来的右子树接到左子树的最右边节点
考虑新的右子树的根节点，一直重复上边的过程，直到新的右子树为 null
https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/solutions/17274/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by--26/
'''

    def flattenTravel(self,root:TreeNode) -> None:
        if not root:
            return
        while root:
            # if there is no left node,move forward
            if not root.left :
                root = root.right
            else:
                pre = root.left # find most right node of left node, this will be the pre node of current's right node
                while pre:
                    pre = pre.right

                pre.right =root.right # connect right node to it's pre node
                root.right = root.left
                root.left = None
                root = root.right # move to next node
