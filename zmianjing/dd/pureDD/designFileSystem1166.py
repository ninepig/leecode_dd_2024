class Trie:
    def __init__(self):
        self.children = {}
        self.v = 0

    def insert(self, s, v):
        node = self
        paths = s.split('/')
        for path in paths[1:-1]: # leave the last element , if any in path is missing , means that path can not be put since no parent path exist
            if path not in node.children:
                return False
            node = node.children[path]
        if paths[-1] in node.children: # means all the path already exist
            return False

        node.children[paths[-1]] = Trie()
        node = node.children[paths[-1]]
        node.v = v
        return True

    def search(self,s)-> int:
        node = self
        paths = s.split('/')
        for path in paths:
            if path not in node.children:
                return -1
            node = node.children[path]
        return node.v or -1 # 有可能被delete了

    #自己写的 ,这个逻辑不对 ， python 的del dict key 必须是 del dict[key]
    def delete(self,s)->bool:
        node = self
        paths = s.split('/')
        for path in paths:
            if path not in node.children:
                return False
            node= node.children[path]
        del node
        return True

    #自己写的 ,这个逻辑才make sense， 还需要测试 ， python 的del dict key 必须是 del dict[key]
    def delete(self,s)->bool:
        node = self
        parent = None
        lastPath = None
        paths = s.split('/')
        for path in paths:
            if path not in node.children:
                return False
            parent = node
            node= node.children[path]
            lastPath = path
        del parent[lastPath] ## delete LastNode, this node has value
        return True



