'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Iteratively
# Time Complexity - O(n), Space Complexity - O(1)

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, res = head, None
        while cur:
            cur.next, res, cur = res, cur, cur.next
        return res

# Iteratively by making a new previous node
# Time Complexity - O(n), Space Complexity - O(1)

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, res = head, ListNode()
        while cur:
            cur.next, res.next, cur = res.next, cur, cur.next
        return res.next

# Recursively
#Time Complexity - O(n), Space Complexity - O(n)

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        reversedList = self.reverseList(head.next)
        head.next.next, head.next = head, None
        return reversedList

# Custom Input Check

s = Solution()

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

answer = s.reverseList(node1)

while answer:
    print(answer.val)
    answer = answer.next
