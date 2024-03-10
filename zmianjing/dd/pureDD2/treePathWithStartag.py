'''
Max value path in Binary search (OK)
●Variation of Leetcode 124
●Given a binary tree with alive nodes,
alive node can only be leaf nodes and marked with aterisk mask. Find the maximum path length between two alive nodes.
'''
import math


class TreeNode:
    def __init__(self,):
        self.val  = 0
        self.left = TreeNode()
        self.right = TreeNode()
        self.star = True

class solution:
    ## post travel
    ## alive node can only be child node
    def maxPath(self,root:TreeNode):
        self.max = 0
        def dfs(node:TreeNode):
            if not root:
                return -math.inf
            if not node.left and not node.right and node.star : # we find a alive node, leaf node and has tag value
                return node.val
            cur_val = node.val
            leftPath = dfs(node.left)
            rightPath = dfs(node.right)
            if leftPath != -math.inf and rightPath != -math.inf :
                #We have live node on both side
                self.max = max(self.max, cur_val + rightPath + leftPath)
            if leftPath != -math.inf: # make sure we have a live node on left, then plus current val
                leftPath += node.val
            if rightPath != -math.inf:
                rightPath += node.val
            return max(leftPath,rightPath) ## current node, can return max of left or right

        dfs(root)
        return self.max

    '''
    livenode can be any node, not child node only'''
    def maxPathAnylivenode(self,root:TreeNode):
        self.max = 0
        def dfs(node:TreeNode):
            if not node :
                return -math.inf
            leftPath = dfs(node.left)
            rightPath = dfs(node.right)
            # 看看左侧右侧有没有live node
            if leftPath == -math.inf and rightPath == -math.inf and  not node.star :
                return -math.inf ## no live node so far
            temp = -math.inf ## live node distance so far
            if leftPath != -math.inf: ## we have live node on left
                temp = max(temp,leftPath)
            if rightPath != -math.inf:
                temp = max(temp,rightPath)

            if node.star :
                if temp!= -math.inf:
                    ## we have two live node now
                    ## 这里有bug
                    self.max = max(self.max,temp)
                return node.val # return current node's val , node to node,
            else:
                ## current node is not star, we have live node on two side
                if leftPath != -math.inf and rightPath != -math.inf :
                    self.max = max(self.max, leftPath + rightPath + node.val)
                return temp + node.val # return max on single side.
        dfs(root)
        return self.max





