class TreeNode:
    def __init__(self, val=0, left=None, right=None,star=False):
        self.val = val
        self.left = left
        self.right = right
        self.star = star

'''这个题比124 有意思多了 之前还是没理解124
124 可以取0 ， 但是这个题 有一个必须livenode的概念'''
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxValue = float('-inf')

        def dfs(node:TreeNode) -> float:
            if not node:
                return float('-inf')
            ## find live node
            if not node.left and not node.left and node.star:
                return node.val # return live node's value

            curValue = node.val
            leftPathValue = dfs(node.left)
            rightPathValue = dfs(node.right)
            # they have a path means there is a live node on that path
            if leftPathValue != float('-inf') and rightPathValue !=  float('-inf'):
                self.maxValue = max(self.maxValue, curValue + leftPathValue + rightPathValue)
            ## make sure left has a live node
            leftMax =  leftPathValue if leftPathValue == float('-inf') else leftPathValue + curValue
            rightMax = rightPathValue if rightPathValue == float('-inf') else rightPathValue + curValue
            return max(leftMax, rightMax)

        dfs(root)
        return int(self.maxValue)


    ## follow up liveNode 不一定是leaf, 很有意思
    def maxPathSumAnyLiveNode(self, root: Optional[TreeNode]) -> int:
        self.maxValue = float('-inf')
        def dfs(node:TreeNode) -> float:
            if not node:
                return float('-inf')
            leftSum = dfs(node.left)
            rightSum = dfs(node.right)

            # 左侧没有live node 右侧没有live node 自己不是live node 那就返回-inf
            if leftSum == float('-inf') and rightSum == float('-inf') and not node.star:
                return float('-inf')

            # 两侧有任意的live Node， 我们就更新到目前节点最长的temp
            temp = float('-inf')
            if leftSum != float('-inf'):
                temp = max(leftSum,temp)
            if rightSum != float('-inf'):
                temp = max(rightSum,temp)

            if node.star:
                if temp != float('-inf'):
                    #我们有两个live node了,更新值
                    self.maxValue = max(self.maxValue,temp)
                return node.val # 只返回当前livenode 值， 因为更新过了，只能是点对点
            else: ## 当前点不是start Node
                if leftSum != float('-inf') and rightSum != float('-inf') :
                    # 两侧都有live node 更新最大值
                    self.maxValue = max(self.maxValue,leftSum + rightSum + node.val)
                return temp + node.val # 如果没有两边都有，那就返回当前最大值

        dfs(root)
        return int(self.maxValue)