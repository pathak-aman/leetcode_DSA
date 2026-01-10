# We need to have as maximum meetings as possible 
# OR remove as minimum as possible

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[1])

        meeting_included = 1
        end_time = intervals[0][1]

        for i in range(1, len(intervals)):
            # print(intervals[i], end_time)
            if intervals[i][0] >= end_time:
                meeting_included += 1
                end_time = intervals[i][1]
        return len(intervals) - meeting_included