1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
9        summation = 0
10        carry = 0
11        
12        head = ListNode((l1.val + l2.val) % 10)
13        result = head
14        
15        if l1 != None and l2 != None and l1.val + l2.val > 9:
16            carry = 1
17
18        l1 = l1.next
19        l2 = l2.next
20        
21        while ((l1 != None or l2 != None) or carry == 1):
22            if l1 != None:
23                summation += l1.val
24                l1 = l1.next
25            if l2 != None:
26                summation += l2.val
27                l2 = l2.next
28            summation = summation + carry
29            
30            if summation > 9:
31                carry = 1
32            else:
33                carry = 0
34            
35            summation = summation % 10
36
37            result.next = ListNode(summation)
38            result = result.next
39            
40            summation = 0
41        
42        return head
43