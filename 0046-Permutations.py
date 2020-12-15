'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

# Using Backtracking

class Solution:
    
    def backtrack(self, nums, res, cur):
        if not nums:
            res.append(cur)
        for i in range(len(nums)):
            self.backtrack(nums[:i] + nums[i+1:], res, cur + [nums[i]])
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        cur = []
        res = []
        self.backtrack(nums, res, cur)
        return res