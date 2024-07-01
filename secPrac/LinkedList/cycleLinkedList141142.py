class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next: return False
        slow , fast = head, head.next
        while fast:
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next.next # 可能会空指针 有问题

        return False

    # 正确答案比较好, 因为判断了 fast.next
    def hasCycleAnswer(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if fast == None or fast.next == None:
                return False
            slow = slow.next
            fast = fast.next.next

        return True

    def hasCycleSet(self, head: ListNode) -> bool:
        nodeset = set()

        while head:
            if head in nodeset:
                return True
            nodeset.add(head)
            head = head.next
        return False

    # 142 floyd algo
    def detectCycle(self, head: ListNode) -> ListNode:
        fast , slow = head,head
        while True:
            if not fast and not fast.next:
                return None
            slow = slow.next
            fast = fast.next.next
            if slow == fast :
                break
        # we found met node
        ans = head
        while ans != slow:
            ans = ans.next
            slow = slow.next

        return ans