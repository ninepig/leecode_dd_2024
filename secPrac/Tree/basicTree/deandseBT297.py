from firstRount.Tree.TreeBasic.TreeNode import TreeNode


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "NONE"
        return  str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        ## preorder
        def dfs(datalist):
            val = datalist.pop(0)
            if val == 'NONE':
                return None
            root = TreeNode(val)
            root.left = TreeNode(datalist)
            root.right = TreeNode(datalist)
            return root
        datalist = data.split(",")
        return dfs(datalist)
