
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy_dict = dict()
        curr = head
        ## 把所有node都创建一遍 放入dict之中
        while curr:
            copy_node = Node(curr.val, None, None)
            copy_dict[curr] = copy_node
            curr = curr.next

        curr = head

        while curr:
            ## 遍历一次, 把next 以及 random都从dict之中找到.同时赋值, curr.next表示从dict之中寻找
            if curr.next:
                copy_dict[curr].next = copy_node[curr.next]
            if curr.random:
                copy_dict[curr].random = copy_node[curr.random]

            curr = curr.next

        return copy_dict[head]

    def copyRandomList2(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy_dict = dict()
        curr = head

        while curr:
            copy_node = Node(curr.val,None,None)
            copy_dict[curr] = copy_node
            curr = curr.next

        curr = head

        while curr:
            if curr.next:
                copy_dict[curr].next = copy_node[curr.next] # find deep copied list
            if curr.random:
                copy_dict[curr].random = copy_node[curr.random]
            curr = curr.next
        
        return copy_dict[head]
