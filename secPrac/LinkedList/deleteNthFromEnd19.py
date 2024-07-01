class Solution:
    ## 快慢指针
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        fast = head
        slow = dummy
        while n > 0:
            fast = fast.next
            n -= 1

        ## we found fast
        while fast :
            fast = fast.next
            slow = slow.next

        slow.next =slow.next.next # remove next of slow , if slow start from dummy, slow's next is our target

        return dummy.next 