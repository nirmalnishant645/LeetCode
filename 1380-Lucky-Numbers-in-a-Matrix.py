'''
Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

 

Example 1:

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column

Example 2:

Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.

Example 3:

Input: matrix = [[7,8],[1,2]]
Output: [7]

 

Constraints:

    m == mat.length
    n == mat[i].length
    1 <= n, m <= 50
    1 <= matrix[i][j] <= 10^5.
    All elements in the matrix are distinct.
'''
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        row_mins = [10**5 + 1] * m
        col_maxs = [0] * n
        
        for i in range(m):
            for j in range(n):
                row_mins[i] = row_mins[i] if row_mins[i] < matrix[i][j] else matrix[i][j]
                col_maxs[j] = col_maxs[j] if col_maxs[j] > matrix[i][j] else matrix[i][j]
        
        for i in row_mins:
            if i in col_maxs:
                    return [i]
