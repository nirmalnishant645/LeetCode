'''
https://leetcode.com/problems/sqrtx/
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:
Input: 4
Output: 2

Example 2:
Input: 8
Output: 2

Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        lower, upper = 0, x
        while(lower<=upper):
            mid=(lower+upper)//2
            square = mid**2
            if(square==x):
                return mid
            if(square<x):
                lower = mid+1
            else:
                upper = mid-1
        return upper
