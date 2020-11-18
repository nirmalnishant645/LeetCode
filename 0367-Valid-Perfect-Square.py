'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
'''
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start, end = 0, num
        while start <= end:
            mid = (start+end)//2
            square = mid*mid
            if square == num:
                return True
            elif square > num:
                end = mid - 1
            else:
                start = mid + 1
        return False
