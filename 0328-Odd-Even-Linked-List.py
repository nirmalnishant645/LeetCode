'''
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL

Note:

    The relative order inside both the even and odd groups should remain as it was in the input.
    The first node is considered odd, the second node even and so on ...

'''
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        odd = head
        even = odd.next
        evenList = even
        
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            
            even.next = odd.next
            even = even.next
            
        odd.next = evenList
        
        return head

# Custom Input Check

node1 = ListNode(10)
node2 = ListNode(20)
node3 = ListNode(30)
node4 = ListNode(40)
node5 = ListNode(50)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

s = Solution()

answer = s.oddEvenList(node1) # 10 => 30 => 50 => 20 => 40

while answer:
    print(answer)
    answer = answer.next