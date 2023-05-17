# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []

        while head:
            arr.append(head.val)
            head = head.next
        
        i, j = 0, len(arr)-1
        Max = 0

        while i < j:
            pair = arr[i] + arr[j]
            Max = max(Max, pair)
            i+=1
            j-=1

        return Max

