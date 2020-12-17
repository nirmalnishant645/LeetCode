'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''

from typing import List

# Bit Manipulation

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0 
        for num in nums:
            res ^= num
        return res

# Hash Set

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique = set()
        for num in nums:
            unique.add(num)
        return (2 * sum(unique)) - sum(nums)

# Hash Set One Liner

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2*(sum(set(nums))) - sum(nums)

# Hash Table

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique = {}
        for num in nums:
            if num in unique:
                unique[num] += 1
            else:
                unique[num] = 1
        for key, value in unique.items():
            if value == 1:
                return key

# Check Custom Input

s = Solution()
answer = s.singleNumber([3, 3, 2, 2, 1]) # 1
print(answer)