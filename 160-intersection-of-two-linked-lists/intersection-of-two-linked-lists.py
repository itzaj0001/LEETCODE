# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = set()
        temp = headA

        while temp:
            a.add(temp)
            temp = temp.next

        temp = headB
        while temp:
            if temp in a:
                return temp
            temp = temp.next
        return None
        

        

        