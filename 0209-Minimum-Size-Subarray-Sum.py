'''
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.

Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
'''
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        i, res = 0, len(nums) + 1
        for j in range(len(nums)):
            s -= nums[j]
            while s <= 0:
                res = min(res, j - i + 1)
                s += nums[i]
                i += 1
        return res % (len(nums) + 1)
