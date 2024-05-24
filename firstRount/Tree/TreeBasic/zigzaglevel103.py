import collections


class TreeNode:
    def __init__(self,value : int = 0):
        self.val = value
        self.left = TreeNode()
        self.right = TreeNode()

class Solution:
    def ziglevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        odd = True
        res = []
        while queue:
            # 关键点
            level = collections.deque()
            size = len(queue)
            for _ in range(size):
                #关键点
                cur = queue.pop(0)
                if odd:
                    level.append(cur.val)
                else:
                    level.appendleft(cur.val)
                if cur.left :
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            if level:
                # 关键点
                res.append(list(level))

            odd = not odd

        return res
