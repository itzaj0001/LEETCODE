class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
    

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        temp = self.head
        count = 0

        while count<index and temp:
            temp=temp.next
            count+=1

        if temp:
            return temp.val

        return -1
        

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node

    def addAtTail(self, val: int) -> None:
        node = Node(val)

        if not self.head:
            self.head = node
            return
        
        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = node
        

    def addAtIndex(self, index: int, val: int) -> None:
        if not index:
            self.addAtHead(val)
            return

        node = Node(val)
        temp = self.head
        pos = 0

        while pos < index-1 and temp:
            temp = temp.next
            pos+=1
        
        if not temp:
            return

        node.next = temp.next
        temp.next = node

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return

        if not index:
            self.head = self.head.next
            return
        
        temp = self.head
        pos = 0

        while pos < index-1 and temp.next:
            temp = temp.next
            pos+=1
        
        if not temp.next:
            return

        temp.next = temp.next.next
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)