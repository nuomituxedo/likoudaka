# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=self._swapPairs(head)
        return dummy.next
        
    def _swapPairs(self, node):
        if not node or not node.next: return node
        new_head = node.next.next
        a = node
        b = node.next
        b.next = a
        a.next = self.swapPairs(new_head)
        return b