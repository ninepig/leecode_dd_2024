class Solution:
    '''
    遍历链表，利用哈希表，以 旧节点: 新节点 为映射关系，将节点关系存储下来。
再次遍历链表，将新链表的 next 和 random 指针设置好。
    '''
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head : return  head
        new_dict = dict()
        cur = head
        while cur:
            copy_node = ListNode(-1)
            new_dict[cur] = copy_node
            cur = cur.next

        cur = head
        while cur:
            if cur.next:
                new_dict[cur].next = new_dict[cur.next]
            if cur.random:
                new_dict[cur].random = new_dict[cur.random]
            cur = cur.next

        return new_dict[head]
