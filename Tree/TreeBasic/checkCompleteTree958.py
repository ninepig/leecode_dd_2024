import collections
from typing import Optional

from Tree.TreeBasic.TreeNode import TreeNode


'''完全二叉树就是除了最后一层都是2 power n - 1
最后一层必须靠左侧满'''
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root :
            return False

        queue = collections.deque([root])
        is_empty = False
        while queue:
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                if not cur:
                    is_empty = True
                else:
                    if is_empty:
                        return False
                    queue.append(cur.left)
                    queue.append(cur.right)

        return True