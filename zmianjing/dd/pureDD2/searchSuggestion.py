import collections
import heapq
from typing import List


## https://leetcode.com/problems/search-suggestions-system/solutions/508775/python-trie-sort-trie-heap


## 自己写的有问题 一开始不知道哪里出错了。。product 继承的时候有问题 ， 如果用str 继承 就不会有问题了 , 没写错
## followup 是 如果有rating， 先按照rating 排序
## 主要是更改 product lt qt 的method
class tire:
    def __init__(self):
        # self.end = False , not need in this case
        self.children = dict()
        self.suggestion = []
    def insert(self,s:str):
        root = self
        for char in s:
            if char not in root.children:
                root.children[char] = tire()
            root = root.children[char]
            root.add_suggestion(s) # in each node, append suggestion
    def insertWithRating(self,s:str,rating:int):
        root = self
        for char in s:
            if char not in root.children:
                root.children[char] = tire()
            root = root.children[char]
            root.add_suggestionwithRating(s,rating) # in each node, append suggestion
    def add_suggestion(self,s):
        if len(self.suggestion) < 3 : ##top k
            heapq.heappush(self.suggestion,HeapProd(s))
        else:
            heapq.heappushpop(self.suggestion,HeapProd(s))

    def add_suggestionwithRating(self,s:str,rating:int):
        if len(self.suggestion) < 3 : ##top k
            heapq.heappush(self.suggestion,HeapProdRating(s,rating))
        else:
            heapq.heappushpop(self.suggestion,HeapProdRating(s,rating))

    ## 因为添加到堆里， 我们排序最高的是在栈底的，所以输出前要reverse
    def get_suggestion(self):
        return sorted(self.suggestion, reverse=True)

class HeapProd(str):
    def __init__(self,s:str):
        self.string = s

    def __lt__(self, other):
        return self.string > other.string ## 最大堆，push smallest to the bottom of heap

    def __eq__(self, other):
        return self.string == other.string

    def __str__(self):
        return self.string

class HeapProdRating():
    def __init__(self,s:str,rating:int):
        self.string = s
        self.rate = rating

    def __lt__(self, other):
        # return self.string > other.string ## 最大堆，push smallest to the bottom of heap
        if self.rate != other.rate:
            return self.rate > other.rate ## > 就是最大堆， 把最小的放到栈底 ， 然后逆序 最大的就在最后，
        else:
            return self.string > other.string
    def __eq__(self, other):
        return self.string == other.string and self.rate == other.rate

    def __str__(self):
        return self.string

class Solution:
    ## in each char input, we will output list of product name
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        tire_node = tire()
        for product in products:
            tire_node.insert(product)

        result, node = [] ,tire_node

        for char in searchWord:
            node = node.children[char]
            # print(node.suggestion)
            result.append(node.get_suggestion()) # for each char input , we will have 3 suggestion

        return result

    def suggestedProductWithRating(self, products: List[str], searchWord: str, rating:List[int]) -> List[List[str]]:
        tire_node = tire()
        for i in range(len(products)):
            tire_node.insertWithRating(products[i],rating[i]) ## 把 rating 一起insert 进去， 排序的时候多考虑一个rating 即可

        result, node = [] ,tire_node

        for char in searchWord:
            node = node.children[char]
            # print(node.suggestion)
            result.append(node.get_suggestion()) # for each char input , we will have 3 suggestion

        return result

class Solution2:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        class TrieNode:
            def __init__(self):
                self.children = collections.defaultdict(TrieNode) ## 给一个default TrieNode 作为value
                self.h = []

            def add_sugesstion(self, product):
                if len(self.h) < 3:
                    heapq.heappush(self.h, MaxHeapStr(product))
                else:
                    heapq.heappushpop(self.h, MaxHeapStr(product))

            def get_suggestion(self):
                return sorted(self.h, reverse=True)

        class MaxHeapStr():
            def __init__(self, string): self.string = string

            def __lt__(self, other): return self.string > other.string

            def __eq__(self, other): return self.string == other.string

            def __str__(self):
                return self.string

        root = TrieNode()
        for p in products:
            node = root
            for char in p:
                node = node.children[char]
                node.add_sugesstion(p)

        result, node = [], root
        for char in searchWord:
            node = node.children[char]
            result.append(node.get_suggestion())
        return result


test = Solution()
products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
rates = [5,4,3,2,1]
searchWord = "mouse"
res = test.suggestedProductWithRating(products,searchWord,rates)
for r in res:
    for item in r:
        print(item)


## pure sorting
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        list_suggested_products = []
        search_word = ''
        for e in searchWord:
            search_word += e
            list_suggested_products.append(self.search(products, search_word))
        return list_suggested_products

    def search(self, products, word):
        index = 0
        for i, w in enumerate(products):
            if word == w[:len(word)]:
                index = i
                break
        similar_elements = []
        for i in range(index, min(index + 3, len(products))):
            if word == products[i][:len(word)]:
                similar_elements.append(products[i])
        return similar_elements