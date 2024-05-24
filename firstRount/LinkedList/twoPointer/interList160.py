'''
这图关键是画图， 最终一定会有交点的


https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0160.%20%E7%9B%B8%E4%BA%A4%E9%93%BE%E8%A1%A8.md
考虑将链表 listA 的末尾拼接上链表 listB，链表 listB 的末尾拼接上链表 listA。

然后使用两个指针 pA 、pB，分别从链表 listA、链表 listB 的头节点开始遍历，如果走到共同的节点，则返回该节点。

否则走到两个链表末尾，返回 None
'''
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None:
            return None
        pA = headA
        pB = headB
        while pA != pB:
            pA = pA.next if pA != None else headB
            pB = pB.next if pB != None else headA
        return pA