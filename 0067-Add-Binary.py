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
class Solution:
    def addBinary(self, a: str, b: str) -> str:
      res = []
      i = len(a) - 1
      j = len(b) - 1
      carry = '0'
      while i >= 0 or j >=0:
        ach = a[i] if i >= 0 else '0'
        bch = b[j] if j >= 0 else '0'
        if ach == bch:
          res.append(carry)
          carry = ach
        else:
          res.append('1' if carry == '0' else '0')
        i -= 1
        j -= 1

      if carry == '1':
        res.append(carry)

      return ''.join(res[::-1])
