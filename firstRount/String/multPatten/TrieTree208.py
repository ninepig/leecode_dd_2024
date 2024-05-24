'''Trie tree 实现
插入一个单词：时间复杂度为 o(n)
；如果使用数组，则空间复杂度为 o(d^n)
，如果使用哈希表实现，则空间复杂度为 o(n)
。
查找一个单词：时间复杂度为  o(n)
；空间复杂度为  o(1)
。
查找一个前缀：时间复杂度为 o(n)
；空间复杂度为  o(1)
。


'''
class Node:
    def __init__(self):
        self.isEnd = False
        self.children = dict()

class Trie:
    def __init__(self):
        self.root = Node()

    # 插入逻辑
    def insert(self,word:str) -> None:
        cur = self.root
        for ch in word:
            # 遍历插入
            if ch not in cur.children:
                cur.children[ch] = Node()
            cur = cur.children[ch]
        cur.isEnd = Trie

    # 查找
    def search(self, word:str) -> bool:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]

        # 子节点存在 同时这个子节点被标位end过 字典树是路径形成词 所以需要判断是否点曾经位叶子节点过
        return cur is not None and cur.isEnd

    def startsWith(self,word:str) -> bool:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]

        return cur is not None