'''
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        prev = ListNode(0)
        prev.next = head
        cur_node = prev
        while cur_node.next and cur_node.next.next:
            a = cur_node.next
            b = a.next
            cur_node.next, a.next, b.next = b, b.next, a
            cur_node = a
        return prev.next
