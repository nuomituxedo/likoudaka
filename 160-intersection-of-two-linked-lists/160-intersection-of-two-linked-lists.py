# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dummyA=ListNode(0)
        dummyB=ListNode(0)
        dummyA.next = headA
        dummyB.next = headB
        while headA or headB:
            if headA == headB:
                return headA
            headA = headA.next if headA else dummyB.next
            headB = headB.next if headB else dummyA.next
        return None