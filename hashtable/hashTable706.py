class MyHashMap:

    def __init__(self):
        self.bucket = 1003
        self.hashTable = [[] for _ in range(self.bucket)]

    def hash(self, key):
        return key % self.bucket


    def put(self, key: int, value: int) -> None:
        key_hash = self.hash(key)
        for item in self.hashTable[key_hash]:
            if key in item[0]:
                item[1] = value
                return
        self.hashTable[key_hash].append([key,item])


    def get(self, key: int) -> int:
        key_hash = self.hash(key)
        for item in self.hashTable[key_hash]:
            if key in item[0]:
                return item[1]
        return -1

    def remove(self, key: int) -> None:
        key_hash = self.hash(key)
        # enumerate 可以带出index，便于pop
        for i, item in enumerate(self.hashTable):
            if key == item[0]:
                self.hashTable[key_hash].pop(i)
                return 