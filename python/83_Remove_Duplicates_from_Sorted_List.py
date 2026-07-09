# 83. Remove Duplicates from Sorted List
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Difficulty: Easy | Language: python3 | Runtime: 3 ms | Memory: 17.7 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        lets_go = ListNode(head.val)
        lets_go_head = lets_go
        while head.next != None:
            next_node = head.next
            if head.val != next_node.val:
                lets_go.next = ListNode(next_node.val)
                lets_go = lets_go.next
            head = head.next    
        return lets_go_head
