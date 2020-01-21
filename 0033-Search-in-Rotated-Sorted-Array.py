'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''
#Method NN
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower, upper = 0, len(nums)-1
        while lower <= upper:
            flag, mid = 1, (lower+upper)//2
            if nums[mid] == target:
                return mid
            elif nums[lower] <= nums[mid]:
                if flag and nums[lower] <= target < nums[mid]:
                    upper = mid - 1
                    flag = 0
                    continue
                lower = mid + 1
            else:
                if flag and nums[mid] < target <= nums[upper]:
                    lower = mid + 1 
                    flag = 0
                    continue
                upper = mid - 1
        return -1
    
#Method AK
class Solution(object):
    def search(self, nums, target):
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end)//2
            if nums[mid] == target:
                return mid
            elif nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid -1
                else:
                    start = mid + 1
            else:
                if nums[end] >= target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1
