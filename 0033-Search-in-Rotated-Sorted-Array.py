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
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower, upper = 0, len(nums)-1
        
        while lower <= upper:
            mid = (lower+upper)//2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target and target < nums[0]:
                lower = mid + 1
                while lower <= upper:
                    mid = (lower+upper)//2
                    
                    if nums[mid] == target:
                        return mid
                    elif nums[mid] < target:
                        lower = mid + 1
                    else:
                        upper = mid - 1
            elif nums[mid] < target and target > nums[len(nums)-1]:
                upper = mid - 1
                while lower <= upper:
                    mid = (lower+upper)//2
                    
                    if nums[mid] == target:
                        return mid
                    elif nums[mid] < target:
                        lower = mid + 1
                    else:
                        upper = mid - 1
        return -1
