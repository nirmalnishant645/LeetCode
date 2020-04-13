'''
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
'''
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {0: 0}
        max_len = count = 0
        for i, num in enumerate(nums, 1):
            if not num:
                count -= 1
            else:
                count += 1
            if count in d:
                max_len = max(max_len, i - d[count])
            else:
                d[count] = i
        return max_len
