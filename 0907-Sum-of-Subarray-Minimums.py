'''
Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.

Since the answer may be large, return the answer modulo 10^9 + 7.

 

Example 1:

Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.

 

Note:

    1 <= A.length <= 30000
    1 <= A[i] <= 30000
'''
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        res = 0
        s = []
        A = [0] + A + [0]
        for idx, a in enumerate(A):
            while s and A[s[-1]] > a:
                i = s.pop()
                j = s[-1]
                res += A[i] * (idx - i) * (i - j)
            s.append(idx)
        return res % (10 ** 9 + 7)
