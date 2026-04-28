1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6import string
7
8class Solution:
9    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
10        summation = 0
11        carry = 0
12        
13        head = ListNode((l1.val + l2.val) % 10)
14        result = head
15        
16        if l1 != None and l2 != None and l1.val + l2.val > 9:
17            carry = 1
18
19        l1 = l1.next
20        l2 = l2.next
21        
22        while ((l1 != None or l2 != None) or carry == 1):
23            if l1 != None:
24                summation += l1.val
25                l1 = l1.next
26            if l2 != None:
27                summation += l2.val
28                l2 = l2.next
29            summation = summation + carry
30            
31            if summation > 9:
32                carry = 1
33            else:
34                carry = 0
35            
36            summation = summation % 10
37
38            result.next = ListNode(summation)
39            result = result.next
40            
41            summation = 0
42        
43        return head
44