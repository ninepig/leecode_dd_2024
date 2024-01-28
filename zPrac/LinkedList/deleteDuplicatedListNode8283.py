from zPrac.LinkedList import ListNode


class Solution:
    # 去掉重复的元素,保留一个
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head :
            return None
        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next # 删除下一个节点 再比较
            else:
                cur = cur.next

        return head

    #不保留
    def deleteDuplicatesNoDuplicated(self, head: ListNode) -> ListNode:
        dummyNode = ListNode(0)
        dummyNode.next = head
        cur = dummyNode

        # 下一个 以及下下个都不为空
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val : # 如果相等
                temp = cur.next
                while temp and temp.next and temp.val == temp.next.val: # 往后搜
                    temp = temp.next
                cur.next = temp.next # 找到下一个不等的, 删掉中间所有相等的, 这时候dummy的作用就有了
            else:
                cur = cur.next

        return dummyNode.next