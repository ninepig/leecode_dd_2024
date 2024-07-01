class MyHashSet:

    def __init__(self):
        self.bucket = 1003
        self.table = [[] for _ in range(self.bucket)] # using array to simulate chainlist-hashtable


    def hash(self,key):
        return key % self.bucket

    def add(self, key: int) -> None:
        hash_key = self.hash(key)
        if key in self.table[hash_key]:
            return
        self.table[hash_key].append(key)


    def remove(self, key: int) -> None:
        hash_key = self.hash(key)
        if key in self.table[hash_key]:
            return
        self.table[hash_key].remove(key)

    def contains(self, key: int) -> bool:
        hash_key = self.hash(key)
        if key in self.table[hash_key]:
            return True
        return False


class MyHashMap:

    def __init__(self):
        self.bucket = 1003
        self.table = [[] for _ in range(self.bucket)]


    def hash(self,key:int):
        return key%self.bucket

    def put(self, key: int, value: int) -> None:
        hash_key = self.hash(key)
        for item in self.table[hash_key]: ## if exist in current hashtable bucket
            if item[0] == key: # found matching key in list
                item[1] = value # update value
                return
        self.table[hash_key].append([key,value]) # if not exit , we append in hashtable bucket's list


    def get(self, key: int) -> int:
        hash_key = self.hash(key)
        for item in self.table[hash_key]:
            if item[0] == key:
                return item[1]
        return -1

    def remove(self, key: int) -> None:
        hash_key = self.hash(key)
        for i,item in enumerate(self.table[hash_key]):
            if item[0] == key: ##locate item
                self.table[hash_key].remove(i) # remov with index of list

