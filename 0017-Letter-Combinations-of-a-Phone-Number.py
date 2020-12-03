'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
'''

# Method1 using Backtracking

class Solution:
    
    def backtrack(self, res, m, digits, combination, index):
        if index > len(digits):
            return
        if len(combination) == len(digits):
            res.append(combination)
            return
        cur_digit = digits[index]
        cur_string = m[cur_digit]
        for s in cur_string:
            self.backtrack(res, m, digits, combination + s, index + 1)
    
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return res
        
        m = {'2' : 'abc', '3' : 'def', '4' : 'ghi', '5' : 'jkl', '6' : 'mno', '7' : 'pqrs', '8' : 'tuv', '9' : 'wxyz'}
        
        self.backtrack(res, m, digits, '', 0)
        
        return res

# Method 2 using Backtracking but shorthand 

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        
        if not digits:
            return res
        
        mapping = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        
        def backtrack(combination, next_digits):
            if not next_digits:
                res.append(combination)
            else:
                for letter in mapping[next_digits[0]]:
                    backtrack(combination + letter, next_digits[1:])
                    
        backtrack("", digits)
        return res