class TrieNode:
    def __init__(self):
        self.children = dict()
        self.value = 0
        self.isEnd = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str, value: int) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.value = value
        cur.isEnd = True


    def search(self, word: str) -> int:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                return 0
            cur = cur.children[ch]
        return self.dfs_calc_value(cur)

    # 因为已经是找到prefix了 所以只需要把所有的子节点的值都找出来即可
    def dfs_calc_value(self, root) -> int:
        if not root: return 0
        res = root.value
        for node in root.children.values():
            res += self.dfs_calc_value(node)

        return res




'''
MapSum() 初始化 MapSum 对象。
void insert(String key, int val) 插入 key-val 键值对，字符串表示键 key，整数表示值 val。如果键 key 已经存在，那么原来的键值对将被替代成新的键值对。
int sum(string prefix) 返回所有以该前缀 prefix 开头的键 key 的值的总和。
'''
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie_tree = Trie()


    def insert(self, key: str, val: int) -> None:
        self.trie_tree.insert(key,val)


    def sum(self, prefix: str) -> int:
        return self.trie_tree.search(str)
