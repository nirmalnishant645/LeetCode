'''
Given a balanced parentheses string S, compute the score of the string based on the following rule:

    () has score 1
    AB has score A + B, where A and B are balanced parentheses strings.
    (A) has score 2 * A, where A is a balanced parentheses string.

 

Example 1:

Input: "()"
Output: 1

Example 2:

Input: "(())"
Output: 2

Example 3:

Input: "()()"
Output: 2

Example 4:

Input: "(()(()))"
Output: 6

 

Note:

    S is a balanced parentheses string, containing only ( and ).
    2 <= S.length <= 50
'''
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        res = bal = 0
        for idx, s in enumerate(S):
            if s == '(':
                bal += 1
            else:
                bal -= 1
                if S[idx - 1] == '(':
                    res += 1 << bal
        return res
