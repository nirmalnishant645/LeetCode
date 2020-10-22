'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return root
        queue, res = [root], []
        while queue:
            cur, value = [], []
            for node in queue:
                value.append(node.val)
                if node.left:
                    cur.append(node.left)
                if node.right:
                    cur.append(node.right)
            queue = cur
            res.append(value)
            
        return res