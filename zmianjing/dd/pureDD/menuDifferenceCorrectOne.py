class Node:
	def __init__(self, key, value, is_active):
		self.key = key
		self.value = value
		self.is_active = is_active
		self.children = []

	def get_children_map(self):
		map = {}
		for child in self.children:
			map[child.key] = child
		return map

def find_children(node):
	if node==None:
		return 0
	count_child = 0
	for child in node.children:
		count_child+=find_children(child)
	return count_child+1

def find_modified_nodes(old_menu_root, new_menu_root):
	count = 0
	def change(old_menu_root, new_menu_root):
		nonlocal count

		if old_menu_root==None and new_menu_root==None:
			return
		if old_menu_root==None:
			count =  count + find_children(new_menu_root)
		elif new_menu_root==None:
			count = count + find_children(old_menu_root)
		elif old_menu_root.key!=new_menu_root.key:
			count = count + find_children(old_menu_root)
			count = count + find_children(new_menu_root)
		else:
			if old_menu_root.value!=new_menu_root.value:
				count += 1
			elif old_menu_root.is_active!=new_menu_root.is_active:
				count += 1
			map_old_children = old_menu_root.get_children_map()
			map_new_children = new_menu_root.get_children_map()
			for key in map_old_children:
				if key in map_new_children:
					change(map_old_children[key], map_new_children[key])
				else:
					change(map_old_children[key], None)
			for key in map_new_children:
				if key not in map_old_children:
					change(None, map_new_children[key])
	change(old_menu_root, new_menu_root)
	print("Changed nodes:", count)


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


find_modified_nodes(a, a1)