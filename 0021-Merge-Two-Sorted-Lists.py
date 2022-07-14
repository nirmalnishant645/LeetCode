'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = None

#Iterative
#Time Complexity - O(n+m), Space Complexity - O(1)

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur_node = pre_node = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur_node.next = list1
                list1 = list1.next
            else:
                cur_node.next = list2
                list2 = list2.next
            cur_node = cur_node.next
        cur_node.next = list1 if list1 else list2
        return pre_node.next

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

# Custom Input Check 

s = Solution()

l1_1 = ListNode(1)
l1_2 = ListNode(2)
l1_3 = ListNode(4)

l1_1.next = l1_2
l1_2.next = l1_3

# l1: 1 => 2 => 4

l2_1 = ListNode(1)
l2_2 = ListNode(3)
l2_3 = ListNode(4)

l2_1.next = l2_2
l2_2.next = l2_3

# l2: 1 => 3 => 4

answer = s.mergeTwoLists(l1_1, l2_1)

while answer:
    print(answer.val)
    answer = answer.next