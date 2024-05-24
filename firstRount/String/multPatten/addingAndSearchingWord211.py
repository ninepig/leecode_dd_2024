

class Trie:

    def __init__(self):
        self.children = dict()
        self.isEnd = True


    def insert(self, word: str) -> None:
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Trie()
            cur = cur.children[ch]
        cur.isEnd = True

    ## 嵌套函数
    ## 因为出现了 '.' 这个情况. 所以需要dfs走下去.
    def search(self, word: str) -> bool:

        # def dfs(index, node) -> bool:
        #     if index == len(word):
        #         return node.isEnd
        #     ch = word[index]
        #     if ch == '.':
        #         for child in node.children.value():
        #             if child is not None and dfs(index + 1 , child):
        #                 return True
        #     else:
        #         if ch not in node.children:
        #             return False
        #         child = node.children[ch]
        #         if child is not None and dfs(index + 1 , child):
        #             return True
        #     return False
        #
        # return dfs(0,self)

        # 通配符 search
        def dfs(index,node)->bool:
            if index == len(word):
                return node.isEnd
            ch = word[index]
            if ch == '.':
                for child in node.children.values():
                    if child is not None and dfs(index + 1 , child):
                        return True
            else:
                if ch not in node.children:
                    return  False
                child = node.children[ch]
                if child is not None and dfs(index + 1, child):
                    return True

            return False

        return dfs(0,self)




class WordDictionary:

    def __init__(self):
        self.Trie_tree = Trie()


    def addWord(self, word: str) -> None:
        return self.Trie_tree.insert(word)

    def search(self, word: str) -> bool:
        return self.Trie_tree.search(word)
