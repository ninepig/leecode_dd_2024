'''想明白了就没那么难了

这道题的具体解题步骤如下：

先使用哑节点 dummy_head 构造一个指向 head 的指针，避免找不到需要反转的链表区间的前一个节点。使用变量 index 记录当前元素的序号。
使用两个指针 cur、tail 分别表示链表中待反转区间的首尾节点。初始 cur 赋值为 dummy_head，tail 赋值为 dummy_head.next，也就是 head。
将 tail 向右移动，每移动一步，就领 index 加 1。
当 index % k != 0 时，直接将 tail 向右移动，直到移动到当前待反转区间的结尾位置。
当 index % k == 0 时，说明 tail 已经移动到了当前待反转区间的结尾位置，此时调用 cur = self.reverse(cur, tail.next) ，将待反转区间进行反转，并返回反转后区间的起始节点赋值给当前反转区间的首节点 cur。然后将 tail 移动到 cur 的下一个节点。
最后返回新的头节点 dummy_head.next。
关于 def reverse(self, head, tail): 方法这里也说下具体步骤：

head 代表当前待反转区间的第一个节点的前一个节点，tail 代表当前待反转区间的最后一个节点的后一个节点。
先用 first 保存一下待反转区间的第一个节点（反转之后为区间的尾节点），方便反转之后进行连接。
我们使用两个指针 cur 和 pre 进行迭代。pre 指向 cur 前一个节点位置，即 pre 指向需要反转节点的前一个节点，cur 指向需要反转的节点。初始时，pre 指向待反转区间的第一个节点的前一个节点 head，cur 指向待反转区间的第一个节点，即 pre.next。
当当前节点 cur 不等于 tail 时，将 pre 和 cur 的前后指针进行交换，指针更替顺序为：
使用 next 指针保存当前节点 cur 的后一个节点，即 next = cur.next；
断开当前节点 cur 的后一节点链接，将 cur 的 next 指针指向前一节点 pre，即 cur.next = pre；
pre 向前移动一步，移动到 cur 位置，即 pre = cur；
cur 向前移动一步，移动到之前 next 指针保存的位置，即 cur = next。
继续执行第 4 步中的 1、2、3、4步。
最后等到 cur 遍历到链表末尾（即 cur == tail）时，令「当前待反转区间的第一个节点的前一个节点」指向「反转区间后的头节点」 ，即 head.next = pre。令「待反转区间的第一个节点（反转之后为区间的尾节点）」指向「待反转分区间的最后一个节点的后一个节点」，即 first.next = tail。
最后返回新的头节点 dummy_head.next。
'''

class Solution:
    def reverse(self, head, tail):
        pre = head
        cur = pre.next
        first = cur
        while cur != tail:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        head.next = pre
        first.next = tail
        return first

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy_head = ListNode(0)
        dummy_head.next = head
        cur = dummy_head
        tail = dummy_head.next
        index = 0
        while tail:
            index += 1
            if index % k == 0:
                cur = self.reverse(cur, tail.next)
                tail = cur.next
            else:
                tail = tail.next
        return dummy_head.next