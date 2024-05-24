class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        head = dummy
        carry = 0

        while l1 or l2 or carry:
            if l1 :
                num1 = l1.val
                l1 = l1.next
            else :
                num1 = 0
            if l2 :
                num2 = l2.val
                l2 = l2.next
            else:
                num2 = 0

            sum = num2+ num1 + carry
            carry = sum/10
            curNode = ListNode(sum%10)
            head.next = curNode
            head = head.next

        return dummy.next


    def addTwoNumbersReverse(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = [] , stack2 = []
        while l1 :
            stack1.append(l1.val)
            l1 = l1.next
        while l2 :
            stack2.append(l2.val)
            l2 = l2.next

        res = None
        carry = 0
        while stack2 or stack1 or carry:
            if stack1 :
                num1 = stack1.pop()
            else :
                num1 = 0
            if stack2 :
                num2 = stack2.pop()
            else:
                num2 = 0

            sum = num2 + num1 + carry
            carry = sum / 10
            curNode = ListNode(sum % 10)
            # 反向链接. 因为curNode是后一个节点
            curNode.next = res
            res = curNode

        return res