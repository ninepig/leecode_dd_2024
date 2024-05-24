import heapq
'''综合性题目 非常牛逼'''

'''
构造函数中：

将所有句子及对应输入次数插入到字典树中。
输入函数中：

使用 path 变量保存当前输入句子的前缀。
如果遇到 #，则将当前句子插入到字典树中。
如果遇到其他字符，用 path 保存当前字符 c。并在字典树中搜索以 path 为前缀的节点的所有分支，将每个分支对应的单词 path 和它们出现的次数 times 存入数组中。然后借助 heapq 进行堆排序，根据出现次数和 ASCII 码大小排序，找出 times 最多的前三个单词。
'''

class Trie:
    def __init__(self):
        self.children = dict()
        self.isEnd = False
        self.Times = 0

    def insert(self, word: str, times = 1)-> None:
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Trie()
            cur = cur.children[ch]
        # insert all content
        cur.isEnd = True
        cur.Times += times

    def search(self,word:str)-> list:
        cur = self

        for ch in word:
            if ch not in cur.children:
                return []
            cur = cur.children[ch]

        # 如果找到了个这个前缀 ,要把他所有可能的path 都加入进来. 所以用一个递归的方法去做
        res = []
        path = [word]
        cur.dfs(res, path)
        return res

    def dfs(self,res:list,path:list):
        cur = self
        if cur.isEnd:
            # 用一个 (-times, path)的形式, 便于 最大堆排序
            res.append((-cur.Times, ''.join(path)))
        for ch in cur.children:
            # dfs 走下所有children
            node = cur.children[ch]
            path.append(ch)
            node.dfs(res,path)
            path.pop()


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.path = ''
        self.exists = True
        self.tire_tree = Trie()
        for i in range(len(sentences)):
            self.tire_tree.insert(sentences[i],times[i])


    def input(self, c: str) -> List[str]:
        if c == "#":
            self.tire_tree.insert(self.path,1)
            self.path = ''
            self.exists = True
            return []
        else:
            self.path += c
            if not self.exists:
                return []
            words = self.tire_tree.search(self.path)
            if words:
                heapq.heapify(words)
                res = []
                while words and len(res)< 3:
                    res.append(heapq.heappop(words)[1])
                return res
            else:
                self.exists = False
                return []