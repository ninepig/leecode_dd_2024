from LinkedList.List import ListNode


class Solution:
    '''
    # Remove to left  pos pre_reverse
    # reverse from left to right
    # connect  pre_revese to newLeftHead
    # connect new right to tail
    '''
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head : return head
        dummyNode = ListNode(0)
        dummyNode.next = head
        cur_start_node = dummyNode
        index = 1  # 这里index 为1 是以1为base,同时我们要找到 < left, 我们有一个dummyNode
        # find  location previous left
        while cur_start_node and index < left:
            cur_start_node = cur_start_node.next
            index += 1

        pre = cur_start_node
        cur = cur_start_node.next


        # reverse to right
        while cur and index <= right:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
            index += 1

        # connect , we still have point to previous of previous left node

        cur_start_node.next.next  = cur # to previous tail
        cur_start_node.next = pre # to new head

        return dummyNode.next
