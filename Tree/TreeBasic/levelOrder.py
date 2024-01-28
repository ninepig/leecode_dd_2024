
class TreeNode:
    def __init__(self,value : int = 0):
        self.val = value
        self.left = TreeNode()
        self.right = TreeNode()

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # if not root:
        #     return []
        # queue = [root]
        # order = []
        # while queue:
        #     level = []
        #     size = len(queue)
        #     for _ in range(size):
        #         curr = queue.pop(0)
        #         level.append(curr.val)
        #         if curr.left:
        #             queue.append(curr.left)
        #         if curr.right:
        #             queue.append(curr.right)
        #     if level:
        #         order.append(level)
        # return order
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            cur_level = []
            size = len(queue)
            for _ in range(size):
                cur = queue.pop(0)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                cur_level.append(cur.val)
            if cur_level:
                res.append(cur_level)

        #return res
        # question 107 ,排序反转
        return res[::-1]
