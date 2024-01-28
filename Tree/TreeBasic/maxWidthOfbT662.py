import collections
from typing import Optional

from Tree.TreeBasic.TreeNode import TreeNode


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        ans = 0
        queue = collections.deque([[root, 0]])
        while queue:
            #计算当前层最大宽度
            ans = max(ans,queue[-1][1] - queue[0][1] + 1)
            size = len(queue)
            for _ in range(size):
                cur,index = queue.popleft()
                if cur.left :
                    queue.append([cur.left, 2*index + 1])
                if cur.right :
                    queue.append([cur.right, 2 * index + 2])

        return ans