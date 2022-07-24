set:
if we have two listNodes containing the same values will appear twice because they are object. However if we have two primitive values that are equal, set will only keep one of them.
---
** Approach: hashset**
Time complexity : O(m+n)O(m+n).
Space complexity : O(m)O(m) or O(n)O(n).
​
public class Solution {
public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
Set<ListNode> set =new HashSet<>();
while (headA!=null){
set.add(headA);
headA = headA.next;
}
while (headB!=null){
if (set.contains(headB)) return headB;
headB = headB.next;
}
return null;
}
}
-------
Memorize this approach:
//approach: two pointers
//time complexity: O(m + n)
//space complexity: O(1)
**Why the while loop stops after the 2nd iteration???**
**->after 2nd iteration, both pointers point to null, so (a ==b), loop terminates.**
public class Solution {
public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
//boundary check
if(headA == null || headB == null) return null;
​
ListNode a = headA;
ListNode b = headB;
​
//if a & b have different len, then we will stop the loop after second iteration
while( a != b){
//for the end of first iteration, we just reset the pointer to the head of another linkedlist
a = a == null? headB : a.next;
b = b == null? headA : b.next;
}
​
return a;
}
}