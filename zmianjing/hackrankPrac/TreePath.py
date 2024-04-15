import math


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.tag = bool


class solution:
    ## value can be negticve
    def maxPathBetweenTwoLeafNode(self, root: Node):
        max_sum = -math.inf

        def dfs(node: Node):
            nonlocal max_sum
            if not node:
                return 0
            left_path = dfs(node.left)
            right_path = dfs(node.right)
            cur_sum = left_path + right_path + node.value
            if max_sum < cur_sum:
                max_sum = cur_sum

            return max(left_path, right_path) + node.value

        dfs(root)
        return max_sum

    def maxPathBetweenTwoLeafNodeWithTag(self, root: Node):
        max_sum = -math.inf

        def dfs(node: Node):
            nonlocal max_sum
            if not node:
                return -math.inf
            if not node.left and not node.right and node.tag is True:
                return node.value  ## only we have tag true, we can return value
            left_path = dfs(node.left)
            right_path = dfs(node.right)

            if left_path != -math.inf and right_path != -math.inf:  ## both side have value
                cur_sum = left_path + right_path + node.value
                if max_sum < cur_sum:
                    max_sum = cur_sum
            elif left_path != -math.inf:  # we only have left path
                left_path += node.value
            elif right_path != -math.inf:
                right_path += node.value

            return max(left_path, right_path)

        dfs(root)
        return max_sum

    def maxPathBetweenAnyLeafNodeWithTag(self, root: Node):
        max_sum = -math.inf

        def dfs(node: Node):
            nonlocal max_sum
            if not node:
                return -math.inf
            left_path = dfs(node.left)
            right_path = dfs(node.right)

            if left_path == -math.inf and right_path == -math.inf and node.tag is False:  ## we dont have any node so far
                return -math.inf

            ## we get larger of both side
            temp = -math.inf
            if left_path != -math.inf:
                temp = max(temp, left_path)
            if right_path != -math.inf:
                temp = max(temp, right_path)

            ## if current node is tag node , so we need cal the sum
            if node.tag is True:
                max_sum = max(max_sum, temp + node.value)
                return node.value  ## if current node is a node, we only return its value , since that is a 'target' node
            else:
                if left_path != -math.inf and right_path != -math.inf:  # we have path on both side
                    max_sum = max(max_sum, left_path + right_path + node.value)
                ## for this level, we return bigger side
                return temp + node.value

        dfs(root)
        return max_sum

    def maxPathPrintOutBetweenLeafNodeWithTag(self, root: Node):
        max_sum = -math.inf
        max_sum_path = []

        def dfs(node):
            nonlocal max_sum, max_sum_path
            if not node:
                return -math.inf, []  ## we return this because that leaf may not be our target
            ## 对于这个node 必须显式的让他设为True or False 才可以，因为default 是默认bool 变量 <class 'bool'>
            if not node.left and not node.right and node.tag == True:
                ## only return value when we are leaf and has tag
                return node.value, [node.value]  ##这才对嘛！！ 牛逼

            left_sum, left_sum_path = dfs(node.left)
            right_sum, right_sum_path = dfs(node.right)

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
                return right_sum, right_sum_path + [node.value]

        dfs(root)
        return max_sum, max_sum_path

    def maxPathWithoutTag(root):
        if not root:
            return 0, []

        # Helper function to perform DFS and update max_sum
        def dfs(node):
            nonlocal max_sum, max_path

            if not node:
                return 0, []

            left_sum, left_path = dfs(node.left)
            right_sum, right_path = dfs(node.right)

            # Calculate max path sum through the current node
            max_path_sum = left_sum + right_sum + node.val

            # Check if the current path has a greater sum
            if max_path_sum > max_sum:
                max_sum = max_path_sum
                max_path = left_path + [node.val] + right_path[::-1]

            # Return max sum reachable from this node to any leaf
            if left_sum > right_sum:
                return left_sum + node.val, left_path + [node.val]
            else:
                return right_sum + node.val, right_path + [node.val]

        max_sum = -math.inf
        max_path = []
        dfs(root)
        return max_sum, max_path


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

sol = solution()
print(sol.maxPathBetweenTwoLeafNode(root))

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
root.right.right.tag = True  ## test for anynode
root.right.right.right = Node(0)
root.right.right.right.left = Node(4)
root.right.right.right.left.tag = False
root.right.right.right.right = Node(-1)
root.right.right.right.right.tag = False
root.right.right.right.right.left = Node(10)
root.right.right.right.right.left.tag = True
max_sum = sol.maxPathBetweenTwoLeafNodeWithTag(root)
print("Maximum path sum between two leaf nodes:", max_sum)

max_sum = sol.maxPathBetweenAnyLeafNodeWithTag(root)
print("Maximum path sum between any leaf nodes:", max_sum)

max_sum, path = sol.maxPathPrintOutBetweenLeafNodeWithTag(root)
print("Maximum path sum between any leaf nodes:", max_sum, path)