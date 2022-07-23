'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''

# Method 1 (Comparing each String)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        lcp = strs[0]
        for index in range(1, len(strs)):
            lcp = self.sub_compare(lcp, strs[index])
            if not lcp:
                return ""
        return lcp
        
    def sub_compare(self, s1, s2):
        res = ""
        if len(s2) < len(s1):
            s1, s2 = s2, s1
        for index, char in enumerate(s1):
            if char == s2[index]:
                res += char
            else:
                break
        return res