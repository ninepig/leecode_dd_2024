class Node:
    def __init__(self,data):
        self.data =data
        self.next = None

class solution:
    def sortedList(self,head:Node):
        if not head :
            return head
        count = [0,0,0] ## intial 0,1,2 's count
        help = head
        ## build array
        while help:
            count[help.data] += 1
            help = help.next

        ## build list based on array
        index = 0
        new_head = head
        while new_head:
            if count[index] == 0:
                index += 1
            else:
                new_head.data = count[index]
                count[index] -= 1
                new_head = new_head.next
        return head


