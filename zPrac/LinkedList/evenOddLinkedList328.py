from LinkedList.List import ListNode


class Solution:
    '''必须画图'''
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next or not head.next.next:
            return head

        oddHead = head
        evenHead = head.next
        cur = head.next.next
        isOdd = True
        while cur:
            if isOdd:
                oddHead.next = cur
                oddHead = cur
            else:
                evenHead.next = cur
                evenHead = cur
            isOdd = not isOdd
            cur = cur.next

        oddHead.next = evenHead #连接2个节点
        evenHead.next = None # even的尾部为空

        return head




