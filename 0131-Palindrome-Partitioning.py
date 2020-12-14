'''
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
A palindrome string is a string that reads the same backward as forward.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]
 
Constraints:
1 <= s.length <= 16
s contains only lowercase English letters.
'''

# Using DFS

class Solution:
    
    def isPalindrome(self, seg):
        start, end = 0, len(seg) - 1
        
        while start < end:
            if seg[start] != seg[end]:
                return False
            start += 1
            end -= 1
        return True
    
    def dfs(self, s, temp, res):
        if not s and temp:
            res.append(temp[:])
            return
        for i in range(1, len(s) + 1):
            seg = s[:i]
            if self.isPalindrome(seg):
                temp.append(seg)
                self.dfs(s[i:], temp, res)
                temp.pop()
    
    def partition(self, s: str) -> List[List[str]]:
        res = []
        temp = []
        self.dfs(s, temp, res)
        return res