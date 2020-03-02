'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''
#Method 1
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        summ = maxSum = nums[0]
        for i in range(1, len(nums)):
            summ = nums[i] if summ<0 else summ+nums[i]
            maxSum = summ if summ>maxSum else maxSum
        return maxSum

#Method 2
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        cur_sum = max_sum = nums[0]
        for i in range(1, len(nums)):
            cur_sum = nums[i] if nums[i] > cur_sum + nums[i] else cur_sum + nums[i]
            max_sum = cur_sum if cur_sum > max_sum else max_sum
        return max_sum
