class Node:
    def __init__(self):
        self.children = dict()
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = Node()

    # insert
    def insert(self,word:str):
        root = self.root
        for ch in word:
            if not root.children[ch]:
                root.children[ch] = Node()
            root = root.children[ch]

        root.isEnd = True

    def search(self,word:str)->bool:
        root = self.root
        for ch in word:
            if not root.children[ch]:
                return False
            root = root.children[ch]

        return root is not None and root.isEnd == True

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for ch in prefix:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        return cur is not None