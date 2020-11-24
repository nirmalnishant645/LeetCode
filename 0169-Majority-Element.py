'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
Input: [3,2,3]
Output: 3

Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2
'''

from typing import List

# O(1) Space Complexity Solution 1

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = count = 0
        for num in nums:
            if num == n:
                count += 1
            elif not count:
                n = num
                count += 1
            else:
                count -= 1
        return n

# Custom Input Check

s = Solution()
answer = s.majorityElement([1, 1, 1, 5]) # 1
print(answer)