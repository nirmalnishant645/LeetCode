'''
Given the root of a binary tree, return the postorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [3,2,1]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
Example 4:


Input: root = [1,2]
Output: [2,1]
Example 5:


Input: root = [1,null,2]
Output: [2,1]
 

Constraints:

The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up:

Recursive solution is trivial, could you do it iteratively?
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.recursive(root, res)
        return res
    
    def recursive(self, root, res):
        if not root:
            return
        self.recursive(root.left, res)
        self.recursive(root.right, res)
        res.append(root.val)

# Iterative

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node and visited:
                res.append(node.val)
            elif node:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
                
        return res