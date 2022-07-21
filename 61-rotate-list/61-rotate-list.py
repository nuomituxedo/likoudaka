# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #return if head is empty
        if not head: return None
        
        #find out the total number of nodes in the linkedlist
        #apply modulo to k to get the actual number of rotations needed
        length = -1
        dummy = ListNode(0)
        dummy.next = head
        while dummy:
            length += 1
            dummy = dummy.next
        k = k % length
        #if no rotation is needed, directly return head
        if k == 0: return head
        
        # 1. create a dummy node, travel the list nodes to the node to be cut (new end)
        # 2. after this operation we end up with 2 smaller linkedlists
        dummy = ListNode(0)
        dummy.next = head
        for i in range(0, length - k):
            dummy = dummy.next
        new_head = ListNode(0)
        new_head = dummy.next # new_head points to the new head node
        
        dummy.next = None #make dummy the end node, now we have 2 linkedlists
        
        #3. create dummy2 to point to the second linkedlist and travel to its end node
        dummy2 = ListNode(0)
        dummy2 = new_head
        
        while dummy2.next:
            dummy2 = dummy2.next
        
        #4. now relink the two linkedlists
        dummy2.next = head
        return new_head