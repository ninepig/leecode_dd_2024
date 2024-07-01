class Solution:
    ## 脑经急转弯, 这个题 关键是要想明白
    ## 如果A 和 b 有相交 那他们最后相交长度(k) 肯定是一致的 ,而且A 和 b都会存在
    ## 所以 如果我们把A放到b后面 同时b放到a后面 这样两个list 从头开始走, 如果有相交 肯定找到相遇节点
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        dummyA = headA
        dummyB = headB
        while dummyA != dummyB:
            dummyA = dummyA.next if dummyA else headB
            dummyB = dummyB.next if dummyB else headA

        return dummyA
