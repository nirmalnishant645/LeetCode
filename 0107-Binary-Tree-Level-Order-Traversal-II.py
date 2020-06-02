'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Method 1, Iterative Solution

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        current, res = [root], []

        while current:
            nex, temp = [], []
            for n in current:
                temp.append(n.val)
                if n.left:
                    nex.append(n.left)
                if n.right:
                    nex.append(n.right)
            current = nex
            res.append(temp)
        return res[::-1]
