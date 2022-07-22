Claire - Simplefied:
​
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
Claire after hint (recursion) 7/21/2022
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
​
​
**Most voted solution:**
public class Solution {
public ListNode swapPairs(ListNode head) {