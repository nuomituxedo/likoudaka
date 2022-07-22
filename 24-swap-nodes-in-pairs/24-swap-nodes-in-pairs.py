# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        
        #swap two nodes at a time and recursion with the next node
        a = head #first node
        b = head.next #second node
        c = head.next.next #third node
        
        #let the first node point to the third node
        #the third node passed in the next recursive call
        a.next = self.swapPairs(c)
        #let the second node point to the first node (backtracking)
        b.next = a
        return b
        
    