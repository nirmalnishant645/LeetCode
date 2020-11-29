'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
'''
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first = last = head
        for _ in range(n):
            last = last.next
        if not last:
            return first.next
        while last.next:
            last = last.next
            first = first.next
        first.next = first.next.next
        return head

# Check Custom Input

s = Solution()

node1 = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(5)
node4 = ListNode(7)

node1.next = node2
node2.next = node3
node3.next = node4

answer = s.removeNthFromEnd(node1, 2) # 1 => 3 => 7

while answer:
    print(answer.val)
    answer = answer.next