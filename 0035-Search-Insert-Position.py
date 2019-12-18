'''
https://leetcode.com/problems/search-insert-position/
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lower, upper = 0, len(nums)-1

        while (lower<=upper):
            mid = (lower+upper)//2

            if (nums[mid]==target):
                return mid
            if (nums[mid]<target):
                lower=mid+1
            else:
                upper=mid-1
        return lower
