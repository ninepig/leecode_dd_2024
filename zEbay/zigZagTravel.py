# Write a function for zigzag traversal in a binary tree.

import collections


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def ZigZagView(self, root: TreeNode):
        if not root:
            return []
        res = []
        queue = collections.deque(root)
        level = 0
        while queue:
            cur_level_size = len(queue)
            cur_level = res
            for i in range(cur_level_size):
                cur = queue.popleft()
                cur_level.append(cur.value)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            if level % 2 == 0:
                res.append(cur_level)
            else:
                res.append(cur_level[::-1])
            level += 1
        return res
