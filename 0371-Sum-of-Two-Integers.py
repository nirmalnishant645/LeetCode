'''
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1
'''
class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        mask = 0xffffffff
        
        while (b & mask) > 0:
            
            carry = (a & b) << 1
            a ^= b            
            b = carry
            
        return a & mask if b > 0 else a