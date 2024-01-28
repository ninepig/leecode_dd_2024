class Solution:
    def reorderList(self, head: ListNode) -> None:
        if head is None : return  head
        vect = []
        cur = head
        while cur:
            vect.append(cur)
            cur = cur.next

        left , right = 0 , len(vect) - 1

        while left < right:
            vect[left].next = vect[right]
            left += 1
            if left == right :
                break
            # 把左侧第二个 attach到最后一个上, 交叉链接
            vect[right].next = vect[left]
            right -= 1
        vect[left].next = None
