'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3

Example 2:

Input: "IV"
Output: 4

Example 3:

Input: "IX"
Output: 9

Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''
# Time Complexity: O(n)
# Space Complexity: O(1)

# Method 1

class Solution:
    def romanToInt(self, s: str) -> int:
        
        symbol_value = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        
        result = 0
        
        for i in range(len(s)):
            
            if i > 0 and symbol_value[s[i]] > symbol_value[s[i - 1]]:
                
                result += symbol_value[s[i]] - 2 * (symbol_value[s[i - 1]])
            
            else:
                
                result += symbol_value[s[i]]
                
        return result

# Method 2 (Checking the value of next character and subtracting if more than the current character and adding if less)

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        res = 0
        for index in range(len(s) - 1):
            if roman_numerals[s[index]] < roman_numerals[s[index + 1]]:
                res -= roman_numerals[s[index]]
            else:
                res += roman_numerals[s[index]]
        return res + roman_numerals[s[-1]]