'''
这题不会改变头节点 所以可以不需要dummyNode
非常优雅 清晰的写法
'''

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not  head.next or not head.next.next :
            return head

        evenHead= head.next
        odd, even = head, evenHead
        isOdd = True

        cur = head.next.next

        while cur:
            if isOdd:
                odd.next = cur
                odd = cur
            else:
                even.next = cur
                even = cur
            isOdd = not isOdd
            cur = cur.next

        odd.next = evenHead
        even.next = None

        return head
