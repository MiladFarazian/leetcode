# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/
# Difficulty: Medium | Language: python3 | Runtime: 3 ms | Memory: 17.8 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def print_list(head):
    current = head
    while current:
        print(current.val)
        current = current.next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #print_list(l1)
        #print_list(l2)
        sum = 0
        carry = 0
        dummy_head = ListNode()
        l3 = dummy_head
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum = val1 + val2 + carry
            carry = sum // 10
            digit = sum % 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            l3.next = ListNode(digit)
            l3 = l3.next
        return dummy_head.next
