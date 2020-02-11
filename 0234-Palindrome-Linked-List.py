'''
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        slow = fast = prevSlow = head
        while fast and fast.next:
            prevSlow = slow
            slow = slow.next
            fast = fast.next.next
        if fast != None:
            slow = slow.next
        prevSlow.next = None
        prev = None
        cur_node = slow
        while cur_node:
            cur_node.next, prev, cur_node = prev, cur_node, cur_node.next
        while head:
            if head.val != prev.val:
                return False
            head, prev = head.next, prev.next
        return True
        
