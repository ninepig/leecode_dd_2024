from secPrac.LinkedList.ListNode import ListNode


class MyLinkedList:

    # head 只是头节点
    # size
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)

    # index is 1 based
    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1
        # count = 0
        # cur = self.head
        # while count < index - 1 :
        #    cur = cur.next
        #    count += 1
        # 用这个 for循环 就不用考虑计数问题, 因为腰跑那么多次 变相计数了. index次
        curr = self.head
        for _ in range(index + 1):
            curr = curr.next
        return curr.val
        # return cur.val

    def addAtHead(self, val: int) -> None:

        # nextAfterHead = self.head.next
        # newNode = ListNode(val)
        # newNode.next = nextAfterHead
        # self.head.next = newNode
        # self.size += 1
        self.addAtIndex(0,val)


    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size,val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index < 0 :
            index = 0

        pre = self.head

        # 用for 循环 跑到 index位置
        for _ in range(index):
            pre = pre.next

        insert_node = ListNode(val)
        insert_node.next = pre.next
        pre.next = insert_node


    def deleteAtIndex(self, index: int) -> None:
        if index <=0 or index > self.size:
            return
        self.size -= 1
        pre = self.head
        for _ in range(index):
            pre = pre.next

        pre.next = pre.next.next



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)