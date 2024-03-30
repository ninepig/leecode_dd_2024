'''
这道题经常见
是leetcode 加强版 增加了delete的api
1 hashmap
2 trie
todo do more test case
'''

class solutionHashmap:

    def __init__(self):
        self.table = dict()
        self.table[""] = -1 ## give an empty dummy value to make this work
    def createPath(self,key:str,value:str):
        if not key or len(key) == 0:
            return False
        if key in self.table:
            return False ## existed already
        prefix = key[:key.rindex("/")] ## /aa/bb --> we need /aa contain in the table , otherwise falue
        if prefix not in self.table:
            return False
        else:
            self.table[key] = value

        return True

    def getPathValue(self,key:str):
        if key not in self.table:
            return None
        return self.table[key]

    ## need check with inteviewer, if /aa/bb exist, we want to delete /aa, what happen?
    ## remove all with /aa prefix or telling user there is a conflict
    ## we treate this as remove all  (start with )
    def deletePath(self,key:str):
        if key not in self.table:
            return False ## not exit
        pendingDelete = []
        for item in self.table.keys():
            if item.startswith(key):
                pendingDelete.append(item)
        for delete_key in pendingDelete:
            del self.table[delete_key]

        return True


class Trie:
    ## using tree, each path will be trie node's key
    def __init__(self):
        self.value = str
        self.children = dict()

    def insertFile(self,path:str,value:str):
        node = self
        paths = path.split("/")
        for item in paths[1:-1]: ## we leave last path to do check
            if item not in node.children: ## parent path not there
                return False
            node = node.children[item]
        if paths[-1] in node.children: ## path already there
            return False
        node.children[paths[-1]] = Trie()
        node = node.children[paths[-1]]
        node.value = value

        return True

    ## in Trie, delete is much easier, if parent delete, children will all delete if there is no parent
    def deleteFile(self,path:str):
        node = self
        parent = None
        last_path = None
        paths = path.split("/")
        paths = paths[1:]
        for item in paths:
            if item not in node.children:
                return False ## parent path not exist
            ## 顺序不能错啊！！傻逼玩意儿
            parent = node
            node = node.children[item]
            last_path = item
        ## path exist
        del parent.children[last_path]
        return True

    def searchFile(self,path:str):
        node = self
        paths = path.split("/")
        paths = paths[1:] ## in python it will be empty for first if we split "/aa/bb"
        for item in paths:
            if item not in node.children:
                return -1 ## not exist
            else:
                node = node.children[item]
        return node.value or -1


class solutionTrie:

    def __init__(self):
        self.trie = Trie()
    def createPath(self,paths:str, val:str):
        return self.trie.insertFile(paths,val)

    def getPathValue(self,paths):
        return self.trie.searchFile(paths)

    def deletePath(self,paths):
        return self.trie.deleteFile(paths)






test = solutionTrie()
print(test.createPath("/leet/code","123"))
print(test.createPath("/leet","222"))
print(test.createPath("/leet/code","123"))
print(test.getPathValue("/leet"))
print(test.getPathValue("/leet/code"))
# print(test.deletePath("/leet/code"))
# print(test.getPathValue("/leet/code"))
print(test.deletePath("/leet"))
print(test.getPathValue("/leet"))



# test = solutionHashmap()
# print(test.createPath("/leet/code","123"))
# print(test.createPath("/leet","123"))
# print(test.getPathValue("/leet"))
# print(test.createPath("/leet/code","222"))
# print(test.getPathValue("/leet/code"))
# print(test.deletePath("/leet"))
# print(test.getPathValue("/leet/code"))












