class MyHashSet:

    def __init__(self):
        self.myset = [[] for i in range(0,10)]
        

    def add(self, key: int) -> None:
        index = key%10
        if key not in self.myset[index]:
            self.myset[index].append(key)
        

    def remove(self, key: int) -> None:
        index = key%10
        if key in self.myset[index]:
            self.myset[index].remove(key)
        

    def contains(self, key: int) -> bool:
        index = key%10
        return (key in self.myset[index])
           

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)