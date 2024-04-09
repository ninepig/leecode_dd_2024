# // At DoorDash, menus are updated daily even hourly to keep them up-to-date. Each menu can be regarded as a tree. When the merchant sends us the latest menu, can we calculate how many nodes has changed?
#https://leetcode.com/discuss/interview-question/1265810/Doordash-PhoneScreen
# // Assume each Node structure is as below:
#
# // class Node {
# // String key;
# // int value;
# // boolean active;
# // List children;
# // }
# // Assume there are no duplicate nodes with the same key.
#
# // Output: Return the number of changed nodes in the tree.
#
# // Example 1
# // Existing Menu in our system:
#
# // Existing tree
# // a(1, T)
# // /
# // b(2, T) c(3, T)
# // / \
# // d(4, T) e(5, T) f(6, T)
# // ( Legend - a(1, T) a is the key, 1 is the value, T is True for active status )
#
# // New Menu sent by the Merchant:
#
# // New tree
# // a(1, T)
# //
# // c(3, F)
# //
# // f(66, T)
# // Expected Answer: 5 Explanation: Node b, Node d, Node e are automatically set to inactive. The active status of Node c and the value of Node f changed as well.
#
# // Example 2
# // Existing Menu in our system:
#
# // Existing tree
# // a(1, T)
# // /
# // b(2, T) c(3, T)
# // / \
# // d(4, T) e(5, T) g(7, T)
# // New Menu sent by the Merchant:
#
# // New tree
# // a(1, T)
# // /
# // b(2, T) c(3, T)
# // / | \
# // d(4, T)e(5, T)f(6, T) g(7, F)
# // Expected Answer: 2 Explanation: Node f is a newly-added node. Node g changed from Active to inactive


class menuNode:
    def __init__(self,key:str,value:int,status:bool):
        self.key = key
        self.value = value
        self.status = status
        self.children = []

class solution:

    def checkDifference(self, old_root: menuNode, new_root: menuNode):
        if not old_root and not new_root:
            return 0
        if not old_root:
            return self.countTree(new_root)
        if not new_root:
            return self.countTree(old_root)
        if old_root.key != new_root.key:
            return self.countTree(old_root) + self.countTree(new_root)
        count = 0
        # if old_root.value != new_root.value:
        #     count += 1
        ## 如果要有status 这个的字段 我们只要判断这里就行了。 这个字段只有在key 存在的时候才需要判断
        if old_root.value != new_root.value or old_root.status != new_root.status:
            count += 1

        ## get all new tree's key:childrenNode dict
        new_tree_key_child_dict = {c.key: c for c in new_root.children}  ##用map 大括号包裹 就是map 用中括号包裹是dict
        for old_child in old_root.children:
            ## 这个方法非常非常优雅
            count += self.checkDifference(old_child, new_tree_key_child_dict.pop(old_child.key, None))

        ## bugbugbugbugbug !! 没加values
        for rest_child in new_tree_key_child_dict.values():  ## bug here, that is node / not key
            count += self.countTree(rest_child)

        return count

    def countTree(self, cur_node: menuNode):
        if not cur_node:
            return 0
        count = 1
        for child in cur_node.children:
            count += self.countTree(child)

        return count

    def countMenuNode(self,menu_node:menuNode):
        pass
