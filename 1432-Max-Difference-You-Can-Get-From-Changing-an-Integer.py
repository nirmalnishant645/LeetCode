'''
You are given an integer num. You will apply the following steps exactly two times:

Pick a digit x (0 <= x <= 9).
Pick another digit y (0 <= y <= 9). The digit y can be equal to x.
Replace all the occurrences of x in the decimal representation of num by y.
The new integer cannot have any leading zeros, also the new integer cannot be 0.
Let a and b be the results of applying the operations to num the first and second times, respectively.

Return the max difference between a and b.

 

Example 1:

Input: num = 555
Output: 888
Explanation: The first time pick x = 5 and y = 9 and store the new integer in a.
The second time pick x = 5 and y = 1 and store the new integer in b.
We have now a = 999 and b = 111 and max difference = 888
Example 2:

Input: num = 9
Output: 8
Explanation: The first time pick x = 9 and y = 9 and store the new integer in a.
The second time pick x = 9 and y = 1 and store the new integer in b.
We have now a = 9 and b = 1 and max difference = 8
Example 3:

Input: num = 123456
Output: 820000
Example 4:

Input: num = 10000
Output: 80000
Example 5:

Input: num = 9288
Output: 8700
 

Constraints:

1 <= num <= 10^8
'''
class Solution:
    def maxDiff(self, num: int) -> int:
        a, b = ([d for d in str(num)] for _ in range(2))
        x, y = a[0], ' ' 
        for i, ch in enumerate(a):
            if ch == x:
                a[i] = '9'
                b[i] = '1'
            else:
                if x == '1' and ord(ch) > ord('0') or x == '9' and ord(ch) < ord('9'):
                    if y == ' ':
                        y = ch
                    if y == ch:
                        if x == '1':
                            b[i] = '0'
                        else:
                            a[i] = '9'
        return int(''.join(a)) - int(''.join(b))
