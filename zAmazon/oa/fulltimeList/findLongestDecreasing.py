'''
https://www.1point3acres.com/bbs/thread-972668-1-1.html

given the segement structure of a process as a linked list
find the longest sub-list which has the segment sizes in non-increasing order

'''

class Node:
    def __init__(self,val=None):
        self.next = None
        self.val = val

class solution:
    def findLongestDecreasingNode(self,root:Node):
        head = root
        current = root
        next = current.next

        maxLength = 1
        curLen = 1

        maxHead = root
        maxEndNode = root
        # endNode = root

        while next:
            if next.val <= current.val:
                curLen += 1
                # endNode = next
                current = next
                next = next.next
            else:
                if curLen > maxLength:
                    maxLength = curLen
                    maxHead = head
                    maxEndNode = current
                head = next
                curLen = 1
                current = head
                next = current.next

        if curLen > maxLength :
            maxHead = head
            maxEndNode = current

        maxEndNode.next = None
        return maxHead

# node1 = Node(4)
# node2 = Node(2)
# node3 = Node(1)
# node4 = Node(3)
# node5 = Node(2)
# node6 = Node(1)
# node1.next  = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
# node5.next = node6
# node6.next = None


node1 = Node(2)
node2 = Node(5)
node3 = Node(4)
node4 = Node(4)
node5 = Node(5)
# node6 = Node(1)
node1.next  = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = None
# node6.next = None
sol = solution()
head = sol.findLongestDecreasingNode(node1)
while head:
    print(head.val)
    head = head.next


