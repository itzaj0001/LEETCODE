class MyHashMap:

    def __init__(self):
        self.myset = [[] for i in range(0,10)]

    def put(self, key: int, value: int) -> None:
        index = key%10
        for i in range(len(self.myset[index])):
            if self.myset[index][i][0] == key:
                self.myset[index][i] = (key,value)
                return   
        self.myset[index].append((key,value))
            

    def get(self, key: int) -> int:
        index = key%10
        for i in range(len(self.myset[index])):
            if self.myset[index][i][0]==key:
                return self.myset[index][i][1]
        return -1
        

    def remove(self, key: int) -> None:
        index = key%10
        for i in range(len(self.myset[index])):
            if self.myset[index][i][0]==key:
                self.myset[index].pop(i)
                return
                
        
            
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

       
           

        

