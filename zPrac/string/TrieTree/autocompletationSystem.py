import heapq


class TrieTree:
    def __init__(self):
        self.children = dict()
        self.isEnd = False
        self.times = 0

    ## times 可以是数
    def insert(self,word:str,time:int):
        cur = self
        for ch in word:
            if not self.children[ch]:
                self.children[ch] = TrieTree()
            cur =self.children[ch]
        cur.isEnd = True
        cur.times += time

    def search(self,word:str):
        cur = self
        for ch in word:
            if not self.children[ch]:
                return []
            cur = self.children[ch]
        ans = []
        path = [word]
        self.dfs(cur,ans,path)

    def dfs(self,curNode, ans, path):
        cur = curNode
        if cur.isEnd:
            ans.append((-cur.times,''.join(path)))
        else:
            for ch in cur.children: ## 因为要用到ch,也就是key,所以不用child in cur.children.value,其他时候如果直接要找child节点,可以用values
                node = cur.children[ch]
                path.append(ch)
                self.dfs(node,ans,path)
                path.pop()


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.exist = True
        self.Trie = TrieTree()
        self.path = ""
        for i in range(len(sentences)):
            self.Trie.insert(sentences[i],times[i])

    '''
    ---># means end of insert---> input
    ---> if not # , we search based on char input. if found not exist , no need to keep search, just tell user no
    ---> if we found exist, return top 3 result from trie tree
    '''
    def input(self, c: str) -> List[str]:
        if c == '#': # end of input
            self.Trie.insert(self.path,1)
            self.path = ''
            self.exist = True
        else:
            self.path += c
            # if we already found not exist
            if not self.exist:
                return []
            words = self.Trie.search(self.path)
            if words:
                heapq.heapify(words)
                res = []
                # top 3
                while words and len(res) < 3:
                    res.append(heapq.heappop(words)[1])
                return res
            else:
                self.exist = False
                return []

