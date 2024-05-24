class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def maxPathSumAnyNode(self, root: TreeNode) -> float:
        if not root: return 0
        self.max = -math.inf
        def dfs(node:TreeNode):
           if not node: # if node not exist, return -inf
               return  0
           left_pathsum = dfs(node.left)
           right_pathsum = dfs(node.right)
           left_maxsum = max(left_pathsum,0)
           right_maxsum = max(right_pathsum,0)
           self.max = max(self.max, left_maxsum + right_maxsum + node.val) ## we update max value if we choose current node
           return max((left_maxsum + node.val),(right_maxsum + node.val)) ## since that is anynode, so we can choose left max or right max

        dfs(root)
        return self.max
def max_leaf_to_leaf(root):
    if not root:
        return 0

    # Helper function to perform DFS and update max_sum
    ## 如果是leaf的话 他就必须走到底。  所以不需要， 直接一个dfs 就行，相当于简单了,
    ## 思路被那个math.inf 局限住了 。 只要是leaf node 返回 0 就可以了。
    ## node val 可以在后序的时候计算
    ## 只有那个有tag的时候用math.inf做值判断比较好， 因为 not node 返回是叶子节点 不适用了。 还需要有个tag flag，这个时候返回的是node 的val
    # left_maxsum = max(left_pathsum, 0)
    # right_maxsum = max(right_pathsum, 0)
    def dfs(node):
        nonlocal max_sum
        if not node:
            return 0

        left_sum = dfs(node.left)
        right_sum = dfs(node.right)

        # Calculate max path sum through the current node
        max_path_sum = left_sum + right_sum + node.val

        # Update max_sum if necessary
        max_sum = max(max_sum, max_path_sum)

        # Return max sum reachable from this node to any leaf
        return max(left_sum, right_sum) + node.val

    max_sum = float('-inf')
    dfs(root)
    return max_sum

def max_leaf_to_leaf_path(root):
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

    max_sum = float('-inf')
    max_path = []
    dfs(root)
    return max_sum, max_path


# Example usage:
# Constructing a sample binary tree
root = TreeNode(-15)
root.left = TreeNode(5)
root.right = TreeNode(6)
root.left.left = TreeNode(-8)
root.left.right = TreeNode(1)
root.left.left.left = TreeNode(2)
root.left.left.right = TreeNode(6)
root.right.left = TreeNode(3)
root.right.right = TreeNode(9)
root.right.right.right = TreeNode(0)
root.right.right.right.left = TreeNode(4)
root.right.right.right.right = TreeNode(-1)
root.right.right.right.right.left = TreeNode(10)

# t1 = TreeNode(4, TreeNode(3), TreeNode(10, TreeNode(1), TreeNode(2)))
# Find the maximum path sum between two leaf nodes
max_sum, max_path = max_leaf_to_leaf_path(root)
# max_sum, max_path = max_leaf_to_leaf_path(root)
print("Maximum path sum between two leaf nodes:", max_sum)
print("Path:", max_path)