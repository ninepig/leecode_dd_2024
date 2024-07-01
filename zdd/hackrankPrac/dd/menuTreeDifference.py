class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.children = []
        # self.status = bool ## for menu question   , this could be two questions


class Solution:
    def findDifferenceCount(self, old_root, new_root):
        if not old_root and not new_root:
            return 0
        elif not old_root:
            return self.getCount(new_root)
        elif not new_root:
            return self.getCount(old_root)
        elif old_root.key != new_root.key:
            return self.getCount(new_root) + self.getCount(old_root)

        count = 0
        if old_root.value != new_root.value:
            # if old_root.value != new_root.value or old_root.status != new_root.status:
            count += 1

        ## calc the child
        new_root_child = {item.key: item for item in new_root.children}

        for old_child in old_root.children:
            ## if we have old  child key in new child dict, we find one, otherwise, popout None
            count += self.findDifferenceCount(old_child, new_root_child.pop(old_child.key, None))

        for rest_child in new_root_child.values():
            count += self.getCount(rest_child)

        return count

    def getCount(self, node):
        if not node:
            return 0
        count = 1
        for child in node.children:
            count += self.getCount(child)

        return count

    def checkDifferencePath(self, old_root: Node, new_root: Node):
        if not old_root and not new_root:
            return 0, []
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
            child_diff, child_path = self.checkDifferencePath(old_child,
                                                              new_tree_key_child_dict.pop(old_child.key, None))
            count += child_diff
            path += child_path
        ## bugbugbugbugbug !! 没加values
        for rest_child in new_tree_key_child_dict.values():  ## bug here, that is node / not key
            child_diff, child_path = self.countTreePath(rest_child)
            count += child_diff
            path += child_path

        return count, path

    def countTreePath(self, cur_node: Node):
        if not cur_node:
            return 0
        diff_list = []
        count = 1
        diff_list.append(cur_node)
        for child in cur_node.children:
            child_count, children_path = self.countTreePath(child)
            count += child_count
            diff_list += children_path
        return count, diff_list


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
node16 = Node("f", 6)
node17 = Node("g", 7)

node11.children.append(node12)
node11.children.append(node13)
node12.children.append(node14)
node12.children.append(node15)
node12.children.append(node16)
node13.children.append(node17)

sol = Solution()
print(sol.checkDifferencePath(node1, node11))