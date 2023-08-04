from typing import Any


class Item:
    def __init__(self, key: Any, value: Any):
        self.key: Any = key
        self.value: Any = value


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table: list[Any] = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def __setitem__(self, __name: Any, __value: Any) -> None:
        hash = self._hash_function(__name)
        items = self.table[hash]
        for item in items:
            if item.key == __name:
                return
        self.table[hash].append(Item(__name, __value))

    def __getitem__(self, __name: Any) -> Any:
        hash = self._hash_function(__name)
        items = self.table[hash]
        for item in items:
            if item.key == __name:
                return item.value
        raise KeyError(f"Could not find key {__name}")

    def __delitem__(self, __name: Any) -> None:
        hash = self._hash_function(__name)
        items = self.table[hash]
        for key, item in enumerate(items):
            if item.key == __name:
                del items[key]
                return
        raise KeyError(f"Could not find key {__name}")

    def __iter__(self):
        for buckets in self.table:
            for item in buckets:
                yield (item.key, item.value)


if __name__ == "__main__":
    ht = HashTable(3)
    ht[2] = 20
    ht[5] = 50
    ht["name"] = "Matheus"
    print({k: v for k, v in ht})
    del ht["name"]
    print({k: v for k, v in ht})
