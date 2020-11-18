'''
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
'''
class Solution:
    def frequencySort(self, s: str) -> str:
        d1, d2 = {}, {}
        for c in s:
            d1[c] = d1.get(c, 0) + 1

        for k,v in d1.items():
            d2[v] = d2.get(v, '') + k*v

        res = ''
        for i in range(len(s), -1, -1):
            if i in d2:
                res += d2[i]
        return res
