# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        if not head.next:
            return True
        if not head.next.next:
            if head.val == head.next.val:
                return True
            return False

        slow = fast = head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        
        temp = slow
        prev = None
        while temp != None:
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt
        
        curr = head
        while prev and curr:
            if prev.val != curr.val:
                return False
            prev = prev.next
            curr = curr.next
        return True



        
        
        
        