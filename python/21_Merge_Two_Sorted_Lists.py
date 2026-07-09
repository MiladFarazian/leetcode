# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/
# Difficulty: Easy | Language: python3 | Runtime: 3 ms | Memory: 17.9 MB

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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        list3 = dummy_head
        while list1 or list2:
            if list1 is None:
                list3.next = ListNode(list2.val)
                list3 = list3.next
                list2 = list2.next
            elif list2 is None:
                list3.next = ListNode(list1.val)
                list3 = list3.next
                list1 = list1.next
            else:
                if list1.val <= list2.val:
                    list3.next = ListNode(list1.val)
                    list3 = list3.next
                    list1 = list1.next
                else:
                    list3.next = ListNode(list2.val)
                    list3 = list3.next
                    list2 = list2.next
        print_list(dummy_head)
        return dummy_head.next
