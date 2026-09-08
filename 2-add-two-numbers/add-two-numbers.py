# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy

        p1, p2 = l1, l2
        carry = 0

        while p1 and p2:
            x, y  = p1.val, p2.val
            
            summ = x + y + carry
            carry = summ // 10
            node = ListNode(summ%10)
            curr.next = node
            curr = node
            p1, p2 = p1.next, p2.next

        while p1 or p2 or carry:

            if not p1 and not p2:
                node = ListNode(carry)
                curr.next = node
                break

            elif not p1:
                x, y  = 0, p2.val
                summ = x + y + carry
                carry = summ // 10
                node = ListNode(summ%10)
                curr.next = node
                curr = node
                p2 = p2.next
            else:
                x, y  = p1.val, 0
                summ = x + y + carry
                carry = summ // 10
                node = ListNode(summ%10)
                curr.next = node
                curr = node
                p1 = p1.next
        

        return dummy.next
            



        