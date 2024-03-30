'''
面经似乎只有2个
https://www.1point3acres.com/bbs/thread-1050277-1-1.html
follow up 很蠢
有点无语： coding round 但是感觉在考sd ：一开始没有反应过来interviewer 想聊啥，
一直在optimize trie （让每个node 记住所有的leaf node）， 最后10分钟，interviewer 说这个现实中会pass 这个restaurant parameter 吗？ 然后才发现interviewer是想聊implement auto complete system。。。就讲了offline sync + db choice + cache + load balancer
follow yp
加上rating 来做

解法
1 sort --》 search
2 trie
    trie + pq--> in each trie node, we maintain a PQ. we store top 3 candidate
    trie的关键是 对于每个节点我们都加入 suggestion
    而不是传统的在search word 结束加入 type hint system

'''
import heapq
from typing import List


class trie:
    def __init__(self):
        self.children = dict()
        self.suggestion = []

    def insert(self,product:str):
        node = self
        for c in product:
            if c not in node.children:
                node.children[c] = trie()
            node = node.children[c]
            node.add_suggestion(product) ## each node in trie, we need add product , and use

    def get_suggestion(self):
        return sorted(self.suggestion,reverse=True) # we reverse the suggestion and output that

    def add_suggestion(self,name:str):
        if len(self.suggestion) < 3 :
            heapq.heappush(self.suggestion,product(name))
        else:
            # heapq.heappop(self.suggestion)
            # heapq.heappush(self.suggestion,product(name))
            # heapq.heappushpop(self.suggestion,product(name))
            heapq.heappush(self.suggestion,product(name))
            heapq.heappop(self.suggestion)

    def insertwithrate(self, product: str,rate:int):
        node = self
        for c in product:
            if c not in node.children:
                node.children[c] = trie()
            node = node.children[c]
            node.add_suggestion_rate(product,rate)  ## each node in trie, we need add product , and use


    def add_suggestion_rate(self, name: str,rate):
        if len(self.suggestion) < 3:
            heapq.heappush(self.suggestion, productwithrate(name,rate))
        else:
            # heapq.heappop(self.suggestion)
            # heapq.heappush(self.suggestion,product(name))
            # heapq.heappushpop(self.suggestion,product(name))
            heapq.heappush(self.suggestion, productwithrate(name,rate))
            heapq.heappop(self.suggestion)

class product:
    def __init__(self,name:str):
        self.name = name

    def __lt__(self, other):
        return self.name > other.name ## we maintain a max heap, which means, lex high order will be in top of heap

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return self.name


class productwithrate:
    def __init__(self,name:str,rate:int):
        self.name = name
        self.rate = rate

    def __lt__(self, other):
        if self.rate != other.rate:
            return self.rate < other.rate ## we need large rating, so smaller should be top , pop out
        else:
            return self.name > other.name ## we maintain a max heap, which means, lex high order will be in top of heap

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return self.name + str(self.rate)
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        if not products or len(products) == 0:
            return []
        products.sort()
        res = []
        prefix = ""
        for c in searchWord:
            prefix += c
            res.append(self.searchByPrefix(prefix,products))

        return res
    ## we have sorted product name , we use prefix to find 3 name after first prefix item
    def searchByPrefix(self, prefix, products):
        index = 0
        for idx,name in enumerate(products):
            if prefix == name[:len(prefix)]:
                index = idx
                break
        res = []
        for i in range(index,min(index + 3, len(products))): ## either 3 after idx or end of target
            if prefix == products[i][:len(prefix)] : ##double confirm has same prefix to avoid problem
                res.append(products[i])

        return res

    def suggestedProductsWithTrie(self, products: List[str], searchWord: str) -> List[List[str]]:
        help_trie = trie()
        for item in products:
            help_trie.insert(item)

        res = []
        node = help_trie

        for c in searchWord:
            node = node.children[c] ## using trie's char child to get suggestion directly
            res.append(node.get_suggestion())

        return res

    def suggestedProductsRateWithTrie(self, products: List[str],rate:List[int], searchWord: str) -> List[List[str]]:
        help_trie = trie()
        # for item in products:
        #     help_trie.insert(item)
        for i in range(len(products)):
            help_trie.insertwithrate(products[i],rate[i])

        res = []
        node = help_trie

        for c in searchWord:
            node = node.children[c] ## using trie's char child to get suggestion directly
            res.append(node.get_suggestion())

        return res

if __name__ == '__main__':
    test = Solution()
    products = ["mobile","mouse","moneypot","monitor","mousepad"]
    rates = [5, 4, 3, 2, 1]
    # products.sort()
    # print(products)
    searchWord = "mouse"
    # print(test.suggestedProducts(products,searchWord))
    # for items in test.suggestedProductsWithTrie(products,searchWord):
    #     for item in items:
    #         print(item)
    for items in test.suggestedProductsRateWithTrie(products,rates,searchWord):
        for item in items:
            print(item)