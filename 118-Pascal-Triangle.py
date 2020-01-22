'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]


'''
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        if numRows == 1:
            return [[1]]
        for i in range(1, numRows + 1):
            row = [1]
            for j in range(1,i):
                row.append(row[len(row)-1] * (i - j) // j)
            res.append(row)           
        return res
