import collections


class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def leftView(self,root:TreeNode):
        if not root:
            return []
        res = []
        queue = collections.deque(root)
        while queue:
            cur_level_size = len(queue)
            for i in range(cur_level_size):
                cur = queue.popleft()
                if i == 0:
                    res.append(cur.value)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

        return res
        