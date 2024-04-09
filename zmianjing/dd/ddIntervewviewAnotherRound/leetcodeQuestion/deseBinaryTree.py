import collections
from typing import List


class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        if not root:
            return 'None'
        return str(root.val) + ',' + str(self.serialize(root.left)) + ',' + str(self.serialize(root.right))

    def deserialize(self, data):
        def dfs(datalist):
            val = datalist.pop(0)
            if val == 'None':
                return None
            root = TreeNode(int(val))
            root.left = dfs(datalist)
            root.right = dfs(datalist)
            return root

        datalist = data.split(',')
        return dfs(datalist)


# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Serialize_and_Deserialize_N_ary_Tree:
    #
    class Codec:

        SPLITER = ","
        NULL_NODE = "#"

        # Encodes a tree to a single string.
        def serialize(self, root: 'Node') -> str:
            sb = []
            self.buildString(root, sb)
            return ''.join(sb)

        # pre-order traversal
        def buildString(self, node: 'Node', sb: List[str]):
            if node is None:
                sb.append(self.NULL_NODE + self.SPLITER + "0" + self.SPLITER)  # size=0
            else:
                sb.append(str(node.val) + self.SPLITER + str(len(node.children)) + self.SPLITER)
                for child in node.children:
                    self.buildString(child, sb)

        # Decodes your encoded data to tree.
        def deserialize(self, data: str) -> 'Node':
            if len(data) == 0:
                return None

            nodes_list = data.split(self.SPLITER)
            return self.buildTree(nodes_list)

        def buildTree(self, nodes: List[str]) -> 'Node':
            # @note: key is here, just keep popping the 1st as root of current sub-tree
            val = nodes.pop(0)

            if val == self.NULL_NODE:
                # pop the "0" added from sb.append(self.NULL_NODE + self.SPLITER + "0")
                size = int(nodes.pop(0)) # here now size=0, but do nothing
                # or, remove above 'size=...' line, but not adding "0" for null-node
                # which is better I think
                return None
            else:
                node = Node()
                node.val = int(val)
                size = int(nodes.pop(0))  # to get children size

                node.children = []
                for i in range(size):
                    node.children.append(self.buildTree(nodes))

                return node