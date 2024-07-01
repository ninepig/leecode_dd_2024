'''
At DoorDash, menus are updated daily even hourly to keep them up-to-date.
 Each menu can be regarded as a tree. A menu can have many categories;
 each category can have many menu_items; each menu_item can have many item_extras; An item_extra can have many item_extra_options…

class Node {
        String key;
        int value;
        boolean active;
        List<Node> children;
 }
We will compare the new menu sent from the merchant with our existing menu.
Each item can be considered as a node in the tree.
The definition of a node is defined above.
Either value change or the active status change means the node has been changed.
There are times when the new menu tree structure is different from existing trees,
 which means some nodes are set to null. In this case, we only do soft delete for any nodes in the menu.
 If that node or its sub-children are null, we will treat them ALL as inactive. There are no duplicate nodes with the same key.

这道题和tree difference 还不一样
如果 node 是null ，他只是把 active 设置成 false 这样其实不删除
也就是 树的结构其实不会变 变化的只是 status
所以相同node 的条件 就是key ， value ， status 都相同
'''

class menuNode:
    def __init__(self,):
        self.key = str
        self.value = str
        self.activate = bool
        self.children = []

class solution:
    def findMenuDifference(self,new_menu:menuNode, old_menu:menuNode):
        # when we reach to none node, end of dfs
        if not new_menu and not old_menu:
            return 0

        count = 0
        # 两个node 不同的情况下
        if not new_menu or not old_menu or not self.eqaul(new_menu,old_menu):
            count += 1
        ## compare children
        new_menu_children_dict = self.get_child_node_dict(new_menu)
        old_menu_children_dict = self.get_child_node_dict(old_menu)

        # if has same children node
        for k in new_menu_children_dict.keys():
            if k in old_menu_children_dict.keys():
                count += self.findMenuDifference(new_menu_children_dict.get(k),
                                                 old_menu_children_dict.get(k))

        # if has node difference
        for k in new_menu_children_dict.keys():
            if k not in old_menu_children_dict:
                count += self.findMenuDifference(new_menu_children_dict.get(k),
                                                 None)

        return count

    def eqaul(self, new_menu, old_menu):

        return (new_menu.key == old_menu.key and new_menu.value == old_menu.value
                and new_menu.activate == old_menu.activate)

    def get_child_node_dict(self, menu):
        child_dict = dict()

        if not menu:
            return child_dict

        for child in menu.children:
            child_dict[child.key] = child

        return child_dict

