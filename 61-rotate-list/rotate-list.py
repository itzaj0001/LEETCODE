# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def count(self, head):
        temp = head
        count = 0 

        while temp:
            count+=1
            temp = temp.next
        return count

    def reverse(self,head):
        temp = head
        prev = None
        while temp:
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt
        return prev

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        length = self.count(head)

        k = k % length

        if k == 0:
            return head
        
        r = self.reverse(head) 

        temp = r
        curr = None

        while k > 0:
            curr = temp
            temp = temp.next
            k-=1

        curr.next = None
        new_head = temp

        while temp.next:
            temp = temp.next
        temp.next = r

        new_head = self.reverse(new_head)
        return new_head
        

        