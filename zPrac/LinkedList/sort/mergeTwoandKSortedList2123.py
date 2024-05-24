import heapq

from firstRount.LinkedList import List
from firstRount.LinkedList.List import ListNode


class Solution:
    # dummy Node 的使用  这里非常有意思
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(-1)
        curr = dummyNode
        while list1 and list1:
            if list1.val <= list2.val:
                curr.next = list1.val
                list1 = list1.next
            else:
                curr.next = list2.val
                list2 = list2.next
            curr = curr.next

        curr.next = list1 if list1 is not None else list2

        return dummyNode.next

    ##heapq的用法不对
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        sorted_list = []
        dummy = ListNode(-1)
        res_head = dummy
        # put k head into heap
        for list in lists:
            sorted_list.append(list[0])
        heapq.heapify(sorted_list) # 不一定需要初始化

        while sorted_list:
            tmp_node = heapq.heappop(sorted_list)
            res_head.next = tmp_node
            if tmp_node.next:
                heapq.heappush(tmp_node.next)
            res_head = res_head.next

        return dummy.next


    # 非常优雅
    def mergeKListsSecond(self, lists: List[ListNode]) -> ListNode:
        sorted_list = []
        dummy = ListNode(-1)
        res_head = dummy

        # into array and heap
        for i in range(len(lists)):
            if lists[i]:
                # insert head and index
                heapq.heappush(sorted_list,)
                lists[i] = lists[i].next # move head pointer

        while sorted_list:
            val,idx = heapq.heappop(sorted_list)

            res_head.next = ListNode(val)
            res_head = res_head.next

            if lists[idx]: # 如果这个list的节点不为空,则我们加入queue
                heapq.heappush(sorted_list,(lists[idx].val, idx))
                lists[idx] = lists[idx].next

        return dummy.next



    def mergeKarrays(self, arrays: List[List[int]]) -> List[int]:
        sortedList = []
        res = []

        # put first element in each array into heaq
        for i in range(len(arrays)):
            if arrays[i][0]:
                heapq.heappush(sortedList,(arrays[i][0],i,0))

        while sortedList:
            val,x,y = heapq.heappop(sortedList)

            res.append(val)

            if y + 1 < len(arrays[x]):
                heapq.heappush(sortedList,(arrays[x][y],x,y + 1))

        return res



