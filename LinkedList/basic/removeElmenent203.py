class Solution:
    '''类似双指针移动'''
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head

        pre = dummy
        cur = dummy.next
        while cur :
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next

        return dummy.next