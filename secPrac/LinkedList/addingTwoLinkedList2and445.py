class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        curr = dummy
        carry = 0
        # 精美的写法
        while l1 or l2 or carry != 0:
            if l1:
                num1 = l1.val
                l1 = l1.next
            else:
                num2 = 0
            if l2:
                num2 = l2.val
                l2 = l2.next
            else:
                num2 = 0

            sum = num1 + num2 + carry
            carry = sum // 10
            curr.next =  ListNode(sum % 10)
            curr = curr.next

        return dummy.next

    # 正向输出， 那就用stack当辅助数组来做
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        res = None
        carry = 0
        while stack1 or stack2 or carry != 0:
            num1 = stack1.pop() if stack1 else 0
            num2 = stack2.pop() if stack2 else 0
            cur_sum = num1 + num2 + carry
            carry = cur_sum // 10
            cur_sum %= 10
            cur_node = ListNode(cur_sum)
            cur_node.next = res
            res = cur_node
        return res