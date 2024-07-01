import math


class Node:
    def __init__(self,value,tag):
        self.value  = value
        self.left = None
        self.right = None
        self.tag = tag

class Solution:

    def getDistanceBetweenAnyLeafNode(self,root:Node):
        max_value = -math.inf
        def dfs(node:Node):
            nonlocal  max_value

            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            sum = left + right + node.value
            max_value = max(sum,max_value)

            return max(left,right) + node.value
        dfs(root)
        return max_value

    def getDistanceBetweenAnyNode(self,root:Node):
        max_value = -math.inf
        def dfs(node:Node):
            nonlocal  max_value

            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            left = max(0,left) ## if that is anynode, we need add this
            right = max(0,right)
            sum = left + right + node.value
            max_value = max(sum,max_value)

            return max(left,right) + node.value
        dfs(root)
        return max_value


    def getDistanceBetweenAnyLeafNodePrintOut(self,root:Node):
        max_value = -math.inf
        max_path = []
        def dfs(node:Node):
            nonlocal max_value,max_path
            if not node:
                return 0,[]

            left,left_path = dfs(node.left)
            right,right_path = dfs(node.right)

            sum = left + right + node.value

            if sum > max_value:
                max_value = sum
                max_path = left_path + [node.value] + right_path[::-1]

            if left + node.value > right + node.value:
                return left + node.value, left_path + [node.value]
            else:
                ## right 需要reverse 所以正常加就行
                return right + node.value ,  right_path + [node.value]

        dfs(root)
        return max_path

    def maxPathBetweenLeafNodeWithTag(self,root:Node):
        max_sum = -math.inf
        def dfs(node:Node):
            nonlocal max_sum
            ## non node
            if not node:
                return -math.inf
            ## target leaf node
            if not node.left and not node.right and node.tag == True:
                return node.value
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            if left_sum != -math.inf and right_sum != -math.inf:
                max_sum = left_sum + right_sum + node.value ## we have activte node on both side
            elif left_sum != -math.inf:
                left_sum += node.value
            elif right_sum != -math.inf:
                right_sum += node.value

            return max(left_sum,right_sum)

        dfs(root)
        return max_sum

    def maxPathBetweenLeafNodeWithTag(self,root:Node):
        max_sum = -math.inf
        max_path = []
        def dfs(node:Node):
            nonlocal max_sum,max_path
            ## non node
            if not node:
                return -math.inf,[]
            ## target leaf node
            if not node.left and not node.right and node.tag == True:
                return node.value,[node.value]
            left_sum ,left_path = dfs(node.left)
            right_sum ,right_path = dfs(node.right)

            if left_sum != -math.inf and right_sum != -math.inf:
                max_sum = left_sum + right_sum + node.value ## we have activte node on both side
                max_path = left_path + [node.value] + right_path[::-1]
            elif left_sum != -math.inf:
                left_sum += node.value
            elif right_sum != -math.inf:
                right_sum += node.value

            if left_sum > right_sum:
                return left_sum, left_path + [node.value]
            else:
                return right_sum, right_path + [node.value]

        dfs(root)
        return max_sum
    def maxPathBewtweenAnyLeafNodeWithTag(self,root:Node):
        max_sum = -math.inf

        def dfs(node):
            nonlocal max_sum
            if not node :
                return -math.inf
            left_path = dfs(node.left)
            right_path = dfs(node.right)
            ## 如果左右都没有，同时当前节点不满足
            if left_path == -math.inf and right_path == -math.inf and node.tag == False:
                return -math.inf
            temp = -math.inf
            ## check if we have one node on each side
            if left_path != -math.inf:
                temp = max(temp,left_path)
            if right_path != -math.inf:
                temp = max(temp,right_path)
            ## get largest on both side

            if node.tag == True:
                if temp != -math.inf: ## we have one on either side
                    max_sum = max(max_sum,temp + node.value)
                return node.value
            else: ## current node is not tag
                ## left and right both have tag
                if left_path != -math.inf and right_path != -math.inf:
                    max_sum = max(max_sum, left_path + right_path + node.value)
                return temp + node.value

        dfs(root)
        return max_sum