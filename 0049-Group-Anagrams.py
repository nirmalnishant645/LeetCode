'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.
'''

from typing import List

# Using Hash Table without sorting

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1
            key = tuple(key)
            if key in d:
                d[key].append(s)
            else:
                d[key] = [s]
        return d.values()

# Using Sorting and Hash Table 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d= {}
        for s in strs:
            key = sorted(s)
            key = ''.join(key)
            if key in d:
                d[key].append(s)
            else:
                d[key] = [s]
        result = []
        for key, value in d.items():
            result.append(value)
        return result

# Using function to find Hash in Hash Table

class Solution:
    
    def findHash(self, s):
        return ''.join(sorted(s))
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            key = self.findHash(s)
            if key in d:
                d[key].append(s)
            else:
                d[key] = [s]
        return d.values()

# Custom Input Check

s = Solution()
answer = s.findHash(["tan","ant","act","cat"]) # [["tan","ant"],["act","cat"]]
print(answer)