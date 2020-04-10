'''
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
'''
class Solution:
    def calculate(self, s: str) -> int:
        num, stack, sign = 0, [], "+"
        
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
                
            if s[i] in "+-*/" or i == len(s) - 1:
                
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                else:
                    stack.append(int(stack.pop()/num))
                    
                num = 0
                sign = s[i]
                
        return sum(stack)
