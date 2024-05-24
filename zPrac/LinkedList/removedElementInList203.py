from firstRount.LinkedList.List import ListNode


class Solution:
    # 比答案的好
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummyNode = ListNode(-1)
        dummyNode.next = head
        cur = dummyNode
        while cur.next:
            if cur.next.val == val:
                cur = cur.next.next
            else:
                cur = cur.next

        return dummyNode.next


    def removeElementsAnswer(self, head: ListNode, val: int) -> ListNode:
        newHead = ListNode(0, head)
        newHead.next = head

        prev, curr = newHead, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return newHead.next