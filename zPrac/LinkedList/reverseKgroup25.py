# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from firstRount.LinkedList.List import ListNode


class Solution:
    # head here is dummy head pointor reverse head , we need this to connect reversed head
    # tail here is the pointer after tail (before reverse head)
    # 1 2 3 4 5 6 , head is 1  6 is tail we want to reverse 2---5
    # 1 5 4 3 2 6
    def reverse(self, head, tail):
        pre = head
        cur = head.next
        first = cur

        while cur != tail:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        head.next = pre # new head conenction to tail pointer before head(before reverse)
        first.next = tail # point to list after tail (before reverse)
        return first # new tail in this question , we need iterator


    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummyNode = ListNode(-1)
        dummyNode.next = head
        cur = dummyNode
        tail = dummyNode.next
        index = 0
        while tail:
            index += 1
            if index % k == 0:
                cur = self.reverse(cur, tail.next) # reverse k group, input dummy head , pointer after tail
                tail = cur.next
            # has K group
            else:
                tail = tail.next

        return dummyNode.next