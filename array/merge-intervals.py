class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        result=[intervals[0]]
        for interval in intervals[1:]:
            last_interval=result[-1]
            if interval[0]<=last_interval[1]:
                last_interval[1]=max(interval[1],last_interval[1])

            else:
                result.append(interval)
        return result

