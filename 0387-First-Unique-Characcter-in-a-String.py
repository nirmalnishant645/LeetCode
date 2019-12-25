'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters.
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
        for i in range(len(s)):
            if s[i] not in dict:
                dict.update({s[i] : [i, 1]})
            else:
                dict.update({s[i] : [i, 0]})
        for char, count in dict.items():
            if count[1]:
                return count[0]
        return -1
