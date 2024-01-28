import heapq

from LinkedList import List
from LinkedList.List import ListNode

'''
经典java做法 python化'''
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode(0)
        curr = head
        pq = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(pq,(lists[i].val, i))

        while pq:
            val,i = heapq.heappop(pq)
            curr.next = ListNode(val)
            curr = curr.next
            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(pq,lists[i])
                lists[i] = lists[i].next

        return head.next

    # have not test yet , 字节面经
    def mergeKArrays(self, arrays: List[List[int]]) -> List[int]:
        res = []
        pq = []
        for i in range(len(arrays)):
            if arrays[i]:
                heapq.heappush(pq,(arrays[i][0], i, 0))

        while pq:
            val,array_index,pos_index = heapq.heappop(pq)
            res.append(val)
            new_pos = pos_index + 1
            if arrays[array_index][new_pos]:
                heapq.heappush(pq,(arrays[array_index][new_pos], array_index, new_pos))

        return res