'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort()
        res = []
        cur_interval = intervals[0]
        res.append(cur_interval)
        
        for interval in intervals:
            if cur_interval[1] >= interval[0]:
                res[-1][1] = max(cur_interval[1], interval[1])
            else:
                cur_interval = interval
                res.append(cur_interval)
                
        return res