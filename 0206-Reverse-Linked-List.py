'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Iteratively
# Time Complexity - O(n), Space Complexity - O(1)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur_node = head
        while cur_node:
            cur_node.next, prev, cur_node = prev, cur_node, cur_node.next
        return prev
