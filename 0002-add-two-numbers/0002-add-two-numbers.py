# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        newList = head = ListNode()

        while l1 or l2:
            total = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            if total >= 10:
                carry = 1
                total -= 10
            else:
                carry = 0
            newList.next = ListNode(total)
            newList = newList.next
            l1, l2 = (l1.next if l1 else None), (l2.next if l2 else None)

        newList.next = (ListNode(1) if carry else None)

        return head.next




        

        