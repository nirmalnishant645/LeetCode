'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].

NOTE: You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
'''

from typing import List

# Simple Binary Search

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                if mid == 0 or nums[mid - 1] != target:
                    first = mid
                    break
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                
        if left > right:
            return [-1, -1]
                
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                if mid == len(nums) - 1 or nums[mid + 1] != target:
                    last = mid
                    break
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                
        return [first, last]

# Simple Binary Search in Two Different Functions

class Solution:
    
    def getFirstOccurence(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                if mid == 0 or nums[mid - 1] != target:
                    return mid
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
                
    def getLastOccurence(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                if mid == len(nums) - 1 or nums[mid + 1] != target:
                    return mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.getFirstOccurence(nums, target)
        last = self.getLastOccurence(nums, target)
        
        return [first, last]

# Simple Binary Search with only one Function

class Solution:
    
    def binarySearch(self, nums, target, flag):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target or (nums[mid] == target and flag):
                high = mid - 1
            else:
                low = mid + 1
        return low if flag else high
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.binarySearch(nums, target, True)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        else:
            return [start, self.binarySearch(nums, target, False)]

# Custom Input Check

s = Solution()
answer = s.searchRange([1, 2, 2, 3, 4, 4, 4, 4]) # [4,7]
print(answer)