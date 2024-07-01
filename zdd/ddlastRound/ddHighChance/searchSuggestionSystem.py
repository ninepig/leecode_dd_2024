'''
这道题对dd而言 就是完成prefix 再搜索
而不是单个都会蹦出来。
所以是字符级别的trie node value
然后找到以后 dfs
根据k 来返回

follow up  1, 按照rating 来排---》 那就要搜索全部了
follow up 是 给一串餐厅的名字和Location，还有User Location，
返回在一定范围内的餐厅名字。 Follow Up因为做不完，就说‍‍一下思路

python的两种 trie 实现方法
1 用array， 对于这个题 如果只用topk个 字典序， 用array的方法简单多了，就是实现起来麻烦些
2 用dict

这两者的区别就是 map 用 not in
array 用 not array[x]
要把变量取出来
'''
from sortedcontainers import SortedDict

class TrieDict:
    def __init__(self):
        self.value = None
        # self.children = SortedDict()
        self.children = dict()  ## 用dict的方式 这样就没办法默认排序了， 也就是加入前k个name 不是排序的 , sortedict可以解决问题
    def insert(self,restName):
        node = self
        for c in restName:
            if c not in node.children:
                c_node = TrieDict()
                node.children[c] = c_node
            node = node.children[c]
        if node.value:
            raise Exception("duplicated")
        node.value = restName
        return True

    def search(self,prefix,k):
        node = self
        for c in prefix:
            if c not in node.children:
                return []
            node = node.children[c]

        res = []
        ## using dfs to find first k element to res
        self.dfs(node,res,k)

        return res

    def dfs(self,node,res,k):
        if node.value :
            if len(res) < k:
                res.append(node.value)
                ## not need to return , we put stuff in res
        else:
            ## 递归找子节点
            for c in node.children:
                child = node.children[c]
                self.dfs(child,res,k)
#

class TrieArray:
    def __init__(self):
        self.value = None
        self.children = [None for _ in range(26)] ## array的方式

    def insert(self, restName):
        node = self
        for c in restName:
            char_idx = ord(c) - ord('a')
            if not node.children[char_idx]:
                c_node = TrieArray()
                node.children[char_idx] = c_node
            node = node.children[char_idx]
        if node.value:
            raise Exception("duplicated")
        node.value = restName
        return True

    def search(self, prefix, k):
        node = self
        for c in prefix:
            char_idx = ord(c) - ord('a')
            if not node.children[char_idx]:
                return []
            node = node.children[char_idx]

        res = []
        ## using dfs to find first k element to res
        self.dfs(node, res, k)

        return res

    def dfs(self, node, res, k):
        if node.value:
            if len(res) < k:
                res.append(node.value)
        else:
            ## dfs to find if any child exist
            for child in node.children:
                if child:
                    self.dfs(child, res, k)
#



class TrieWithRating:
    def __init__(self):
        self.val = None
        self.children = [None for _ in range(26)]
        self.rating = None

    def insert(self,item_name,rating):
        node = self
        for c in item_name:
            c_idx = ord(c) - ord('a')
            if not node.children[c_idx]: ## this char does not exist
                new_trie = TrieWithRating()
                node.children[c_idx] = new_trie
            node = node.children[c_idx]
        ## get last c
        if node.val :
            raise "duplcated input"
        node.val = item_name
        node.rating = rating
        return True

    def search(self,prefix):
        node = self
        for c in prefix:
            c_idx = ord(c) - ord('a')
            if not node.children[c_idx]:
                return []
            node = node.children[c_idx]

        res = []
        self.dfs(node,res)
        return res

    def dfs(self,node,res):
        if node.val:
            res.append((node.rating,node.val))
        else:
            for child in node.children:
                if child:
                    self.dfs(child,res)



class TrieWithLocation:
    def __init__(self):
        self.value = None
        self.children = [None for _ in range(26)]
        self.location = None

    def insert(self,item_name,location):
        node = self
        for c in item_name:
            c_idx = ord(c) - ord('a')
            if not node.children[c_idx]:
                c_node = TrieWithLocation()
                node.children[c_idx] = c_node
            node = node.children[c_idx]

        if node.value:
            raise Exception("item already exist")

        node.value = item_name
        node.location = location
        return True

    def search(self,prefix,userLocation,range):
        node = self
        for c in prefix:
            c_idx = ord(c) - ord('a')
            if not node.children[c_idx]:
                return []
            node = node.children[c_idx]

        res = []
        self.dfs(node,res,userLocation,)
        return res

    def dfs(self, node, res, userLocation, range):
        if node.value and node.location:
            distance = self.distance(userLocation,node.location)
            if distance <= range:
                res.append((distance,node.value))
        else:
            for child in node.children:
                if child:
                    self.dfs(child,res,userLocation,range)

    def distance(self,userLocation,targetLocation):
        return abs(userLocation[0] - targetLocation[0]) + abs(userLocation[1] - targetLocation[1])



# class TrieDictPrac:
#     def __init__(self):
#         self.val = None
#         self.children = dict()
#
#     def insert(self,item_name):
#         node = self
#         for c in item_name:
#             if c not in node.children:
#                 new_trie = TrieDictPrac()
#                 node.children[c] = new_trie
#             node = node.children[c]
#         if node.val:
#             raise Exception("duplicate input")
#         node.val = item_name
#         return True
#
#     def search(self,prefix,top_k):
#         node = self
#         for c in prefix:
#             if c not in node.children:
#                 return []
#             node = node.children[c]
#         res =[]
#         self.dfs(node,res,top_k)
#         return res
#
#     def dfs(self, node,res,top_k):
#         if node.val :
#             if len(res) < top_k:
#                 res.append(node.val)
#         else:
#             for c in node.children.values():
#                 self.dfs(c,res,top_k)


class Solution:
    # def suggestedProducts(self, products:list[str], searchWord: str , k) -> list[str]:
    #     if not products or not searchWord:
    #         return []
    #     help_trie = TrieArrayPrac()
    #     # help_trie = TrieArray()
    #     for product in products:
    #         help_trie.insert(product)
    #
    #     res = help_trie.search(searchWord,3)
    #
    #     return res

    # def suggestedProductsWithRating(self, products:list[str],ratings:list[int], searchWord: str , k) -> list[str]:
    #     if not products or not searchWord:
    #         return []
    #     help_trie = TrieWithRating()
    #     for i in range(len(products)):
    #         help_trie.insert(products[i],ratings[i])
    #     res = help_trie.search(searchWord)
    #     ## if we need sort rating, we have to search all tree, then sort res
    #     res.sort(key = lambda x:(-x[0],x[1]))
    #     return res[0:k]

    # follow up 是 给一串餐厅的名字和Location，还有User Location，返回在一定范围内的餐厅名字。 Follow Up因为做不完，就说一下思路。
    def suggestedProductsWithRating(self, products:list[str],location:list[list[int]], userlocation:list[int],searchWord: str, k,range_int) -> list[str]:
        if not products or not searchWord:
            return []
        help_trie = TrieWithLocation()
        for i in range(len(products)):
            help_trie.insert(products[i],location[i])
        res = help_trie.search(searchWord,userlocation,range_int)
        ## if we need sort distance, we have to search all tree, then sort res name
        res.sort(key = lambda x:(x[0],x[1]))
        return res[0:k]

if __name__ == "__main__":
    sol = Solution()
    test = ["abc","aaa","bbb","addd","aba"]
    rating = [5,5,3,2,1]
    search = "a"
    print(sol.suggestedProductsWithRating(test,rating,search,3))


