'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Method 1

class Solution:
    
    def mergeTwoLists(self, l1, l2):
        res = cur = ListNode()
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return res.next
        
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        last = len(lists) - 1
        while last:
            i, j = 0, last
            while i < j:
                lists[i] = self.mergeTwoLists(lists[i], lists[j])
                i += 1
                j -= 1
                last -= 1
        return lists[0]