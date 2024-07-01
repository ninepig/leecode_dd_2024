from collections import defaultdict

class Trie:
    def __init__(self):
        self.name = None
        self.isFile = False
        self.content = []
        self.children = {}

    def insert(self, path, isFile):
        node = self
        ps = path.split('/')
        for p in ps[1:]:
            if p not in node.children:
                node.children[p] = Trie()
            node = node.children[p]
        node.isFile = isFile
        if isFile:
            node.name = ps[-1]
        return node

    def search(self, path):
        node = self
        if path == '/':
            return node
        ps = path.split('/')
        for p in ps[1:]:
            if p not in node.children:
                return None
            node = node.children[p]
        return node


class FileSystem:
    def __init__(self):
        self.root = Trie()

    def ls(self, path: str) -> list[str]:
        node = self.root.search(path)
        if node is None:
            return []
        ## 如果是file 那就是展示file name
        if node.isFile:
            return [node.name]
        ## 如果ls是一个folder 那就会巴下面的folder 全部打印出来
        return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        self.root.insert(path, False)

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.root.insert(filePath, True)
        node.content.append(content)

    def readContentFromFile(self, filePath: str) -> str:
        node = self.root.search(filePath)
        return ''.join(node.content)



obj = FileSystem()
path = "/wenjing/fff"
filePath = "/wenjing/abc"
content = "abc"
# print(obj.mkdir(path))
param_1 = obj.ls(path)
print(param_1)
obj.addContentToFile(filePath,content)
param_4 = obj.readContentFromFile(filePath)
print(param_4)
print(obj.ls(filePath))
