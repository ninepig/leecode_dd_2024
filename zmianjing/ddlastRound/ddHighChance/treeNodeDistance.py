'''
最经典题目
1 两个节点之间最大path sum
2 with tag node
3 with tag node anynode max
4 print path 应该是基于第2个。 也就是 any leaf node with/out tag node 的最长path

'''

import math

class Node :
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.tag = bool

class Solution:
    def maxPathBewtweenAnyLeafNodeWithoutTag(self,root:Node):
        max_sum = -math.inf
        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0 ## reach leaf node's leaf
            left = dfs(node.left)
            right = dfs(node.right)
            left = max(0,left) ## any node
            right = max(0,right) ## any node
            max_sum = max(max_sum,left + right + node.value) ## update value while dfs searching
            return max((left + node.value), (right + node.value)) # for this node, we need return max value of left or right side
        dfs(root)
        return max_sum
    def maxSumBetweenLeafNodeWithoutTag(self,root:Node):
        max_sum = -math.inf
        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0 ## reach leaf node's leaf
            left = dfs(node.left)
            right = dfs(node.right)
            max_sum = max(max_sum,left + right + node.value) ## update value while dfs searching

            return max((left + node.value), (right + node.value)) # for this node, we need return max value of left or right side
        dfs(root)
        return max_sum

    def maxPathBetweenLeafNodeWithoutTag(self,root:Node):
        max_sum = -math.inf
        max_sum_path = []

        def dfs(node):
            nonlocal max_sum,max_sum_path
            if not node:
                return 0,[]

            left, left_path = dfs(node.left)
            right, right_path = dfs(node.right)
            sum_current_level = left + right + node.value
            ## 左右path 合并
            if sum_current_level > max_sum:
                max_sum = sum_current_level
                max_sum_path = left_path + [node.value] + right_path[::-1]

            if left + node.value > right + node.value:
                return left + node.value , left_path + [node.value]
            else:
                ## 错了 后序， 所以要直接相加， 因为最后会reverse
                # return right + node.value , [node.value] + right_path[::-1]
                return right + node.value, right_path + [node.value]

        dfs(root)
        return max_sum,max_sum_path


    def maxPathBetweenLeafNodeWithTag(self,root:Node):
        max_sum = -math.inf
        def dfs(node):
            nonlocal  max_sum
            if not node:
                return -math.inf ## we return this because that leaf may not be our target
            ## 对于这个node 必须显式的让他设为True or False 才可以，因为default 是默认bool 变量 <class 'bool'>
            if not node.left and not node.right and node.tag == True:
                ## only return value when we are leaf and has tag
                return node.value

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            if left_sum != -math.inf and right_sum != -math.inf:
                ## we have leaf node on both side
                max_sum = max(max_sum, left_sum + right_sum + node.value)
            elif left_sum!= -math.inf:
                left_sum += node.value
            elif right_sum != -math.inf:
                right_sum += node.value

            ## return bigger of each side
            return max(left_sum,right_sum)

        dfs(root)
        return max_sum

    def maxPathPrintOutBetweenLeafNodeWithTag(self, root: Node):
        max_sum = -math.inf
        max_sum_path = []
        def dfs(node):
            nonlocal max_sum,max_sum_path
            if not node:
                return -math.inf,[] ## we return this because that leaf may not be our target
            ## 对于这个node 必须显式的让他设为True or False 才可以，因为default 是默认bool 变量 <class 'bool'>
            if not node.left and not node.right and node.tag == True:
                ## only return value when we are leaf and has tag
                return node.value, [node.value] ##这才对嘛！！ 牛逼

            left_sum,left_sum_path = dfs(node.left)
            right_sum,right_sum_path  = dfs(node.right)

            if left_sum != -math.inf and right_sum != -math.inf:
                ## we have leaf node on both side
                max_sum = max(max_sum, left_sum + right_sum + node.value)
                max_sum_path = left_sum_path + [node.value] + right_sum_path[::-1]
            elif left_sum != -math.inf:
                left_sum += node.value
            elif right_sum != -math.inf:
                right_sum += node.value
            if left_sum > right_sum:
                return left_sum, left_sum_path + [node.value]
            else:
                return right_sum , right_sum_path + [node.value]
        dfs(root)
        return max_sum,max_sum_path

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



root = Node(-15)
root.left = Node(5)
root.right = Node(6)
root.left.left = Node(-8)
root.left.right = Node(1)
root.left.left.left = Node(2)
root.left.left.right = Node(6)
root.right.left = Node(3)
root.right.right = Node(9)
root.right.right.right = Node(0)
root.right.right.right.left = Node(4)
root.right.right.right.right = Node(-1)
root.right.right.right.right.left = Node(10)

sol = Solution()
# t1 = TreeNode(4, TreeNode(3), TreeNode(10, TreeNode(1), TreeNode(2)))
# Find the maximum path sum between two leaf nodes
max_sum = sol.maxSumBetweenLeafNodeWithoutTag(root)
# max_sum, max_path = max_leaf_to_leaf_path(root)
print("Maximum path sum between two leaf nodes:", max_sum)
# print("Path:", max_path)

max_sum, max_path = sol.maxPathBetweenLeafNodeWithoutTag(root)
# max_sum, max_path = max_leaf_to_leaf_path(root)
print("Maximum path sum between two leaf nodes:", max_sum)
print("Path:", max_path)


max_sum = sol.maxPathBewtweenAnyLeafNodeWithoutTag(root)
print("Maximum path sum between two leaf nodes:", max_sum)

root = Node(-15)
root.left = Node(5)
root.right = Node(6)
root.left.left = Node(-8)
root.left.right = Node(1)
root.left.left.left = Node(2)
root.left.left.left.tag = True
root.left.left.right = Node(6)
root.left.left.right.tag = False
root.right.left = Node(3)
root.right.right = Node(9)
root.right.right.tag = True ## test for anynode
root.right.right.right = Node(0)
root.right.right.right.left = Node(4)
root.right.right.right.left.tag = False
root.right.right.right.right = Node(-1)
root.right.right.right.right.tag = False
root.right.right.right.right.left = Node(10)
root.right.right.right.right.left.tag = True
max_sum = sol.maxPathBetweenLeafNodeWithTag(root)
print("Maximum path sum between two leaf nodes:",max_sum)

max_sum,path = sol.maxPathPrintOutBetweenLeafNodeWithTag(root)
print("Maximum path sum between two leaf nodes:",max_sum)
print(path)

max_sum = sol.maxPathBewtweenAnyLeafNodeWithTag(root)
print(max_sum)