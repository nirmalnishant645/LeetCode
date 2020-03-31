'''
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

 

Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.

Example 2:

Input: "aba"
Output: False

Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
'''
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        i, j, l = 1, 0, len(s)
        lookup = [0] * (l + 1)

        while i < l:
          if s[i] == s[j]:
            i += 1
            j += 1
            lookup[i] = j
          elif not j:
            i += 1
          else:
            j = lookup[j]
        return lookup[l] and not lookup[l] % (l - lookup[l])
