# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = ListNode(0)
        slow.next = head
        fast = ListNode(0)
        fast.next = head
        #move slow and fast to head
        slow = slow.next
        fast = fast.next
        while fast != None and slow.next != None and fast.next!= None:
            slow = slow.next
            fast = fast.next.next
        return slow