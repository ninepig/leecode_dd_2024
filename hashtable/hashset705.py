class MyHashSet:

    def __init__(self):
        self.bucket = 1000
        self.hashSet = [[] for _ in range(self.bucket)]

    def hash(self, key):
        return key % self.bucket

    def add(self, key: int) -> None:
        hash_key = self.hashSet(key)
        if key in self.hashSet[hash_key]:
            return False
        self.hashSet[hash_key].append(key)

    def remove(self, key: int) -> None:
        hash_key = self.hash(key)
        if key not in self.table[hash_key]:
            return
        self.table[hash_key].remove(key)


    def contains(self, key: int) -> bool:
        hash_key = self.hash(key)
        return key in self.hashSet(hash_key)
