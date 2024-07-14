'''
https://leetcode.com/discuss/interview-question/1528907/doordash-phone-creen
At DoorDash, menus are updated daily even hourly to keep them up-to-date. Each menu can be regarded as a tree. When the merchant sends us the latest menu, can we calculate
how many nodes have changed/added/deleted?

Assume each Node structure is as below:

class Node {
        String key;
        int value;
        List children;
}

Assume there are no duplicate nodes with the same key.

Output: Return the number of changed nodes in the tree.

Existing tree
               a(1)
            /
         b(2)      c(3)
        /     \
      d(4)    e(5)      f(6)

New tree
            a(1)

               c(3)

                   f(66)

a(1) a is the key, 1 is the value
For example, there are a total of 4 changed nodes. Node b, Node d, Node e are automatically set to inactive. The value of Node f changed as well.

Existing tree
            a(1)
          /
        b(2     c(3)
      /       \
  d(4)      e(5)      g(7)

New tree
                a(1)
            /
         b(2)         h(8)
      /    |   \
e(5)   d(4)   f(6)       g(7)

There are a total of 5 changed nodes. Node f is a newly-added node. c(3) and old g(7) are deactivated and h(8) and g(7) are newly added nodes

followup print out the changes
炒
'''

class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.children = []

    def __str__(self):
        return "key" + str(self.key) + "value" + str(self.value)
class Solution:
    def checkDifference(self,old_root:Node,new_root:Node):
        if not old_root and not new_root :
            return 0
        if not old_root :
            return self.countTree(new_root)
        if not new_root:
            return  self.countTree(old_root)
        if old_root.key != new_root.key:
            return self.countTree(old_root) + self.countTree(new_root)
        count = 0
        if old_root.value != new_root.value:
            count += 1
        ## get all new tree's key:childrenNode dict
        new_tree_key_child_dict ={c.key:c for c in new_root.children} ##用map 大括号包裹 就是map 用中括号包裹是dict
        for old_child in old_root.children:
            ## 这个方法非常非常优雅
            count += self.checkDifference(old_child,new_tree_key_child_dict.pop(old_child.key,None))

        ## bugbugbugbugbug !! 没加values
        for rest_child in new_tree_key_child_dict.values():  ## bug here, that is node / not key
            count += self.countTree(rest_child)

        return count

    def countTree(self,cur_node:Node):
        if not cur_node:
            return 0
        count = 1
        for child in cur_node.children:
            count += self.countTree(child)

        return count

    def checkDifferencePath(self, old_root: Node, new_root: Node):
        if not old_root and not new_root:
            return 0,[]
        if not old_root:
            return self.countTreePath(new_root)
        if not new_root:
            return self.countTreePath(old_root)
        if old_root.key != new_root.key:
            return self.countTreePath(old_root) + self.countTreePath(new_root)
        count = 0
        path = []
        if old_root.value != new_root.value:
            count += 1
        ## get all new tree's key:childrenNode dict
        new_tree_key_child_dict = {c.key: c for c in new_root.children}  ##用map 大括号包裹 就是map 用中括号包裹是dict
        for old_child in old_root.children:
            ## 这个方法非常非常优雅
            child_diff , child_path = self.checkDifferencePath(old_child, new_tree_key_child_dict.pop(old_child.key, None))
            count += child_diff
            path += child_path
        ## bugbugbugbugbug !! 没加values
        for rest_child in new_tree_key_child_dict.values():  ## bug here, that is node / not key
            child_diff,child_path = self.countTreePath(rest_child)
            count += child_diff
            path += child_path

        return count,path

    def countTreePath(self, cur_node: Node):
        if not cur_node:
            return 0
        diff_list = []
        count = 1
        diff_list.append(cur_node)
        for child in cur_node.children:
            child_count,children_path = self.countTreePath(child)
            count += child_count
            diff_list += children_path
        return count,diff_list


## follow up, print all difference

# Existing tree
#                a(1)
#             /
#          b(2)      c(3)
#         /     \
#       d(4)    e(5)      f(6)
#
# New tree
#             a(1)
#
#                c(3)
#
#                    f(66)


# Existing tree
#             a(1)
#           /
#         b(2     c(3)
#       /       \
#   d(4)      e(5)      g(7)
#
# New tree
#                 a(1)
#             /
#          b(2)         h(8)
#       /    |   \
# e(5)   d(4)   f(6)       g(7)

if __name__ == "__main__":
    node1 = Node("a", 1)
    node2 = Node("b", 2)
    node3 = Node("c", 3)
    node4 = Node("d", 4)
    node5 = Node("e", 5)
    # node6 = Node("f", 6)
    node6 = Node("g", 7)

    node1.children.append(node2)
    node1.children.append(node3)
    node2.children.append(node4)
    node2.children.append(node5)
    node3.children.append(node6)

    node11 = Node("a", 1)
    node12 = Node("b", 2)
    node13 = Node("h", 8)
    node14 = Node("d", 4)
    node15 = Node("e", 5)
    node16 = Node("f",6)
    node17 = Node("g", 7)

    node11.children.append(node12)
    node11.children.append(node13)
    node12.children.append(node14)
    node12.children.append(node15)
    node12.children.append(node16)
    node13.children.append(node17)

    sol = Solution()
    print(sol.checkDifference(node1, node11))
    count,path = sol.checkDifferencePath(node1,node11)
    print(count)
    for item in path:
        print(item)
    # node1 = Node("a",1)
    # node2 = Node("b",2)
    # node3 = Node("c",3)
    # node4 = Node("d",4)
    # node5 = Node("e",5)
    # node6 = Node("f",6)
    #
    # node1.children.append(node2)
    # node1.children.append(node3)
    # node2.children.append(node4)
    # node2.children.append(node5)
    # node3.children.append(node6)
    #
    # node11 = Node("a",1)
    # node12 = Node("c",3)
    # node13 = Node("f",66)
    # node11.children.append(node12)
    # node12.children.append(node13)
    #
    # sol = Solution()
    # print(sol.checkDifference(node1,node11))


















