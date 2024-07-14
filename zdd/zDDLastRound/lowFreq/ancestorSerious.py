class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = TreeNode()
        self.right = TreeNode()

class Node:
    def __init__(self):
        self.val = int
        self.children = []
class solution:
    def lowestCommonAncestor(self,root:TreeNode,p:TreeNode,q:TreeNode):
        if not root or p == root or q == root:
            return root ## if root is empty or root is one of target node , it ends dfs
        left = self.lowestCommonAncestor(root.left,p,q)## try to search left
        right = self.lowestCommonAncestor(root.right,p,q)  ## try to search right
        if not left and not right:
            return None
        if left and right:
            return root
        return left if left is not None else right



## 这个方法比较好。 因为只有可能在中间，且一定存在。 所以这种方法比较好
    def lowestCommonAncestorBst(self,root:TreeNode,p:TreeNode,q:TreeNode):
        if not root:
            return root

        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestorBst(root.right,p,q)

        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestorBst(root.left,p,q)

        return root

    ## we assume two target node exist version
    def lowestCommonAncestorNarray(self,root:Node,p:Node,q:Node):
        if p == root or q == root:
            return root ## we found one node equal to target
        count = 0
        temp = None
        for child in root.children:
            res = self.lowestCommonAncestorNarray(child,p,q)
            if res is not None:
                count += 1 ## we found one target in child
                temp = res
        if count == 2:
            return root # means in this level's root, we have two target found

        return temp # if we did not found both, return found node


## could not exit version.
class Node(object):
    def __init__(self, val):
        self.val = val
        self.children = []
        self.ans = None

    def add_child(self, child_node):
        self.children.append(child_node)


def lca(node, a, b, ans):
    if ans[0] is not None:
        return

    return_vals = []
    for child in node.children:
        if child.val == a or child.val == b:
            return_vals.append(child.val)
        else:
            return_vals.append(lca(child, a, b, ans))
    else:
        is_a = is_b = False
        for val in return_vals:
            if val == a:
                is_a = True
            if val == b:
                is_b = True

    if is_a and is_b:
        ans[0] = node.val
        print(node.val)
    else:
        if is_a:
            return a
        if is_b:
            return b