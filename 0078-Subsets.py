'''
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
 

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
'''

# Using Backtracking

class Solution:
    
    def backtrack(self, nums, res, cur, index):
        if index > len(nums):
            return
        res.append(cur[:])
        for i in range(index, len(nums)):
            if nums[i] not in cur:
                cur.append(nums[i])
                self.backtrack(nums, res, cur, i)
                cur.pop()
        return
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, cur = [], []
        self.backtrack(nums, res, cur, 0)
        return res