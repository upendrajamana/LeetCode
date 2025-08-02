class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count=0
        intervals.sort(key=lambda x: x[0])
        prev_end=intervals[0][1]
        for interval in range(1,len(intervals)):
            if intervals[interval][0]<prev_end:
                count+=1
                prev_end = min(prev_end, intervals[interval][1])
            else:
                prev_end = intervals[interval][1]
        return count