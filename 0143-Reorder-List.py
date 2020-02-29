'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        last = None
        while slow:
            slow.next, last, slow = last, slow, slow.next
            
        cur = head
        while last.next:            
            cur_next = cur.next
            last_next = last.next
            cur.next = last
            cur = cur_next
            last.next = cur
            last = last_next
