class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        n = len(intervals)
        intervals.sort()

        result.append(intervals[0])

        for i in range(1, n):
            # Overlapping condition:
            if result[-1][0] <= intervals[i][1] and intervals[i][0] <= result[-1][1]:
                result[-1] = [
                    min(result[-1][0], intervals[i][0]),
                    max(result[-1][1], intervals[i][1])
                ]
            else:
                result.append(intervals[i])
        return result
