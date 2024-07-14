class menuNode:
    def __init__(self,key:str,value:int,status:bool):
        self.key = key
        self.value = value
        self.status = status
        self.children = []

class solution:

    def checkDifference(self, old_root: menuNode, new_root: menuNode):
        if not old_root or not new_root:
            return 0
        if not old_root :
            return self.count(new_root)
        if not new_root :
            return self.count(old_root)
        if new_root.key != old_root.key:
            return self.count(old_root) + self.count(new_root)

        count = 0
        if old_root.value != new_root.value or old_root.status != new_root.status:
            count += 1

        new_tree_key_children_dict = {c.key:c for c in new_root.children}
        for old_child in old_root.children:
            ## compare any old child key in new children dict, if not exist, we pop None
            ## 这一行 细品
            count += self.checkDifference(old_child,new_tree_key_children_dict.pop(old_child.key,None))

        ## 剩下的new child value
        for rest_child in new_tree_key_children_dict.values():
            count += self.count(rest_child)

        return count

    def count(self, node):
        if not node:
            return 0
        count = 1
        for child in node.children:
            count += self.count(child)
        return count

