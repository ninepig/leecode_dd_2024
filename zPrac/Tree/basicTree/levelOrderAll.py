class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        queue = [root]
        while queue:
            size = len(queue)
            cur = []
            for i in range(size):
                temp = queue.pop(0)
                cur.append(temp.val)
                if cur.left :
                    queue.append(cur.left)
                if cur.right :
                    queue.append(cur.right)
            if cur:
                ans.append(cur)
        return ans

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        order = []
        odd = True
        while queue:
            level = collections.deque()
            size = len(queue)
            for _ in range(size):
                curr = queue.pop(0)
                if odd:
                    level.append(curr.val)
                else:
                    level.appendleft(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if level:
                order.append(list(level))
            odd = not odd
        return order