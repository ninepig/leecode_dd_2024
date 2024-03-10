'''
这道题可以用trie，也可以用hashmap 来做

bool createPath(string path, int value) Creates a new path and associates a value to it if possible and returns true.
Returns false if the path already exists or its parent path doesn't exist.

int get(string path) Returns the value associated with path or returns -1 if the path doesn't exist.

bool delete(string path) return true if delete path successful , return False if no node exist


'''
# 第一想法使用trie 来做,  children 是每一级的path
# for tire --> /leet/code split ---> ['', 'leet', 'code'] so we need skip first items
class Trie:
    def __init__(self):
        self.val = str
        self.children = dict()

    def insert(self,paths:str, value:str):
        node = self
        path_array = paths.split('/')
        print(path_array)
        for path in path_array[1:-1]: # not including last element
            if path not in node.children:
                return False # if there  is one path not in trie
            node = node.children[path]
        if path_array[-1] in node.children: # means last path already in trie
            return False

        node.children[path_array[-1]] = Trie()
        node = node.children[path_array[-1]]
        node.val = value
        return True # insert

    def search(self,s):
        node = self
        path_array = s.split('/')
        paths = path_array[1:] ## need to do this to skip  first item ""
        for path in paths:
            if path not in node.children:
                return -1
            node = node.children[path]
        return node.val or -1 # if node.v not exit , return -1

    def delete(self,s):
        node =self
        parent = None ## we need a point to parent node, use to delete path
        last_path = None
        path_array = s.split('/')
        paths = path_array[1:]
        for path in paths:
            if path not in node.children:
                return False # not exist
            parent = node
            node = node.children[path]
            last_path = path
        ## we found target path , use children to dict to delete
        del parent.children[last_path]
        return True


class solutionTrie:

    def __init__(self):
        self.trie = Trie()
    def createPath(self,paths:str, val:str):
        return self.trie.insert(paths,val)

    def getPathValue(self,paths):
        return self.trie.search(paths)

    def deletePath(self,paths):
        return self.trie.delete(paths)


'''
如果用map来做
map的key 应该是 whole path 
value is target value

'''
class solutionHashmap:

    def __init__(self):
        ## path to file value dict
        self.path_file_dict = {"":-1} ## empty as -1 for root path
    ## create 的时候只要看看任何一个parent path 是否存在就行。
    # 比如 /leet/code/file  要看leet/ code 是不是存在 再存file
    # 这样其实简化了 对于 这个 我们只要检查 /LEET/CODE 是否存在就行了。
    # 因为 /code/创建的时候 会替我们检查 leet存在与否
    def createPath(self,paths:str, val:str):
        print(paths)
        if paths in self.path_file_dict:
            return False ## already exists
        if not paths[:paths.rindex("/")] in self.path_file_dict:##parent path not exit
            return False
        self.path_file_dict[paths] = val
        return True

    def getPathValue(self,paths):
        if paths in self.path_file_dict:
            return self.path_file_dict[paths]
        else:
            return "not exist"

    ## need ask what happen if there is children exist?
    ## if this is required, we need check before delete
    ## if any key contain this path in map. if contain. delete
    def deletePath(self,paths):
        # if paths in self.path_file_dict:
        #     del self.path_file_dict[paths]
        # else:
        #     return "not exists"
        ## if we want to delete any path with parent path as input


        contain = False
        delete_key = []
        for key in self.path_file_dict.keys():
            if paths in key:
                # To avoid runtime error
                ##     for key in self.path_file_dict.keys():
                #RuntimeError: dictionary changed size during iteration
                # del self.path_file_dict[key]
                delete_key.append(key)
                contain = True
        for delete_path in delete_key:
            del self.path_file_dict[delete_path]
        if not contain:
            return "not contain"
        else:
            return "successed"


# test = solutionHashmap()
# print(test.createPath("/leet/code","123"))
# print(test.createPath("/leet","123"))
# print(test.getPathValue("/leet"))
# print(test.createPath("/leet/code","222"))
# print(test.getPathValue("/leet/code"))
# print(test.deletePath("/leet"))
# print(test.getPathValue("/leet/code"))

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

