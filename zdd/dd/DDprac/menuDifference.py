class Node:
    def __init__(self, key, value, isActive):
        self.key = key
        self.value = value
        self.isActive = isActive
        self.children = []

    def equals(self, node: 'Node'):
        if node is None:
            return False

        return self.key == node.key and self.value == node.value and self.isActive == node.isActive

def get_child_nodes(menu: 'Node'):
    m = {}
    if menu is None:
        return m

    for node in menu.children:
        m[node.key] = node

    return m

def get_modified_items(oldMenu, newMenu):

    if oldMenu is None and newMenu is None:
        return 0

    count = 0
    if oldMenu is None or newMenu is None or not oldMenu.equals(newMenu):
        count += 1

    child1 = get_child_nodes(oldMenu)
    child2 = get_child_nodes(newMenu)

    for k in child1.keys():
        count += get_modified_items(child1.get(k), child2.get(k))

    for k in child2.keys():
        if k not in child1:
            count += get_modified_items(None, child2.get(k))

    return count





