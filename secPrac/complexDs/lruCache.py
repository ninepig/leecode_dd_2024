'''
LRU的逻辑
0 核心是一个双向链表， capacity head tail dict 4个变量
1 利用一个dict 来保存 key---》node 的mapping
2 每次put 元素，要把元素插入在头部后面，然后删除原来的位置 /如果超过capactity， 我们把尾部的元素删除,再放到头部即可
3 每次get元素，都要把元素插在头部后面，同时删除原来的位置

这个算是简单数据结构的复杂应用。只能说多练习多练习多练习
'''

class double_linked_list:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.pre  = None
        self.next = None

class LRUCache:
    def __init__(self,capacity:int):
        self.dict = {}
        self.capacity = capacity
        self.head = double_linked_list(0,0)
        self.tail = double_linked_list(0,0)
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self,key:int):
        if key not in self.dict:
            return -1
        else:
            node = self.dict[key]
            self.remove_from_list(node)
            self.insert_to_head(node)
            return node.value

    def put(self,key:int,value:int):
        if key in self.dict:
            node = self.dict[key]
            self.remove_from_list(node)
            self.insert_to_head(node)
            node.value = value #update value
        else:
            if len(dict) >= self.capacity:
                self.remove_from_tail()
            node = double_linked_list(key,value)
            self.dict[key] = node
            self.insert_to_head(node)

    def remove_from_list(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    ## 基本的画图
    def insert_to_head(self, node):
        head_next = self.head.next
        self.head.next = node
        node.pre = self.head
        node.next = head_next
        head_next.pre = node

    def remove_from_tail(self):
        if len(self.dict) == 0 : return ## nothing to delete
        tail_node = self.tail.pre
        del self.dict[tail_node.key]
        self.remove_from_list(tail_node)
