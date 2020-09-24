'''
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive Solution
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.recursive(root, res)
        return res
    
    def recursive(self, root, res):
        if not root:
            return
        res.append(root.val)
        self.recursive(root.left, res)
        self.recursive(root.right, res)