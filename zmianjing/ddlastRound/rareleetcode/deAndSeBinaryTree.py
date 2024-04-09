class Node:
    def __init__(self,value):
        self.value= value
        self.left = None
        self.right = None

class solution:
    def se(self,root):
        if not root:
            return "Null"
        return str(root.value) + "," +self.se(root.left) + "," + self.se(root.right)

    def de(self,dataList):

        def preOrder(datas):
            current = datas.pop(0) ##pop first on the queue
            if current == "Null":
                return None
            root = Node(current)
            root.left = preOrder(datas)
            root.right = preOrder(datas)

            return root
        datas = dataList.split(",")
        return preOrder(datas)


class Nnode:
    def __init__(self,val):
        self.val = val
        self.children = []


## 这个方法太有优雅了！！
class solution:

    def se(self,root):
        array = []
        self.buildString(root,array)
        return ''.join(array)

    def buildString(self,node,array):
        if not node:
            array.append("#" + "," + "0" + ",")
        else:
            array.append(str(node.val) + "," + str(len(node.children)) + ",")
            for child in node.children:
                self.buildString(child,array)

    def de(self,data):
        if len(data) == 0:
            return None
        node_list = data.split(",")
        return self.buildTree(node_list)

    def buildTree(self,nodes:list[str]):
        val = nodes.pop(0)
        if val == "#":

            nodes.pop(0) ## remove the size 0
            return None
        else:
            node = Nnode(val)
            size = int(nodes.pop(0))
            node.children= []
            for i in range(size):
                node.children.append(self.buildString())

            return node




