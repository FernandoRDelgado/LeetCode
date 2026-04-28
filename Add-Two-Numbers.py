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
12        node1 = l1
13        node2 = l2
14        
15        head = ListNode((node1.val + node2.val) % 10)
16        result = head
17        
18        if node1 != None and node2 != None and node1.val + node2.val > 9:
19            carry = 1
20
21        node1 = node1.next
22        node2 = node2.next
23        
24        while ((node1 != None or node2 != None) or carry == 1):
25            if node1 != None:
26                summation += node1.val
27                node1 = node1.next
28            if node2 != None:
29                summation += node2.val
30                node2 = node2.next
31            summation = summation + carry
32            
33            if summation > 9:
34                carry = 1
35            else:
36                carry = 0
37            
38            summation = summation % 10
39
40            result.next = ListNode(summation)
41            result = result.next
42            
43            summation = 0
44        
45        return head
46