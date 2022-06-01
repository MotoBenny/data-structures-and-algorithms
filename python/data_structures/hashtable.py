from data_structures.linked_list import LinkedList


class Hashtable:

    def __init__(self, size=1024):
        self.size = size
        self.buckets = [None] * self.size

    def hash(self, key):
        sum_of_chars = 0
        if type(key) is str:
            for char in key:
                sum_of_chars += ord(char)
        elif type(key) is int:
            sum_of_chars = key
        primed = sum_of_chars * 599
        index = primed % self.size

        return index

    def set(self, key, value):
        hash_index = self.hash(key)
        bucket = self.buckets[hash_index]
        if bucket is None:
            self.buckets[hash_index] = LinkedList()
        self.buckets[hash_index].insert((key, value))

    def get(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]
        current = bucket.head
        while current:
            pair = current.value
            curr_key = pair[0]
            if curr_key == key:
                return pair[1]
            current = current.next
        return None

    def contains(self, key):
        idx = self.hash(key)
        bucket = self.buckets[idx]

        if bucket is None:
            return False

        current = bucket.head

        while current:
            if current.value[0] == key:
                return True
            current = current.next
        return False

    def keys(self):
        key_collection = set()
        for bucket in self.buckets:
            if bucket is not None:
                current = bucket.head
                while current:
                    pair = current.value
                    current_key = pair[0]
                    key_collection.add(current_key)
                    current = current.next
        return key_collection
