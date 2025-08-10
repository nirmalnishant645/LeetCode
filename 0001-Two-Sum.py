'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

from typing import List

# Using Hash Tables

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            temp = target-nums[i]
            if temp in dict:
                return [dict[temp], i]
            dict.update({nums[i] : i})

# Using Hash Tables (New)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index, num in enumerate(nums):
            if target - num in d.keys():
                return [d[target - num], index]
            else:
                d[num] = index

# Check Custom Input

s = Solution()
answer = s.twoSum([3,2,1,5], 8) # Testing [0,3]
print(answer)