
class TreeNode:
    def __init__(self,value : int = 0):
        self.val = value
        self.left = TreeNode()
        self.right = TreeNode()

'''
bfs 稳得一笔
'''
class solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res =[]
        queue = [root]
        while queue:
            size = len(queue)
            for i in range(size):
                cur = queue.pop(0)
                if cur.left :
                    queue.append(cur.left)
                if cur.right :
                    queue.append(cur.right)
                if i == size - 1 :
                    res.append(cur.val)

        return res


