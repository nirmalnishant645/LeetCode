'''
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_prod = max_prod = res = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                min_prod, max_prod = max_prod, min_prod
            max_prod = nums[i] * max_prod if nums[i] * max_prod > nums[i] else nums[i]
            min_prod = nums[i] * min_prod if nums[i] * min_prod < nums[i] else nums[i]
            res = max_prod if max_prod > res else res
        return res
