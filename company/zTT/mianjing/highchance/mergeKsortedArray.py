import heapq
from heapq import heapify
from typing import List, Optional


## 数据安全
##  coding都是简单题：第一题是两个数组a, b, 找到满足满足a[i] -b[j] = a[j] -b[i] 条件的i和j。第二题是merge k sorted array
##
## https://www.1point3acres.com/bbs/thread-1065025-1-1.html

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        def push_node(heap, node):
            if node:
                heapq.heappush(heap, (node.val, id(node), node))

        for l in lists:
            push_node(heap, l)

        dummy = ListNode()
        current = dummy

        while heap:
            _, _, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(heap, (node.next.val, id(node.next), node.next))

        return dummy.next


class Solution:
    def mergeSortedArrays(self, arrays):
        pq = []
        for i, arr in enumerate(arrays):
            pq.append((arr[0], i, 0))
        heapq.heapify(pq)

        res = []
        while pq:
            num, i, j = heapq.heappop(pq)
            res.append(num)
            if j + 1 < len(arrays[i]):
                heapq.heappush(pq, (arrays[i][j + 1], i, j + 1))

        return res