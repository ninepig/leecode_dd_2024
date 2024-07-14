class Trie:
    def __init__(self):
        ## need 2 field, since that is a recommenadation or we can only use value node , use that to judge if exists
        self.value = ""
        self.isWord = False
        ## lowercase only need confirm with interview
        self.children = dict()

    def insert(self, name):
        node = self
        for c in name:
            if c not in node.children:
                cur_node = Trie()
                node.children[c] = cur_node
            node = node.children[c]

        node.isWord = True
        node.value = name
        return True

    def search(self, name):
        node = self
        # print(type(node))
        for c in name:
            if c not in node.children:
                raise ("no result , does not exist")
            node = node.children[c]
        res = []
        self.dfs(node, res)

        return res

    def dfs(self, node, res):
        if node.isWord is True:
            # if len(res) < k:
                res.append(node.value)
        else:
            ##TODO eye one this !!如果是dict， 就要用value 来获取所有的node
            for child in node.children.values():
                if child:
                    self.dfs(child, res)


class solution:
    def __init__(self, res_name):
        self.TrieTree = Trie()
        for i in range(len(res_name)):
            self.TrieTree.insert(res_name[i])

    def suggestedProducts(self, name, k):
        # res = self.TrieTree.search(name)
        # return sorted(res)[:k]
        res = self.TrieTree.search(name)
        res.sort()
        return res[:k]

class TrieWithRating:
    def __init__(self):
        self.val = None
        self.children = dict()
        self.rating = None

    def insert(self, item_name, rating):
        node = self
        for c in item_name:
            if c not in node.children:  ## this char does not exist
                new_trie = TrieWithRating()
                node.children[c] = new_trie
            node = node.children[c]
        ## get last c
        if node.val:
            raise Exception("duplcated input")
        node.val = item_name
        node.rating = rating
        return True

    def search(self, prefix):
        node = self
        for c in prefix:
            if c not in node.children:
                return []
            node = node.children[c]

        res = []
        self.dfs(node, res)
        return res

    def dfs(self, node, res):
        ## make sure rating is there
        if node.val and node.rating:
            res.append((node.rating, node.val))
        else:
            for child in node.children.values():
                if child:
                    self.dfs(child, res)


class solution2:
    def __init__(self, res_name, rating):
        self.TrieTree = TrieWithRating()
        for i in range(len(res_name)):
            self.TrieTree.insert(res_name[i], rating[i])

    def suggestedProducts(self, name, k):
        root = self.TrieTree
        res = root.search(name)
        return sorted(res, key=lambda x: (-x[0], x[1]))


test = ["abc", "aaa", "bbb", "addd", "aba"]
rating = [5, 5, 3, 2, 1]
search = "a"
sol = solution(test)
print(sol.suggestedProducts(search, 3))

sol = solution2(test, rating)
print(sol.suggestedProducts(search, rating))


class TrieWithLocation:
    def __init__(self):
        self.value = None
        self.children = dict()
        self.location = None

    def insert(self, item_name, location):
        node = self
        for c in item_name:
            if c not in node.children:
                c_node = TrieWithLocation()
                node.children[c] = c_node
            node = node.children[c]

        if node.value:
            raise Exception("item already exist")

        node.value = item_name
        node.location = location
        return True

    def search(self, prefix, userLocation, range):
        node = self
        for c in prefix:
            if c not in node.children:
                return []
            node = node.children[c]

        res = []
        self.dfs(node, res, userLocation,range)
        return res

    def dfs(self, node, res, userLocation, range):
        if node.value and node.location:
            distance = self.distance(userLocation, node.location)
            if distance <= range:
                res.append((distance, node.value))
        else:
            for child in node.children:
                if child:
                    self.dfs(child, res, userLocation, range)

    def distance(self, userLocation, targetLocation):
        return abs(userLocation[0] - targetLocation[0]) + abs(userLocation[1] - targetLocation[1])

## todo no test did
## todo char level recommdendation?

