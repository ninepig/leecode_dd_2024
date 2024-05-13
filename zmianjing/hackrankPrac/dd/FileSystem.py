 # API:
# get(path): String -> returns the value of a the node at the given path
# set(path, value) -> changes the value of a given node to the new value. Should error out if the path does not currently exist
# create(path, value) -> creates a new node and sets it to the given value. Should error out if the node already exists
# or if the node’s parent does not exist. That is /level1/level2 cannot be created if /level1 has not already been created
# delete(path) -> deletes a node, but ONLY if it has no children

## TODO onwatch 还没写

class Trie:
    def __init__(self):
        self.value = None
        self.children = dict()

    def insert(self, path_string, value):
        node = self
        paths = path_string.split("/")
        ## skip first item , since that will be empty
        for path in paths[1:-1]:  ## we keep last item for better checking
            if path not in node.children:
                raise Exception("no parent path exists")
            node = node.children[path]
        ## bug 1
        last_path = paths[-1]
        if last_path in node.children:
            raise Exception("Node already exists")
        cur_node = Trie()
        cur_node.value = value
        node.children[last_path] = cur_node

        return True  ## insert success

    def get(self, path_string):
        node = self
        paths = path_string.split("/")
        ## skip first item , since that will be empty
        for path in paths[1:]:  ## we keep last item for better checking
            if path not in node.children:
                raise Exception("path not exist")
            node = node.children[path]

        if node.value is None:
            raise Exception("value does not exist")

        return node.value

    def update(self, path_string, value):
        node = self
        paths = path_string.split("/")
        ## skip first item , since that will be empty
        for path in paths[1:]:  ## we keep last item for better checking
            if path not in node.children:
                raise Exception("path not exist")
            node = node.children[path]

        if node.value is None:
            raise Exception("value does not exist")

        node.value = value
        return True

    def delete(self, path_string):
        node = self
        parent = None
        last_path = None
        paths = path_string.split("/")
        ## skip first item , since that will be empty
        for path in paths[1:]:  ## we keep last item for better checking
            if path not in node.children:
                raise Exception("path not exist")
            parent = node
            node = node.children[path]
            last_path = path

        ## we need check if target node has children
        if len(node.children) != 0:
            raise Exception("target path has child node")

        del parent.children[last_path]

        return True


class FileSystemWithTrie:

    def __init__(self):
        self.TrieTree = Trie()

    def createFile(self, paths, value):
        return self.TrieTree.insert(paths, value)

    def getFile(self, paths):
        return self.TrieTree.get(paths)

    def setFile(self, paths, values):
        return self.TrieTree.update(paths, values)

    def deleteFile(self, paths):
        return self.TrieTree.delete(paths)


sol = FileSystemWithTrie()
sol.createFile("/wenjing", "doordash")
sol.createFile("/wenjing/wenjing", "doordash2")
print(sol.getFile("/wenjing"))
print(sol.getFile("/wenjing/wenjing"))
sol.setFile("/wenjing", "doordash99")
print(sol.getFile("/wenjing"))
# sol.deleteFile("/wenjing")
sol.deleteFile("/wenjing/wenjing")
print(sol.getFile("/wenjing/wenjing"))

