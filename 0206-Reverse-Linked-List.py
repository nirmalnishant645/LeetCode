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
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Iteratively
# Time Complexity - O(n), Space Complexity - O(1)

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, res = head, None
        while cur:
            cur.next, res, cur = res, cur, cur.next
        return res

# Recursively
#Time Complexity - O(n), Space Complexity - O(n)

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        reversedList = self.reverseList(head.next)
        head.next.next, head.next = head, None
        return reversedList
