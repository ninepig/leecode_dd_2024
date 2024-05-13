from typing import Optional


'''
链表基本操作
dummy node 

'''
class ListNode:
    def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list2 :
            return list1
        if not list1:
            return list2
        ## dummy的写法这样比较好
        dummy = ListNode()
        head = dummy
        while list1 and list2:
            if list1.val >= list2.val:
                head.next = list2
                list2 = list2.next
            else:
                head.next = list1
                list1 = list1.next
            head = head.next

        ## 漏了这一步
        if list1:
            head.next = list1
        if list2 :
            head.next = list2

        return dummy.next

