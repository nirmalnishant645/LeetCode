'''
https://leetcode.com/problems/move-zeroes/description/

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero] = nums[i]
                non_zero += 1
        for i in range(non_zero, len(nums)):
            nums[i] = 0