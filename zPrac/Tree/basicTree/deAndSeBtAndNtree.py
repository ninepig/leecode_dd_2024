# Definition for a binary tree node.
from typing import List


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    '''
    node ---> string
    we use "null" if node is null
    we use " " work as splitter
    we use preorder to do visit tree
    '''

    def __init__(self):
        self.i = None

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        data = []
        def preOrder(node:TreeNode):
            if not node:
                data.append("null")
                return
            val = node.val
            data.append(val)
            preOrder(node.left)
            preOrder(node.right)

        preOrder(root)
        return ''.join(data)

    def deserialize(self, data:str):
        # """Decodes your encoded data to tree.
        data_array = data.split(",") # ","
        self.i = 0

        def preorder():
            if data_array[self.i] == "null":
                self.i += 1
                return None
            val = data_array[self.i]
            node = TreeNode(val)
            self.i += 1
            node.left = preorder()
            node.right = preorder()
            return node
        return preorder()



class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
class Serialize_and_Deserialize_N_ary_Tree:

    class Codec:
        SPLITER = ","
        NULL_NODE = "#"

        # Encodes a tree to a single string.
        def serialize(self, root: 'Node') -> str:
            data = []
            def dfs(node:Node):
                if not node:
                    data.append(self.NULL_NODE + self.SPLITER + "0" + self.SPLITER) # 0 size node
                else:
                    data.append(str(node.val) + self.SPLITER + str(len(node.children)) + self.SPLITER) ## current value and how many child it has
                    for child in node.children:
                        dfs(child)
            dfs(root)
            return ''.join(data)


        def deserialize(self, data: str) -> 'Node':
            if len(data) == 0:
                return None
            nodes = data.split(self.SPLITER)
            return self.buildTree(nodes)

        def buildTree(self, nodes: List[str])->'Node':
            ## pop 一个node 的value
            ## 如果他是空的， 则需要把size 也pop出来
            ## 如果不是空的， 把他child的size pop出来， 再循环做child的
            cur_node = nodes.pop()
            if cur_node == self.NULL_NODE:
                # pop the "0" added from sb.append(self.NULL_NODE + self.SPLITER + "0")
                size = int(nodes.pop(0)) # here now size=0, but do nothing

                # or, remove above 'size=...' line, but not adding "0" for null-node
                # which is better I think

                return None
            else:
                node = Node()
                node.val = int(cur_node)
                size = int(nodes.pop(0))  # to get children size

                node.children = []
                for i in range(size):
                    node.children.append(self.buildTree(nodes))

                return node




