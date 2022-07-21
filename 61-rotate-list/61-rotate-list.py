# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        length = -1
        dummy = ListNode(0)
        dummy.next = head
        print(dummy)
        while dummy:
            length += 1
            dummy = dummy.next
            print(dummy)
        k = k % length
        if k == 0: return head
        print(k)
        dummy = ListNode(0)
        dummy.next = head
        print(dummy)
        for i in range(0, length - k):
            dummy = dummy.next
            print(dummy)
        new_head = ListNode(0)
        new_head.next = dummy.next
        print(new_head)
        dummy.next = None
        
        dummy2 = ListNode(0)
        dummy2 = new_head.next
        print('000',dummy2)
        while dummy2.next:
            dummy2 = dummy2.next
        print('ppp', dummy2)
        dummy2.next = head
        return new_head.next