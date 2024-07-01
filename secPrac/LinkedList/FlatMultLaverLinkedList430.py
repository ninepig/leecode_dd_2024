# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        self.dfs(head)
        return head

    # 这个版本比较好理解
    def dfs(self, node):

      while node.next and not node.child:
          node = node.next
      tail = None
      if not node.child:
          tail = self.dfs(node.child) # dfs flat child first
          tmp = node.next # record node.next first
          node.next = node.child
          node.child.pre = node
          node.child = None # connect
          tail.next = tmp
          # connect tail if we can flat child
          if tmp :
              tmp.pre = tail

          self.dfs(tail) # handle flat from tail first
      return node

