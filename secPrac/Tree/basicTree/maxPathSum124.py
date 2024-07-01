class Solution:
    '''这题真的经典'''
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root :
            return 0
        ans = float('-inf')
        def dfs(node):
            if not node:
                return 0
            global ans
            max_left = max(dfs(node.left),0)
            max_right = max(dfs(node.right),0)
            max_current = max_left + max_right + node.val
            ans = max(max_current,ans)

            return max(max_left,max_right) + node.val # 对于当前节点 他可以选择左边或者右边作为贡献， 所以我们选取最大的值
        dfs(root)
        return ans

