# https://leetcode.com/discuss/interview-question/1794761/doordash-phone-screen
class TrieTree:
    def __init__(self):
        self.value = None ## value use to store file content
        self.children = dict() ## using dict to present key

    def insert(self,file_path:str,value:str):
        cur_node = self ##
        paths = file_path.split("/")
        for item in paths[1:-1] :## we need remove first path, since in python split will bring empty string in array[0]
            if item not in cur_node.children: ## if not in cur_node's children dict
                raise Exception("path has not exists ")
            cur_node = cur_node.children[item]

        ## we need check if last file is exist
        last_path = paths[-1] ## final file name
        if last_path in cur_node.children:
            raise Exception("file already exists")
        ## we can create file node
        temp_node = TrieTree()
        temp_node.value = value
        cur_node.children[last_path] = temp_node

        return True

    def get(self, file_path):
        cur_node = self  ##
        paths = file_path.split("/")
        for path in paths[1:]:  ## we need remove first path, since in python split will bring empty string in array[0]
            if path not in cur_node.children:  ## if not in cur_node's children dict
                raise Exception("file not exists")
            cur_node = cur_node.children[path]

        if cur_node.value is None:
            raise Exception("file content is broken")

        return cur_node.value

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
        cur_node = self
        paths = path_string.split("/")
        last_path = None
        parent = None

        for path in paths[1:]:
            if path not in cur_node.children:
                raise Exception("file not exists")
            parent = cur_node
            cur_node = cur_node.children[path]
            last_path = path

        if len(cur_node.children)!=0:
            raise Exception("can not delete, file has sub files")

        del parent.children[last_path]

        return True


class FileSystemWithTrie:

    def __init__(self):
        self.TrieTree = TrieTree()

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

##------------------------------------------
##onwatch

class TrieTreeOnWatch:
    def __init__(self):
        self.value = None ## value use to store file content
        self.children = dict() ## using dict to present key
        self.onWatch = False ## flag if this path is onWatch
    def insert(self,file_path:str,value:str):
        cur_node = self ##
        paths = file_path.split("/")
        if_onwatch = False
        for item in paths[1:-1] :## we need remove first path, since in python split will bring empty string in array[0]
            if item not in cur_node.children: ## if not in cur_node's children dict
                raise Exception("path has not exists ")
            cur_node = cur_node.children[item]
            if cur_node.onWath:
                if_onwatch = True

        ## we need check if last file is exist
        last_path = paths[-1] ## final file name
        if last_path in cur_node.children:
            raise Exception("file already exists")
        ## we can create file node
        temp_node = TrieTree()
        temp_node.value = value
        cur_node.children[last_path] = temp_node

        if if_onwatch:
            self.callback("create",file_path,None,value)

        return True

    def get(self, file_path):
        cur_node = self  ##
        paths = file_path.split("/")
        for path in paths[1:]:  ## we need remove first path, since in python split will bring empty string in array[0]
            if path not in cur_node.children:  ## if not in cur_node's children dict
                raise Exception("file not exists")
            cur_node = cur_node.children[path]

        if cur_node.value is None:
            raise Exception("file content is broken")
        if cur_node.onWatch:
            self.callback("get", file_path, cur_node.value, None)

        return cur_node.value

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

        if node.onWatch:
            self.callback("set", path_string, node.value, value)

        node.value = value


        return True

    def delete(self, path_string):
        cur_node = self
        paths = path_string.split("/")
        last_path = None
        parent = None

        for path in paths[1:]:
            if path not in cur_node.children:
                raise Exception("file not exists")
            parent = cur_node
            cur_node = cur_node.children[path]
            last_path = path

        if len(cur_node.children)!=0:
            raise Exception("can not delete, file has sub files")

        if cur_node.onWatch:
            self.callback("delete", path_string, cur_node.value, None)
        del parent.children[last_path]

        return True

    # we need make sure we have this file there then, on watch
    def Watch(self,path_string):
        cur_node = self  ##
        paths = path_string.split("/")
        for item in paths[1:]:  ## we need remove first path, since in python split will bring empty string in array[0]
            if item not in cur_node.children:  ## if not in cur_node's children dict
                raise Exception("path has not exists , can not on watch")
            cur_node = cur_node.children[item]
        cur_node.onWatch = True ## ADDING WATCH flag on current node 
        return True

    def callback(self, param, file_path, param1, value):
        print("callback triggered ")


class FileSystemWithTrie:

    def __init__(self):
        self.TrieTree = TrieTree()

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