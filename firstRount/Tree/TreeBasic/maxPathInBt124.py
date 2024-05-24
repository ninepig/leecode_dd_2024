class TreeNode:
    def __init__(self,value : int = 0):
        self.val = value
        self.left = TreeNode()
        self.right = TreeNode()

'''这道是个难题'''
class Solution:
    def __init__(self):
        self.ans = float('-inf')

    def dfs(self,node :TreeNode)-> int:
        if not node : return 0
        # 左子树提供的最大贡献值
        left_max = max(self.dfs(node.left),0)
        # 右子树提供的最大贡献值
        right_max = max(self.dfs(node.right),0)
        # 包含当前节点和左右子树的最大路径和
        cur_path = left_max + right_max + node.val
        # 更新所有路径中的最大路径和
        self.ans = max(self.ans,cur_path)

        # 这里返回的是这个点作为边的最大贡献
        return max(left_max,right_max) + node.val


    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.ans