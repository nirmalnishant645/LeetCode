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
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.permutation(nums, [], res)
        return res
        
    def permutation(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            self.permutation(nums[:i] + nums[i + 1:], path + [nums[i]], res)