from secPrac.LinkedList import ListNode


class Solution:
    ## 画图 需要做到倒背如流
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.ext = pre
            pre = cur
            cur = tmp

        return pre

    #https://xiaoqingdu.github.io/2021/05/31/%E9%80%92%E5%BD%92%E5%8F%8D%E8%BD%AC%E9%93%BE%E8%A1%A8/
    # clear explain
    def reverseListRec(self, head: ListNode) -> ListNode:
        if not head or not head.next :
            return head
        new_head = self.reverseListRec(head.next)
        new_head.next.next = head #
        new_head.next = None

        return new_head