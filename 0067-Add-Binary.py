'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''

# Method 1

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j, carry = len(a) - 1, len(b) - 1, '0'
        res = []
        while(i >= 0 or j >= 0 or carry != '0'):

            num1 = a[i] if i >= 0 else '0'
            num2 = b[j] if j >= 0 else '0'

            if num1 == num2:
                res.append(carry)
                carry = num1
            else:
                res.append('1' if carry == '0' else '0')

            i -= 1 
            j -= 1 

        return ''.join(res[::-1])

# Method 2

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j, carry, result = len(a) - 1, len(b) - 1, 0, []
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            result.append(str(total%2))
            carry = total//2
            
        return ''.join(result[::-1])