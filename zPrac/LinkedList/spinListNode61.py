class Solution:
    ## 本质rotate 找新的头

    # https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0061.%20%E6%97%8B%E8%BD%AC%E9%93%BE%E8%A1%A8.md
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k <= 0 or not head or not head.next:
            return head

        size = 1
        curr = head

        while curr.next:
            size += 1
            curr = curr.next

        k %= size

        # connect head  to be a loop
        curr.next = head
        # 1 2 3 4 5
        # 5 1 2 3 4  n=1
        # 4 5 1 2 3  n= 2
        # 3 4 5 1 2   n =3
        # 2 3 4 5 1   n =4
        # find n - k node from end, move right to get new head
        #  n - k % n 的位置
        cut = size - k
        while cut > 0:
            curr = curr.next
            cut -= 1

        newHead = curr.next
        curr.next = None

        return newHead
