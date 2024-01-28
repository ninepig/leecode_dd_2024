from LinkedList.List import ListNode


class Solution:
    '''
    https://camo.githubusercontent.com/796c8c2b5cc744dcf0176eeee0e1d619305eb65d60f306c72e9d33091650266f/68747470733a2f2f7163646e2e69746368617267652e636e2f696d616765732f32303232303131313133333633392e706e67
    看了这个图就不会忘记怎么做了
    pre 是 cur 的pre节点
    当反转过后 cur是pre后面那个节点了
    '''
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None : return head
        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        return pre

    def reverseListRecur(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head

    def reverseListBetween(self,head:list , left : int , right : int):
        if head is None or head.next is None:
            return  head
        dummy = ListNode(-1)
        dummy.next =head
        cur = dummy
        reverse_index = 0

        while cur.next and reverse_index < left:
            cur = cur.next
            reverse_index += 1

        reverse_pre = cur
        pre = reverse_pre
        cur = reverse_pre.next
        while cur and reverse_index < right:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
            reverse_index += 1

        # 链接反转以后的
        # cur 相当于 反转后尾部节点的下一个 pre相当于尾部节点
        # 123456  ---> 154326
        # reverse_pre =1
        # cur = 6 pre = 2
        reverse_pre.next.next = cur
        reverse_pre.next = pre

        return head


class Solution:
    ## 不太懂这个题
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == 1:
            return self.reverseN(head, right)

        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head

    def reverseN(self, head, n):
        if n == 1:
            return head
        last = self.reverseN(head.next, n - 1)
        next = head.next.next
        head.next.next = head
        head.next = next
        return last


