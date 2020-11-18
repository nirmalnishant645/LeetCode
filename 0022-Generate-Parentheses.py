'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(res, s, opening, closing, max_pairs):
            if len(s) == max_pairs * 2:
                res.append(s)
                return
            if opening < max_pairs:
                backtrack(res, s + '(', opening + 1, closing, max_pairs)
            if closing < opening:
                backtrack(res, s + ')', opening, closing + 1, max_pairs)
        
        backtrack(res, "", 0, 0, n)
        return res