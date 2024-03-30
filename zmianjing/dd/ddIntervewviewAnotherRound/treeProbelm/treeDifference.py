class ddNode(object):
    def __init__(self,key:int,value:int):
        self.key = key
        self.value = value
        self.children = []

    def __str__(self):
        return "key" + str(self.key) + "value" + str(self.value)


'''
经典树比较题
key value children 
https://www.1point3acres.com/bbs/thread-1052303-1-1.html
https://www.1point3acres.com/bbs/thread-1045497-1-1.html
详见题意
'''
class solution:
    def getDifference(self, old_root : ddNode, new_root: ddNode):
        '''
        ## need clearilfy
        0 key is unique
        1 if key is same , value is same ---> same node
        2 if key is same value is difference --> difference + 1
        3 if key is different, all node(including children) are different
        this is very important
        '''
        if not old_root and not new_root:
            # print("not old, not new ")
            return 0 ## same null tree
        elif not old_root : ## only old tree is empty
            # print("not old")
            return self.get_node_count(new_root)
        elif not new_root:
            # print("not new ")
            return self.get_node_count(old_root)
        elif old_root.key != new_root.key : # if key not same, two tree are totally different
            # print("not same key")
            return self.get_node_count(new_root) + self.get_node_count(old_root)

        cur_diff = 0
        # print(old_root)
        # print(new_root)
        if old_root.value != new_root.value:
            cur_diff += 1
        # print("cur_diff",cur_diff)
        ## cal the children
        new_tree_children = {c.key : c for c in new_root.children} ## form new tree's children's dict

        for old_c in old_root.children:
            ## we use old children's key to find children with same key in new_tree_children
            ## meanwhile , we pop that children node from dict.
            ## if that node can not be found, we give that NONE
            cur_diff += self.getDifference(old_c,new_tree_children.pop(old_c.key,None))
        for rest_new_chid in new_tree_children.values():
            cur_diff += self.get_node_count(rest_new_chid)

        return cur_diff

    def get_node_count(self, node:ddNode):

        if not node:
            return 0
        count = 1
        for child in node.children:
            count += self.get_node_count(child)

        return count


## key has to be different, other wise will cause problem

test = solution()
node1 = ddNode(5,3)
node2 = ddNode(4,2)
node3 = ddNode(6,3)
node1.children.append(node2)
node1.children.append(node3)
# print(test.get_node_count(node1))

node4 = ddNode(5,4)
node5 = ddNode(4,2)
node6 = ddNode(6,4)

node4.children.append(node5)
node4.children.append(node6)

print(test.getDifference(node4,node1))
