class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        n = len(intervals)

        i = 0
        
        # All intervals that end before start of newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        

        while i < n and intervals[i][0] <= newInterval[1] and newInterval[0] <= intervals[i][1]:
            newInterval = [
                min(intervals[i][0], newInterval[0]),
                max(intervals[i][1], newInterval[1]),
            ]
            i +=1
        result.append(newInterval)


        # All interval whose start time is after the end of new merged interval
        while i < n and intervals[i][0] >= newInterval[1]:
            result.append(intervals[i])
            i += 1
       
        return result
        
