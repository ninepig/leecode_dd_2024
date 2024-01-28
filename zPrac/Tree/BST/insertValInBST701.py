from Tree.TreeBasic.TreeNode import TreeNode


class Solution:
    # 这个题考察的是bst的基本性质, 如果val < target 在左侧, 当左侧为空的情况下 直接插入左侧,不为空就继续查找
    # 同理右侧
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        cur = root
        while cur:
            if cur.val < val:
                #
                if not cur.left:
                    target = TreeNode(val)
                    cur.left = target
                    break
                else:
                    cur = cur.left
            else:
                if not cur.right:
                    target = TreeNode(val)
                    cur.right = target
                    break
                else:
                    cur = cur.right

        return root