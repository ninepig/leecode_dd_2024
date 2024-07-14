class BNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
class SolutionBtree:

    def se(self,root):
        if not root:
            return "NULL"
        return str(root.value) + "," + self.se(root.left) + "," + self.se(root.right)

    def de(self,dataList):
        def preOrder(datas):
            current = datas.pop(0) ## pop first item, since preorder
            if current == "NULL":
                return None
            root = BNode(current)
            root.left = preOrder(datas)
            root.right = preOrder(datas)

            return root
        datas = dataList.split(",")
        return  preOrder(datas)



class NNode:
    def __init__(self,value):
        self.value = value
        self.children = None

class SolutionNTree:

    def se(self,root:NNode):
        array = []
        self.build_String(root,array)
        return ''.join(array)

    def build_String(self, node, array):
        if not node:
            ## we use # represent NULL , 0 means 0 children
            array.append("#" + "," + "0" + ",")
        else:
            array.append(str(node.val)+","+str(len(node.children))+",")
            for child in node.children:
                self.build_String(child,array)

    def de(self,datas:str):
        if len(datas) == 0:
            return None
        data_list = datas.split(",")
        return self.buildTree(data_list)

    def buildTree(self, data_list):
        val = data_list.pop(0) ## pop first vlaue
        if val == '#':
            data_list.pop(0) ## pop children
            return None
        else:
            node = NNode(val)
            size = int(data_list.pop(0))
            node.children = []
            for i in range(size):
                node.children.append(self.buildTree(data_list))

            return node