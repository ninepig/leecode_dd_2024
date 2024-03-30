import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSumLeafToLeaf(self,root:TreeNode):

        # dfs
        '''
        maintain
        1 sum so far
        2 path so far
        3 max value so far
        4 max value's path
        '''
        def dfs(node:TreeNode):
            # if not node:
            #     return (-math.inf,[],-math.inf,[])
            # left_s, left_s_path , left_m , left_m_path = dfs(node.left)
            # right_s, right_s_path, right_m , right_m_path = dfs(node.right)
            #
            # ## if we have node on left / right side, othersie, remain empty
            # left_s , left_s_path = (-math.inf,[]) if left_s == -math.inf else (left_s,left_s_path)
            # right_s , right_s_path = (-math.inf,[]) if right_s == -math.inf else (right_s,right_s_path)
            if not node:
                return (0, [], 0, [])

                ## 取得左侧sum， 左侧path  左侧max值，左侧max path
            left_s, left_s_path, left_m, left_m_path = dfs(node.left)
            right_s, right_s_path, right_m, right_m_path = dfs(node.right)

            # 如果左侧sum 是小于0， 那就path 为空 sum为0
            left_s, left_s_path = (0, []) if left_s <= 0 else (left_s, left_s_path)
            right_s, right_s_path = (0, []) if right_s <= 0 else (right_s, right_s_path)

            ## get curr_summary max, curr_summary path
            if left_s > right_s :
                curr_s = left_s + node.val
                curr_s_path = left_s_path + [node.val]
            else:
                curr_s = right_s + node.val
                curr_s_path = right_s_path + [node.val]

            if node.left and node.right: ## we have value on both side
                ## largest value is on left side
                if left_m == max(left_m,right_m,left_s + right_s + node.val):
                    curr_m = left_m
                    curr_m_path = left_m_path
                ## largest value is on right side
                elif right_m == max(left_m,right_m,left_s+right_s + node.val):
                    curr_m = right_m
                    curr_m_path = right_m_path
                else:## largest is contain current node
                    curr_m = left_s + right_s + node.val
                    curr_m_path = left_s_path + [node.val] + list(reversed(right_s_path))
            elif node.left:
                ## we only have value on left side
                if left_m == max(left_m, left_s + node.val): ## check if largest is contain current node
                    curr_m = left_m
                    curr_m_path = left_m_path
                else:
                    curr_m = left_s + node.val
                    curr_m_path = left_s_path + [node.val]
            elif node.right:
                if right_m == max(right_m, right_s + node.val): ## check if largest is contain current node
                    curr_m = right_m
                    curr_m_path = right_m_path
                else:
                    curr_m = right_s + node.val
                    curr_m_path = [node.val] + list(reversed(right_s_path))
            else: ## left right empty
                curr_m  = node.val
                curr_m_path = [node.val]

            return (curr_s,curr_s_path,curr_m, curr_m_path)

        a, b, c, d = dfs(root)
        if a >= c:
            return a, b
        return c, d

# test = Solution()
# t1 = TreeNode(4, TreeNode(3), TreeNode(10, TreeNode(1), TreeNode(2)))
# print(test.pathSumLeafToLeaf(t1))
# (19, [3, 4, 10, 2])


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