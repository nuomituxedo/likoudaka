**Most voted solution:**
public class Solution {
public ListNode swapPairs(ListNode head) {
if ((head == null)||(head.next == null))
return head;
ListNode n = head.next;
head.next = swapPairs(head.next.next);
n.next = head;
return n;
**// original head of each level of recursion always points to the n node in next level of recursion**
}
}