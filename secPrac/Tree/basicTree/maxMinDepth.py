class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1


    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        min_depth = 0
        if root.left:
            ## 计算左侧最小
            min_depth = min(min_depth,self.minDepth(root.left))
        if root.right :
            #计算右侧最小
            min_depth = min(min_depth,self.minDepth(root.right))

            #对于当前层最小的就是 左右最小的+1
        return min_depth + 1