'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

# Using Sliding Window

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSum = max(curSum, maxSum)
        return maxSum
        

# Using Kadane's Algorithm METHOD 1

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        cur_sum = max_sum = nums[0]
        
        for i in range(1, len(nums)):
            
            cur_sum = max(nums[i] + cur_sum, nums[i])
            max_sum = max(cur_sum, max_sum)
            
        return max_sum

# Using Kadane's Algorithm METHOD 2

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum, max_sum = 0, nums[0]
        
        for num in nums:
            cur_sum = max(num, cur_sum + num)
            max_sum = max(cur_sum, max_sum) 
            
        return max_sum