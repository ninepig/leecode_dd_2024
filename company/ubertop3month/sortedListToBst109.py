# https://leetcode.cn/problems/convert-sorted-list-to-binary-search-tree/solutions/11235/kuai-man-zhi-zhen-zhao-zhong-dian-by-powcai

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def findmid(head, tail):
            slow = head
            fast = head
            while fast != tail and fast.next != tail:
                slow = slow.next
                fast = fast.next.next
            return slow

        def helper(head, tail):
            if head == tail: return
            node = findmid(head, tail)
            root = TreeNode(node.val)
            root.left = helper(head, node)
            root.right = helper(node.next, tail)
            return root

        return helper(head, None)

