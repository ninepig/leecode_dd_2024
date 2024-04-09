'''
Implement an in-memory tree key value store.
Definitions:
path is a / separate string describing the node. Example /animals/dogs/german_shepard
Values are all strings

# API:
# get(path): String -> returns the value of a the node at the given path
# set(path, value) -> changes the value of a given node to the new value. Should error out if the path does not currently exist
# create(path, value) -> creates a new node and sets it to the given value. Should error out if the node already exists
# or if the node’s parent does not exist. That is /level1/level2 cannot be created if /level1 has not already been created
# delete(path) -> deletes a node, but ONLY if it has no children

follow yo
没那么复杂，你就在node里加一个value，存那个function
每次你走path的时候，走到一个node，如果有function，存起来就行
这个题的坑在于，你写第一题的时候就要reusable的code
把走path这个逻辑包到一个function里
'''


class Trie:
    def __init__(self):
        self.value = str
        self.children = dict()

    ## input is /animals/dogs/german_shepard
    def insert(self,paths:str,value:str)->bool:
        node = self
        path = paths.split("/")
        ## path[0] is empty since our input /animals/dogs/german_shepard
        ## path[-1] we want to save german_shepherd for checking
        for item in path[1:-1]:
            if item not in node.children: ## parent path not exist
                raise Exception("parent path does not exists")
            node = node.children[item]

        last_path = path[-1]
        if last_path in node.children : ## it already exists:
            raise Exception("file already exists")

        cur_node = Trie()
        cur_node.value = value
        node.children[last_path] = cur_node
        return True

    def update(self,paths:str,value:str)->bool:
        node = self
        path = paths.split("/")
        ## path[0] is empty since our input /animals/dogs/german_shepard
        ## path[-1] we want to save german_shepherd for checking
        for item in path[1:-1]:
            if item not in node.children: ## parent path not exist
                raise Exception("parent path does not exists")
            node = node.children[item]

        last_path = path[-1]
        if last_path not in node.children : ## it already exists:
            raise Exception("node not exists")

        cur_node = node.children[last_path]
        if cur_node.value:
            ## update value
            cur_node.value = value
        else:
            raise Exception("node content exists")
        return True
    def search(self,paths:str):
        node = self
        path = paths.split("/")
        for item in path[1:]:
            if item not in node.children:
                raise Exception("path does not exists")
            node = node.children[item]

        if not node.value:
            raise Exception("path does not has value")
        return node.value

    def delete(self, paths: str):
        node = self
        parent = None
        last_item = None
        path = paths.split("/")
        ## delete 不能用这个 [1:-1] 因为可能只有1个path
        for item in path[1:]:
            if item not in node.children:
                raise Exception("path does not exists")
            parent = node
            node = node.children[item]
            last_item = item

        ## check if last node has children
        if len(node.children) > 0:
            raise Exception("node has children")

        del parent.children[last_item] ## delete from parent dict

        return True


class solution:

    def __init__(self):
        self.Trie = Trie()

    # API:
    # get(path): String -> returns the value of a the node at the given path
    # set(path, value) -> changes the value of a given node to the new value. Should error out if the path does not currently exist
    # create(path, value) -> creates a new node and sets it to the given value. Should error out if the node already exists
    # or if the node’s parent does not exist. That is /level1/level2 cannot be created if /level1 has not already been created
    # delete(path) -> deletes a node, but ONLY if it has no children

    def get(self,path):
        return self.Trie.search(path)

    def set(self,path,value):
        return self.Trie.update(path,value)

    def create(self,path,value):
        return self.Trie.insert(path,value)

    def delete(self,path):
        return self.Trie.delete(path)

if __name__ == "__main__":
    sol = solution()
    #case 1
    # sol.create("/wenjing/wenjing","abc") ## good

    # case2
    # sol.create("/wenjing", "abc")
    # print(sol.get("/wenjing"))

    # case3
    # sol.create("/wenjing", "abc")
    # sol.set("/wenjing","bcd")
    # print(sol.get("/wenjing"))

    # case4
    # sol.create("/wenjing", "abc")
    # sol.set("/wenjing","bcd")
    # sol.delete("/wenjing")
    # print(sol.get("/wenjing")) ## delete successed

    # case 5
    # sol.create("/wenjing", "abc")
    # sol.create("/wenjing/wenjing2", "bbb")
    # sol.create("/wenjing/wenjing2/wenjing3", "ccc")
    # print(sol.get("/wenjing/wenjing2"))
    # print(sol.get("/wenjing/wenjing2/wenjing3"))

    ## case 6
    # sol.create("/wenjing", "abc")
    # sol.create("/wenjing/wenjing2", "bbb")
    # sol.create("/wenjing/wenjing2/wenjing3", "ccc")
    # sol.delete("/wenjing/wenjing2")
