# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        temp = head

        while temp:
            nxt = temp.next
            prev = dummy
            curr = dummy.next

            while curr:
                if temp.val < curr.val:
                    break
                prev = curr
                curr = curr.next

            prev.next = temp
            temp.next = curr
            temp = nxt
            
        return dummy.next
                
            

        