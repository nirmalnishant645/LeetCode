'''
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list. 

Follow up:

Can you solve it using O(1) (i.e. constant) memory?
'''

# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Hare Tortoise Algorithm

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# Custom Input Check

s = Solution()

node1 = ListNode(1)
node2 = ListNode(5)
node3 = ListNode(11)
node4 = ListNode(8)
node5 = ListNode(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node2

answer = s.hasCycle(node1)

print(answer)