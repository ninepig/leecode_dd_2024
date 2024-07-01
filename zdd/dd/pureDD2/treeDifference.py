class TreeNode(object):
    def __init__(self):
        self.key = str
        self.value = str
        self.children = []


class Solution :
    # https://www.1point3acres.com/bbs/thread-779975-1-1.html
    # 一些判定规则如下（面试时请与面试官clarify，不要上来就说是这样，至少要会演）：
    # 1.
    # 如果node
    # key一样，value一样，视为同一个节点。
    # 2.
    # 如果node
    # key一样，value不同，视为不同节点，但树的结构保持不变。
    # 3.
    # 如果node
    # key不同，则视为完全不同的两棵树，答案应该返回这两棵树里一共有多少节点。
    # 4.
    # children数组里的顺序无关。
    def compute_diff(self,old_tree: TreeNode, new_tree: TreeNode) -> int:
        if old_tree is None and new_tree is None:
            return 0
        ## if tree different
        elif old_tree is None:
            return self.get_node_count(new_tree)
        elif new_tree is None:
            return self.get_node_count(old_tree)
        elif old_tree.key != new_tree.key:
            return self.get_node_count(old_tree) + self.get_node_count(new_tree)

        cur_res = 0
        if old_tree.value != new_tree.value:
            cur_res +=1

        # put key : children  (key is children 's key, c is children) in dict
        new_tree_children = {c.key : c for c in new_tree.children}
        for old_child in old_tree.children:
            # compare old_tree's children with new tree's children
            # 這個方法很優雅
            cur_res += self.compute_diff(old_child,new_tree_children.pop(old_child.key,None))

        # for new children which not has same in old one
        for rest_new_child in new_tree_children.values():
            cur_res += self.get_node_count(rest_new_child)

        return cur_res

    def get_node_count(self, node:TreeNode):
        if not node:
            return 0

        count = 1
        for child in node.children:
            count += self.get_node_count(child)

        return count
