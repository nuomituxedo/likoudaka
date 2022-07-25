# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = {} # dict
        index = 0
        while head and head not in visited:
            visited[head] = index
            head = head.next
            index += 1
        return head