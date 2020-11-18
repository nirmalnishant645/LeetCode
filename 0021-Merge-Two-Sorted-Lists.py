'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Iterative
#Time Complexity - O(n+m), Space Complexity - O(1)
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        head = cur_node = ListNode()
        
        while l1 and l2:
            
            if l1.val < l2.val:
                cur_node.next = l1
                l1 = l1.next
                
            else:
                cur_node.next = l2
                l2 = l2.next
                
            cur_node = cur_node.next
        
        cur_node.next = l1 or l2
        
        return head.next

#Recursive
#Time Complexity - O(n+m), Space Complexity - O(n+m)
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2: return l1 or l2
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l2.next, l1)
            return l2
