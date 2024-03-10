import math


class TreeNode:
    def __init__(self,):
        self.val  = 0
        self.left = TreeNode()
        self.right = TreeNode()
        self.star = True


'''
124的变种
1 leaf node + starTag 才能算值，其他都不行
2 dfs的过程 ， 对于空结点 我们直接返回 inf
2.1 只有对于子节点+ 有tag的节点 我们才返回 value
2.2 比较左侧， 右侧， 如果左侧右侧都有节点 我们可以统计结果
2.3 如果只有单侧有节点 我们可以将当前的值返回给上一曾
'''
class Solution:
    def getMaxPath(self, root:TreeNode):
        self.max = 0
        def dfs(node:TreeNode):
            if not node:
                return -math.inf
            if not node.left and not node.right and node.star:
                return node.val
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            if left_sum != -math.inf and right_sum != -math.inf : # we have left path,right path available
                self.max = max(self.max, left_sum + right_sum + node.val)  ## during travel, we updated max value
            elif left_sum != -math.inf:
                left_sum += node.val
            elif right_sum != -math.inf:
                right_sum += node.val

            return max(right_sum, left_sum) ## return max of left/right path
        dfs(root)
        return self.max

    def getMaxPathAnyNode(self,root:TreeNode):
        self.max = 0
        def dfs(node:TreeNode):
            if not node:
                return -math.inf
            left_path = dfs(node.left)
            right_path = dfs(node.right)
            ## if two side has no tag node, and node is not tag node , return -math.inf
            if left_path == -math.inf and right_path == -math.inf and not node.star:
                return -math.inf

            temp = -math.inf
            ## if any side is not empty, get latest on left/right side
            if left_path != -math.inf:
                temp = max(temp, left_path)
            if right_path != -math.inf:
                temp = max(temp,right_path)

            if node.star: # we found two node
                if temp != -math.inf:
                    # self.max = max(self.max, temp) 答案有问题
                    self.max = max(self.max,temp + node.val)
                return node.val ## we only need return node.val
            else: # node is not target node
                if left_path != -math.inf and right_path != -math.inf:
                    ## we have two node on both left, right side
                    self.max = max(self.max, left_path + right_path + node.val)
                return temp + node.val # we only return larger on two side
        dfs(root)
        return self.max