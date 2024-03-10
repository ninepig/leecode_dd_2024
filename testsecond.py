class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_max_sum_path(root):
    def recur(node):
        if not node:
            return (0, [], 0, [])

        ## 取得左侧sum， 左侧path  左侧max值，左侧max path
        left_s, left_s_path, left_m, left_m_path = recur(node.left)
        right_s, right_s_path, right_m, right_m_path = recur(node.right)

        #如果左侧sum 是小于0， 那就path 为空 sum为0
        left_s, left_s_path = (0, []) if left_s <= 0 else (left_s, left_s_path)
        right_s, right_s_path = (0, []) if right_s <= 0 else (right_s, right_s_path)

        ## 计算当前节点的最大值，最大path
        ## 如果左侧大于右侧
        if left_s > right_s:
            ## current sum 就取 左侧 + 当前值
            curr_s, curr_s_path = left_s + node.val, left_s_path + [node.val]
        else:
            curr_s, curr_s_path = right_s + node.val, right_s_path + [node.val]

        ## 如果两边都有 ，计算
        if node.left and node.right: ##最大值在左侧/右侧/当前
            if left_m == max(left_m, right_m, left_s + right_s + node.val):
                curr_m, curr_m_path = left_m, left_m_path

            elif right_m == max(left_m, right_m, left_s + right_s + node.val):
                curr_m, curr_m_path = right_m, right_m_path

            else:
                curr_m, curr_m_path = left_s + right_s + node.val, left_s_path + [node.val] + list(
                    reversed(right_s_path))

        elif node.left:
            if left_m == max(left_m, left_s + right_s + node.val):
                curr_m, curr_m_path = left_m, left_m_path
            else:
                curr_m, curr_m_path = left_s + node.val, left_s_path + [node.val]

        elif node.right:
            if right_m == max(right_m, left_s + right_s + node.val):
                curr_m, curr_m_path = right_m, right_m_path
            else:
                curr_m, curr_m_path = right_s + node.val, [node.val] + list(reversed(right_s_path))

        else:
            curr_m, curr_m_path = node.val, [node.val]

        return (curr_s, curr_s_path, curr_m, curr_m_path)

    a, b, c, d = recur(root)
    if a >= c:
        return a, b
    return c, d


t1 = TreeNode(4, TreeNode(3), TreeNode(10, TreeNode(1), TreeNode(2)))
print(get_max_sum_path(t1))
# (19, [3, 4, 10, 2])