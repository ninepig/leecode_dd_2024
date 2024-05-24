class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    '''
    remove duplicate and keep original
    12334 --> 1234
    '''
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # if head is None or head.next is None:
        #     return  head
        # dummy = ListNode(-1)
        # dummy.next = head
        # cur = dummy
        # while cur.next and cur.next.next :
        #     if cur.next.val == cur.next.next.val:
        #         cur.next = cur.next.n
        if head == None:
            return  head
        cur = head

        while cur:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
     '''
     12334
     124
     因为可能要移动头节点 所以要用dummy
     '''
    def deleteDuplicatesTotally(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return  head
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        while cur.next and cur.next.next :
            if cur.next.val == cur.next.next.val:
                temp = cur.next
                while temp.next and temp.next.next and temp.next.val == temp.next.next.val:
                    temp = temp.next
                # remove 操作永远是指向下一个点,这样可以是移除
                cur.next = temp.next
            else:
                cur = cur.next

        return dummy.next