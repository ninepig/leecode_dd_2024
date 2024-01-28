class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        hashset = set()
        cur = head
        while cur:
            if cur in hashset:
                return True
            hashset.add(cur)
            cur = cur.next
        return false


    def hasCycle2(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        slow = head
        fast = head.next

        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next

        return True
    '''
    思路 1：快慢指针（Floyd 判圈算法）
利用两个指针，一个慢指针 slow 每次前进一步，快指针 fast 每次前进两步（两步或多步效果是等价的）。
如果两个指针在链表头节点以外的某一节点相遇（即相等）了，那么说明链表有环。
否则，如果（快指针）到达了某个没有后继指针的节点时，那么说明没环。
如果有环，则再定义一个指针 ans，和慢指针一起每次移动一步，两个指针相遇的位置即为入口节点。
    '''
    def detectCycle(self, head: ListNode) -> ListNode:
        fast, slow = head, head
        while True:
            if not fast or not fast.next:
                return None
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break

        ans = head
        while ans != slow:
            ans, slow = ans.next, slow.next
        return ans