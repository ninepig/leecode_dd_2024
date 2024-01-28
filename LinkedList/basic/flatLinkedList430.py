class Solution:
    def dfs(self, node: 'Node'):
        # 找到链表的尾节点或 child 链表不为空的节点
        while node.next and not node.child:
            node = node.next
        tail = None
        if node.child:
            # 如果 child 链表不为空，将 child 链表扁平化
            tail = self.dfs(node.child)

            # 将扁平化的 child 链表链接在该节点之后
            temp = node.next
            node.next = node.child
            node.next.prev = node
            node.child = None
            tail.next = temp
            if temp:
                temp.prev = tail
            # 链接之后，从 child 链表的尾节点继续向后处理链表
            return self.dfs(tail)
        # child 链表为空，则该节点是尾节点，直接返回
        return node

    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        self.dfs(head)
        return head


def flatten(self, head: 'Node') -> 'Node':
    temp = head

    stack = []

    while head:
        if head.child:
            if head.next:
                stack.append(head.next)
            head.next = head.child
            head.next.prev = head
            head.child = None
        elif not head.next and stack:
            head.next = stack.pop()
            head.next.prev = head

        head = head.next

    return temp


# /*
# // Definition for a Node.
# class Node {
#     public int val;
#     public Node prev;
#     public Node next;
#     public Node child;
# };
# */
#
# class Solution {
#     public Node flatten(Node head) {
#         if( head == null) return head;
# 	// Pointer
#         Node p = head;
#         while( p!= null) {
#             /* CASE 1: if no child, proceed */
#             if( p.child == null ) {
#                 p = p.next;
#                 continue;
#             }
#             /* CASE 2: got child, find the tail of the child and link it to p.next */
#             Node temp = p.child;
#             // Find the tail of the child
#             while( temp.next != null )
#                 temp = temp.next;
#             // Connect tail with p.next, if it is not null
#             temp.next = p.next;
#             if( p.next != null )  p.next.prev = temp;
#             // Connect p with p.child, and remove p.child
#             p.next = p.child;
#             p.child.prev = p;
#             p.child = null;
#         }
#         return head;
#     }
# }