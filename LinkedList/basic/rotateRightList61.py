'''
我们可以将链表先连成环，然后将链表在指定位置断开。

先遍历一遍，求出链表节点个数 n。注意到 k 可能很大，我们只需将链表右移 k % n 个位置即可。

第二次遍历到 n - k % n 的位置，记录下断开后新链表头节点位置，再将其断开并返回新的头节点。

其实就是脑经急转弯 想明白就很简单了

'''

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or not head or not head.next:
            return head
        curr = head
        count = 1
        while curr.next:
            count += 1
            curr = curr.next
        cut = count - k % count
        curr.next = head
        while cut:
            curr = curr.next
            cut -= 1
        newHead = curr.next
        curr.next = None
        return newHead