# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# l0 -> l1 -> l2-->l3-->ln ---> l0 --> ln ---> l1 -->ln-1
#
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find mid
        # reverse right part
        # connect
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse from mid
        pre = None
        cur = slow
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        # pre is new head
        # connect two list one by one
        while pre:
            t = pre.next
            pre.next = cur.next
            cur.next = pre
            cur = cur.next
            pre = t

    # 用数组这个方法也比较好
    def reorderListUsingArray(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        vec = []
        node = head
        while node:
            vec.append(node)
            node = node.next

        left, right = 0, len(vec) - 1
        while left < right:
            vec[left].next = vec[right]
            left += 1
            if left == right:
                break
            vec[right].next = vec[left]
            right -= 1
        vec[left].next = None
