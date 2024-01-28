class Solution:
    '''
    1 bf
    2 prefix + sufix
    3 tire + prefix +suffix ---> trie can boost searching speed from o n to o k
    '''
    def palindromePairsBF(self, words: List[str]) -> List[List[int]]:
        size = len(words)
        ans = []
        for i in range(size):
            for j in range(size):
                if i != j:
                    temp = words[i] + words[j]
                    if temp[::-1] == temp:
                        ans.append([i,j])

        return ans

    ## abc --> if bc's reverse cb in words---> cbabc-->good
    ## ab cc ---> if ab's reverse ba in words--->abccba --->good
    def palindromePairsPreSuffix(self, words: List[str]) -> List[List[int]]:
        ans = []
        size = len(words)
        for i in range(size):
            for j in range(len(words[i])):
                if self.isPalidrome(words[i][:j+1]):
                    temp = words[i][j+1:][::-1] # check the reverse of suffex if exist in dict
                    if temp in words:
                        temp_index = words.index(temp)
                        if temp_index != i and temp_index != -1:# not word it self
                            ans.append([i,temp_index])
                if self.isPalidrome(words[i][j+1:]):
                    temp = words[i][:j+1][::-1]
                    if temp in words:
                        temp_index = words.index(temp)
                        if temp_index != i and temp_index != -1:  # not word it self
                            ans.append([i, temp_index])
        return ans





    def isPalidrome(self,word:str)->bool:
        left , right = 0 , len(word) - 1
        while left < right:
            if word[left] != word[right]:
                return False
            else:
                left += 1
                right -= 1
        return True




class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = dict()
        self.isEnd = False
        self.index = -1


    def insert(self, word: str, index: int) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Trie()
            cur = cur.children[ch]
        cur.isEnd = True
        cur.index = index

    def search(self, word: str) -> int:
        """
        Returns if the word is in the trie.
        """
        cur = self
        for ch in word:
            if ch not in cur.children:
                return -1
            cur = cur.children[ch]

        if cur is not None and cur.isEnd:
            return cur.index
        return -1

class Solution:
    def isPalindrome(self, word: str) -> bool:
        left, right = 0, len(word) - 1
        while left < right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1
        return True

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie_tree = Trie()
        size = len(words)
        for i in range(size):
            word = words[i]
            trie_tree.insert(word, i)

        res = []
        for i in range(size):
            word = words[i]
            for j in range(len(word)):
                if self.isPalindrome(word[:j+1]):
                    temp = word[j+1:][::-1]
                    index = trie_tree.search(temp)
                    if index != i and index != -1:
                        res.append([index, i])
                        if temp == "":
                            res.append([i, index])
                if self.isPalindrome(word[j+1:]):
                    temp = word[:j+1][::-1]
                    index = trie_tree.search(temp)
                    if index != i and index != -1:
                        res.append([i, index])
        return res