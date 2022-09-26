class MapSum:

    def __init__(self):
        self.map={}

    def insert(self, key: str, val: int) -> None:
        self.map[key] = val

    def sum(self, prefix: str) -> int:
        total = 0
        for key in self.map.keys():
            if key.startswith(prefix):
                total += self.map[key]
        return total


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)