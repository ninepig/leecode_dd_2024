import math


class TreeNode:
    def __int__(self,val):
        self.val = val
        self.left = TreeNode()
        self.right = TreeNode()
        self.star = True ## activate node

class Solution:
    ## 加了tag这个变量 其实和原来的题目差的不少， 因为就不能无脑 not node 返回 0 作为叶子节点的判断方法了
    def maxPathSumLeafNodeWithTag(self, root: TreeNode) -> int:
        if not root: return 0
        self.max = -math.inf

        def dfs(node: TreeNode):
            if not node:
                return -math.inf
            if not node.left and not node.right and node.star:  ## leaf node with star tag,
                return node.val
            left_pathsum = dfs(node.left)  ## get left path
            right_pathsum = dfs(node.right)  ## get right path
            if left_pathsum != -math.inf and right_pathsum != -math.inf:  ## we have leaf node in left/right side
                self.max = max(self.max, left_pathsum + right_pathsum + node.val)
            elif left_pathsum != -math.inf:  ## we only have leaf node on left side
                left_pathsum += node.val
            elif right_pathsum != -math.inf:  ## we only have leaf node on right side
                right_pathsum += node.val

            return max(left_pathsum, right_pathsum)  ## return larger path to parent node

        dfs(root)
        return int(self.max)


    def maxPathSumLeafNodeWithTagAnyNode(self, root: TreeNode) -> int:
        if not root: return 0
        self.max = -math.inf

        def dfs(node:TreeNode):
            if not node:
                return -math.inf
            left_path = dfs(node.left)
            right_path = dfs(node.right)
            ## no node on left, right and current node does not have star tag
            if left_path == -math.inf and right_path == -math.inf and not node.star:
                return -math.inf
            ## left or right or node is star --> 3 situations
            temp = -math.inf
            if left_path != -math.inf:
                temp = max(temp,left_path)
            if right_path != -math.inf:
                temp = max(temp,right_path)
            ## get larget on both side

            if node.star : # current node is a star tag, so we need update max value
                if temp != -math.inf: ## we have left or right node
                    # self.max = max(self.max,temp + node.val)
                    self.max = max(self.max, temp + node.val) ## we update with larger value + current value
                return node.val ## for this dfs, we only return node's value, our target is value in any node
            else: ## current node is not target node
                if left_path != -math.inf and right_path != -math.inf: ## we have two side node
                    self.max = max(self.max,left_path + right_path + node.val)
                return temp + node.val ## temp is larger one on both side, so we return this to parent level

        dfs(root)
        return int(self.max)