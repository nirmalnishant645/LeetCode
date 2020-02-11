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
        
        slow = fast = prev_slow = head
        
        mid = self.midNode(slow, fast, prev_slow)
        
        second_head = self.reverse(mid)
        
        while head:
            if head.val != second_head.val:
                return False
            head, second_head = head.next, second_head.next
        return True
    
    def midNode(self, slow, fast, prev_slow):
        while fast and fast.next:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next
        if fast != None:
            slow = slow.next
        prev_slow.next = None
        return slow
    
    def reverse(self, head_node):
        prev = None
        while head_node:
            head_node.next, prev, head_node = prev, head_node, head_node.next
        return prev
