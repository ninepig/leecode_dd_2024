"""
# Definition for a Node.

"""
import collections


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

'''
经典level order'''
class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return root
        queue = collections.deque()
        queue.append(root)
        while queue:
            size = len(queue)
            for i in range(size):
                cur = queue.popleft()
                if i != size -1 :
                    # 链接右侧结点, 是queue的头部 ,这个题画图就清晰很多
                    cur.next = queue[0]
                if  cur.left:
                    queue.append(cur.left)
                if  cur.right:
                    queue.append(cur.right)
        return root