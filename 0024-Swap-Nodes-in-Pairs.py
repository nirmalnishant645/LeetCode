'''
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        temp = ListNode()
        temp.next = head
        cur = temp
        
        while cur.next and cur.next.next:
            cur.next.next, cur.next, cur.next.next = cur.next.next.next, cur.next.next, cur.next
            cur = cur.next.next
        
        return temp.next
