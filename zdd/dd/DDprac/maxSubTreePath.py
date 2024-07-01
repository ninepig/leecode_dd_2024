'''
这道题目前看到有纯变种 + followup ， 普通 + follow 的组合 所以都需要做一遍

普通版 124
普通版 124 + followup --》 print path
变种 --》 leafnode +starMark
变种follow --》 anynode + starMark
'''
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    '''
    124
    if node is empty--> return 0
    check left side
    check right side
    left max is 0 or left (could be minous)
    right max is 0 or right

    calc the max value during travel
    return max left or max right as the end of this travel

    '''
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root : return 0
        max_path_sum = 0

        def dfs(root:TreeNode):
            nonlocal max_path_sum ## 或者用self.xxx
            if not root:
                return 0
            left_path = dfs(root.left)
            right_path = dfs(root.right)

            left_max = max(left_path,0)
            right_max = max(right_path,0)

            max_path_sum = max(max_path_sum,left_max + right_max + root.val)

            return max(left_max + root.val , right_max + root.val)

        dfs(root)

        return max_path_sum

    '''
    对于当前节点 sum / max 值 也就是到当前节点最大值， 以及算上当前节点的summary 。 因为可以选择取当前点 或者不取当前点
    '''
    def get_max_sum_path_follow_up(root):
        def recur(node):
            if not node:
                return (0, [], 0, [])

            ## 取得左侧sum， 左侧path  左侧max值，左侧max path
            left_s, left_s_path, left_m, left_m_path = recur(node.left)
            right_s, right_s_path, right_m, right_m_path = recur(node.right)

            # 如果左侧sum 是小于0， 那就path 为空 sum为0
            left_s, left_s_path = (0, []) if left_s <= 0 else (left_s, left_s_path)
            right_s, right_s_path = (0, []) if right_s <= 0 else (right_s, right_s_path)

            ## 计算包含当前节点的最大值，最大path
            ## 如果左侧大于右侧
            if left_s > right_s:
                ## current sum 就取 左侧 + 当前值
                curr_s, curr_s_path = left_s + node.val, left_s_path + [node.val]
            else:
                curr_s, curr_s_path = right_s + node.val, right_s_path + [node.val]

            ## 如果两边都有，则表示左右都有路径，更新max值的path
            if node.left and node.right:  ##最大值在左侧/右侧/当前
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


