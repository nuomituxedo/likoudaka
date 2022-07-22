# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        cur=ListNode(0)
        cur.next=self._swapPairs(head)
        return cur.next
        
    def _swapPairs(self, node):
        if not node: return None
        if not node.next: return node
        new_head = node.next.next
        a = node
        b = node.next
        b.next = a
        a.next = self.swapPairs(new_head)
        return b