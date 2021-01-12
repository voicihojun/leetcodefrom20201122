class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = {}

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        if value < 0:
            print("value need to be non-negative")
            return
        self.hashmap[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key in self.hashmap.keys():
            return self.hashmap[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.hashmap.keys():
            del self.hashmap[key]