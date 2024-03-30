'''
这个题和treedifference应该是一样的 就是多了一个字段
多一次判断

https://www.1point3acres.com/bbs/thread-1049598-1-1.html
感觉这个才是主要的题目

'''

class Node:
    def __init__(self, key, value, isActive):
        self.key = key
        self.value = value
        self.isActive = isActive
        self.children = []

class solution:
    def getDifference(self,new_menu:Node, old_menu:Node):
        '''
        1 if key is not same, oll children node is not same
        2 if key is same, value not same, this node is not same
        3 key same, value same activa flag is same means ---> same node
        '''
        if not new_menu and not old_menu:
            return 0
        elif not new_menu: ## return all count of old menu
            return self.get_all_count(old_menu)
        elif not old_menu:
            return self.get_all_count(new_menu)
        elif old_menu.key != new_menu.key:
            return self.get_all_count(old_menu) + self.get_all_count(new_menu)

        cur_diff = 0
        if old_menu.value != new_menu.value or old_menu.isActive != new_menu.isActive:
            cur_diff += 1

        ## check children node difference
        new_chilrdren_dict = {c.key: c for c in new_menu.children}
        ## we compare same key
        for old_c in old_menu.children:
            cur_diff += self.getDifference(old_c,new_chilrdren_dict.pop(old_c.key,None))

        for remain_new_c in new_chilrdren_dict.values():
            cur_diff += self.get_all_count(remain_new_c) ## we need compute the count number since key is different

        return cur_diff



    def get_all_count(self, node):
        if not node:
            return 0
        count = 1
        for child in node.children:
            count += self.get_all_count(child)

        return count


test = solution()
a = Node('a', 1, True)
b = Node('b', 2, True)
c = Node('c', 3, True)
d = Node('d', 4, True)
e = Node('e', 5, True)
g = Node('g', 7, True)
# f = Node('f', 6, True)

a.children = [b, c]
b.children = [d, e]
c.children= [g]
# c.children = [f]

a1 = Node('a', 1, True)
b1 = Node('b', 2, True)
c1 = Node('c', 3, True)
d1 = Node('d', 4, True)
e1 = Node('e', 5, True)
f1 = Node('f', 6, True)
g1 = Node('g', 7, False)

a1.children = [b1, c1]
b1.children = [d1, e1, f1]
c1.children = [g1]
# a1.children = [c1]
# c1.children = [f1]


print(test.getDifference(a, a1))