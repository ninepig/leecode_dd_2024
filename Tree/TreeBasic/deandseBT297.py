from Tree.TreeBasic.TreeNode import TreeNode

'''
这道题很经典
就是前序遍历'''
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'NULL'
        return str(root.val) + ',' + str(self.serialize(root.left)) + ',' + str(self.serialize(root.right))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def dfs(datalist):
            val = datalist.pop(0)
            if val == 'NULL':
                return None
            root = TreeNode(int(val))
            root.left = dfs(datalist)
            root.right = dfs(datalist)
            return root

        datalist = data.split(',')
        return dfs(datalist)

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "NULL"

        return str(root.val) + ',' + str(self.serialize(root.left)) + ',' + str(self.serialize(root.right))

    def deserialize(self, data):
        dataList = data.split(',')
        def dfs(datalist):
            val = datalist.pop(0)
            if val == "NULL":
                return None
            root =TreeNode(val)
            root.left = dfs(datalist)
            root.right = dfs(datalist)
            return root
        return dfs(dataList)