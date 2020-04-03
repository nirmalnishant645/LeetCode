'''
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:

Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]] 
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

Example 2:

Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]] 
Explanation: The palindromes are ["battab","tabbat"]
'''
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        words = {word : i for i, word in enumerate(words)}
        res = []
        
        for word, k in words.items():
            for j in range(len(word) + 1):
                pre = word[:j]
                post = word[j:]
                if self.is_palindrome(pre):
                    back = post[::-1]
                    if back != word and back in words:
                        res.append([words[back], k])
                if j != len(word) and self.is_palindrome(post):
                    back = pre[::-1]
                    if back != word and back in words:
                        res.append([k, words[back]])
        return res
                        
    def is_palindrome(self, check):
        return check == check[::-1]
